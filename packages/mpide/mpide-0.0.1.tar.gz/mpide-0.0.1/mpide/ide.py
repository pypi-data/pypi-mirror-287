#!/usr/bin/env python3

"""Magic REPL for MicroPython development"""

#
# - [ ] command history
# - [ ] bootstrap
# - [ ] auto-update mpy/py files
# - [ ] persist

import asyncio
import logging

from textual import work
from textual.app import ComposeResult
from textual.widgets import TextArea, Input, Pretty
from textual.containers import Vertical, Container
from trickkiste.base_tui_app import TuiBaseApp
from textual.binding import Binding
from mpremote.main import State
import builtins
import io

def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("trickkiste.muide")

class PrintWrapper(io.StringIO):
    def __call__(self, *args, **kwargs):
        log().info("%s", args)


class MpIDE(TuiBaseApp):
    CSS = """
        Header {text-style: bold;}
        #app-grid {
            layout: grid;
            grid-size: 2;  /* two columns */
            grid-columns: 2fr 1fr;
            grid-rows: 1fr;
        }
        #left-pane > Static {
            background: $boost;
            color: auto;
            margin-bottom: 1;
            padding: 1;
        }
        #left-pane {
            width: 100%;
            height: 100%;
            row-span: 2;
            background: $panel;
            border: dodgerblue;
        }
        #status-view > Static {
            width: auto;
            height: 100%;
            margin-right: 1;
            background: $boost;
        }
        #status-view {
            height: 100%;
            background: $panel;
            border: mediumvioletred;
        }
        Button  {width: 40;}
        #button_grid {
            grid-size: 3;
            height: auto;
        }
    """
    BINDINGS = [
        Binding("ctrl+c", "ctrlc"),
        Binding("ctrl+x", "app.quit", "Quit", show=True),
    ]
    class Prompt(Input):
        BINDINGS = [
            # overrides pre-defined Binding
            Binding("ctrl+d", "app.ctrld"),
        ]

    def __init__(self) -> None:
        super().__init__(logger_show_funcname=True, logger_show_tid=True, logger_show_name=True)
        self.code_log = TextArea(read_only=True, language="python", theme="dracula")
        self.code_log.can_focus = False
        self.repl_input = MpIDE.Prompt()
        self.status_view = Pretty(None, id="status-view")
        self._mqueue = asyncio.Queue()
        self.state = State()

    def compose(self) -> ComposeResult:
        """Set up the UI"""
        with Container(id="app-grid"):
            with Vertical(id="left-pane"):
                yield self.code_log
                yield self.repl_input
            yield self.status_view
        yield from super().compose()

    async def initialize(self) -> None:
        """UI entry point"""
        self.set_log_levels((log(), "DEBUG"), ("trickkiste", "INFO"), others_level="WARNING")
        await asyncio.sleep(0.1)  # wait for window resize updates, to avoid ugly logs
        builtins.print = PrintWrapper()  # redirect `print` messages from mpremote
        self.ensure_connection()
        self.handle_messages()

    async def on_input_submitted(self) -> None:
        await self._mqueue.put(self.repl_input.value)
        self.repl_input.value = ""

    async def action_ctrlc(self) -> None:
        log().debug("CTRL-C")
        await self._mqueue.put(":ctrl-c")

    async def action_ctrld(self) -> None:
        log().debug("CTRL-D")
        await self._mqueue.put(":ctrl-d")

    @work(exit_on_error=True)
    async def ensure_connection(self) -> None:
        while True:
            if self.state.transport:
                await asyncio.sleep(1)
                continue
            try:
                log().info("connect..")
                self.state.ensure_friendly_repl()
                self.state.did_action()
                self.print_serial()
                self.status_view.styles.background = "darkblue"
            except SystemExit as exc:
                log().error("got SystemExit from mpremote - this indicates no device is connected")
                self.abort_connection()
            except Exception as exc:
                log().error(f"{exc}")
            await asyncio.sleep(2)

    @work(exit_on_error=True)
    async def handle_messages(self) -> None:
        """Reads messages from a queue and operates on serial. This is the only function
        allowed to write to serial to avoid conflicts (thus the queue)"""
        while True:
            element = await self._mqueue.get()
            log().info(f"{element}")
            if isinstance(element, str):
                try:
                    if element == ":ctrl-d":
                        self.state.transport.write_ctrl_d(self.add_serial_output)
                    elif element == ":ctrl-c":
                        self.state.transport.serial.write(b"\x03")
                    else:
                        self.state.transport.serial.write(f"{element}\r\n".encode())
                except OSError as exc:
                    log().error(f"{exc}")
                    self.abort_connection()
                except Exception as exc:
                    log().error(f"{exc}")

    @work(exit_on_error=True)
    async def print_serial(self) -> None:
        """Reads data from serial and adds it to the output"""
        while True:
            try:
                # busy wait for data - we have to go away from mpremote to make this async..
                if not (n := self.state.transport.serial.inWaiting()):
                    await asyncio.sleep(0.1)
                    continue
                if (dev_data_in := self.state.transport.serial.read(n)) is not None:
                    self.add_serial_output(dev_data_in.decode())
            except OSError as exc:
                log().error(f"{exc}")
                self.abort_connection()
                return

    def abort_connection(self):
        self.status_view.styles.background = "red"
        self.state = State()

    def add_serial_output(self, data:str) -> None:
        self.code_log.text += data
        self.code_log.scroll_end()



def main():
    MpIDE().execute()


if __name__ == "__main__":
    main()
