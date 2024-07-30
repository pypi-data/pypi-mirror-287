#!/usr/bin/env python3
#                  _     _
#  _ __ ___  _ __ (_) __| | ___
# | '_ ` _ \| '_ \| |/ _` |/ _ \
# | | | | | | |_) | | (_| |  __/
# |_| |_| |_| .__/|_|\__,_|\___|
#           |_|
#
# mpide - MicroPython (Integrated) Development Environment
# Copyright (C) 2024 - Frans Fürst
#
# mpide is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# mpide is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details at <http://www.gnu.org/licenses/>.
#
# Anyway this project is not free for machine learning. If you're using any content of this
# repository to train any sort of machine learned model (e.g. LLMs), you agree to make the whole
# model trained with this repository and all data needed to train (i.e. reproduce) the model
# publicly and freely available (i.e. free of charge and with no obligation to register to any
# service) and make sure to inform the author (me, frans.fuerst@protonmail.com) via email how to
# get and use that model and any sources needed to train it.

"""Magic REPL and file synchronization toolbox"""

# pylint: disable=too-many-branches
# pylint: disable=too-many-statements

import asyncio
import builtins
import io
import logging
import sys
from collections.abc import Iterator, MutableSequence
from contextlib import contextmanager, suppress
from pathlib import Path

import yaml
from apparat import fs_changes
from mpremote.main import State  # type: ignore[import-untyped]
from mpremote.transport import TransportError  # type: ignore[import-untyped]
from rich.syntax import Syntax
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Input, Label, RichLog
from trickkiste.base_tui_app import TuiBaseApp

from mpide.utils import load_module, mpyfy

__version__ = "0.1.0"  # It MUST match the version in pyproject.toml file

STARTUP_HELPTEXT = f"""{'<br>' * 50}
Quick reference
:snippet         # run snippet
:cat <file>      # plot @file to REPL
:cp <src> <dst>  # copy file from host to target
CTRL+D           # soft-reboot
CTRL+C           # send keyboard interrupt
CTRL+X           # quit application
__________________________________________________
""".replace(
    "<br>", "\n"
)


def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("trickkiste.mpide")


class MpIDE(TuiBaseApp):
    """mpide Textual app tailoring all features"""

    MPIDE_DIR = Path(__file__).parent
    CSS_PATH = MPIDE_DIR / "mpide.css"
    PROJECT_DIR = Path(".").absolute()
    MPIDE_LOCAL_DIR = PROJECT_DIR / ".mpide"

    BINDINGS = [
        Binding("ctrl+x", "app.quit", "Quit", show=True),
        Binding("ctrl+c", "ctrlc"),
        Binding("up", "arrow_up"),
        Binding("down", "arrow_down"),
    ]

    class Prompt(Input):
        """Specialization for Input just in order to re-direct ctrl+d"""

        BINDINGS = [
            # overrides pre-defined Binding
            Binding("ctrl+d", "app.ctrld"),
        ]

    class PrintWrapper(io.StringIO):
        """Acts like print() and redirects to log"""

        def __call__(self, *args: object, **kwargs: object) -> None:
            log().info("%s", args)

    def __init__(self) -> None:
        super().__init__(logger_show_funcname=True, logger_show_tid=True, logger_show_name=True)
        self.code_log = RichLog(id="code-log", wrap=True)
        self.code_log.can_focus = False
        self.repl_input = self.Prompt(id="repl-input")
        self.prefix_label = Label("", id="prefix-label")
        self._mqueue: asyncio.Queue[str] = asyncio.Queue()
        self.history: MutableSequence[str] = []
        self.state = State()
        self.title = f"MPIDE - {self.PROJECT_DIR.relative_to(Path('~').expanduser())}"

    def compose(self) -> ComposeResult:
        """Set up the UI"""
        yield Header(show_clock=True, id="header")
        with Vertical(id="left-pane"):
            yield self.code_log
            with Horizontal(id="input-pane"):
                yield self.prefix_label
                yield self.repl_input
        yield from super().compose()

    async def initialize(self) -> None:
        """UI entry point"""
        self.set_log_levels((log(), "DEBUG"), ("trickkiste", "INFO"), others_level="WARNING")
        self.add_serial_output(STARTUP_HELPTEXT)
        await asyncio.sleep(0.1)  # wait for window resize updates, to avoid ugly logs
        # redirect `print` messages from mpremote
        builtins.print = self.PrintWrapper()  # type: ignore [assignment]
        self.ensure_connection()
        self.handle_messages()
        self.watch_fs_changes()
        self.MPIDE_LOCAL_DIR.mkdir(exist_ok=True)
        with suppress(FileNotFoundError):
            with (self.MPIDE_LOCAL_DIR / "command_history.yaml").open(encoding="utf-8") as in_file:
                self.history = yaml.load(in_file, Loader=yaml.Loader)
        self.set_status_info()

    def cleanup(self) -> None:
        """UI shutdown"""
        with (self.MPIDE_LOCAL_DIR / "command_history.yaml").open(
            "wt", encoding="utf-8"
        ) as out_file:
            yaml.dump(self.history, out_file)

    async def on_input_submitted(self) -> None:
        """Invoke functionality after pressing Return in input field"""
        await self._mqueue.put(self.repl_input.value)
        self.repl_input.value = ""

    async def action_ctrlc(self) -> None:
        """React on CTRL-C"""
        await self._mqueue.put(":ctrl-c")

    async def action_ctrld(self) -> None:
        """React on CTRL-D"""
        await self._mqueue.put(":ctrl-d")

    async def action_arrow_up(self) -> None:
        """React on UP"""
        await self._mqueue.put(":up")

    async def action_arrow_down(self) -> None:
        """React on DOWN"""
        await self._mqueue.put(":down")

    @work(exit_on_error=True)
    async def ensure_connection(self) -> None:
        """Continuously tries to connect"""
        while True:
            if self.state.transport:
                await asyncio.sleep(1)
                continue
            try:
                log().info("connect..")
                self.state.ensure_friendly_repl()
                self.state.did_action()
                self.state.transport.serial.write(b"\r\n")
                self.print_serial()
                self.set_status_info()
            except SystemExit:
                log().error("got SystemExit from mpremote - this indicates no device is connected")
                self.abort_connection()
            except Exception as exc:  # pylint: disable=broad-except
                log().error("%s", exc)
            await asyncio.sleep(2)

    @contextmanager
    def raw_repl(self) -> Iterator[None]:
        """Convenience decorator for entering raw repl"""
        try:
            self.state.transport.enter_raw_repl(soft_reset=False)
            yield
        finally:
            self.state.transport.exit_raw_repl()

    @work(exit_on_error=True)
    async def handle_messages(self) -> None:
        """Reads messages from a queue and operates on serial. This is the only function
        allowed to write to serial to avoid conflicts (thus the queue)"""
        history_cursor = 0
        while True:
            element = await self._mqueue.get()
            log().debug("got element %s", element)
            command_entered = True
            if isinstance(element, str):
                try:
                    if element == ":up":
                        command_entered = False
                        history_cursor = max(history_cursor - 1, -len(self.history))
                        with suppress(IndexError):
                            self.repl_input.value = self.history[history_cursor]
                    elif element == ":down":
                        command_entered = False
                        history_cursor = min(history_cursor + 1, 0)
                        with suppress(IndexError):
                            self.repl_input.value = (
                                self.history[history_cursor] if history_cursor else ""
                            )
                    elif element == ":ctrl-d":
                        command_entered = False
                        self.state.transport.write_ctrl_d(self.add_serial_output)
                    elif element == ":ctrl-c":
                        command_entered = False
                        self.state.transport.serial.write(b"\x03")
                    elif element == ":snippet":
                        with (self.MPIDE_DIR / "target/mpide/setup_ramdisk.py").open() as file:
                            snippet = file.read()
                        with self.raw_repl():
                            try:
                                self.state.transport.exec_raw_no_follow(snippet.encode())
                            except TransportError as exc:
                                self.add_serial_output(f"Error: {exc}")
                    elif element.startswith(":cp "):
                        _, source_raw, target_raw = element.split()
                        log().debug("cp %s %s", source_raw, target_raw)
                        if source_raw.endswith(".py") and target_raw.endswith(".mpy"):
                            source_path = self.precompiled_from(Path(source_raw))
                        else:
                            source_path = Path(source_raw)
                        with self.raw_repl():
                            # self.state.transport.fs_cp(source, target)
                            log().debug("cp %s %s", source_path, target_raw)
                            with open(source_path, "rb") as in_file:
                                self.state.transport.fs_writefile(target_raw, in_file.read())
                    elif element.startswith(":cat "):
                        _, path = element.split()
                        log().debug("cat %s", path)
                        with self.raw_repl():
                            self.state.transport.exec_raw_no_follow(
                                f"with open('{path}') as f: print(f.read())"
                            )
                    else:
                        self.state.transport.serial.write(f"{element}\r\n".encode())

                except OSError as exc:
                    log().error("could not write: %s", exc)
                    self.abort_connection()
                except Exception as exc:  # pylint: disable=broad-except
                    log().error("could not write: %r", exc)

            if command_entered:
                if element.strip():
                    self.history.append(element)
                history_cursor = 0

    @work(exit_on_error=True)
    async def print_serial(self) -> None:
        """Reads data from serial and adds it to the output"""
        while True:
            try:
                # busy wait for data - we have to go away from mpremote to make this async..
                if not (num_bytes := self.state.transport.serial.inWaiting()):
                    await asyncio.sleep(0.1)
                    continue
                if (dev_data_in := self.state.transport.serial.read(num_bytes)) is not None:
                    self.add_serial_output(dev_data_in.decode())
            except OSError as exc:
                log().error("could not read: %s", exc)
                self.abort_connection()
                return

    def abort_connection(self) -> None:
        """Reset connection and show flashy connection state"""
        self.state = State()
        self.set_status_info()

    def set_status_info(self) -> None:
        """Sets text and color of status bar"""
        connected_device = (
            f"connected to {self.state.transport.device_name}" if self.state.transport else ""
        )
        self.update_status_bar(
            # f" PID: {current_process.pid}"
            # f" / {current_process.cpu_percent():6.1f}% CPU"
            # f" / {len(tasks)} tasks"
            # f" │ System CPU: {cpu_percent:5.1f}% / {int(cpu_percent * cpu_count):4d}%"
            # f" │ mpcross/micropython/idf"
            f" Status: {connected_device or 'not connected'}"
            f" │ mpide v{__version__}"
        )
        self._footer_label.styles.background = "#224422" if connected_device else "#442222"

    def add_serial_output(self, data: str) -> None:
        """Append stuff to the REPL log"""
        *head, tail = data.rsplit("\n", maxsplit=1)
        self.prefix_label.update(tail)
        if head:
            self.code_log.write(
                Syntax(head[0], "python", indent_guides=True, background_color="#222222")
            )

    def precompiled_from(self, path: Path) -> Path:
        """Returns path to precompiled result from @path"""
        sys.path.append(".")  # needed for loading relative stuff inside config.py
        config = load_module("config.py").config
        mpy_cross = config.get("mpy-cross_path") or "mpy-cross"
        log().debug("mpy-cross: '%s'", mpy_cross)
        return mpyfy(path, mpy_cross)

    @work(exit_on_error=True)
    async def watch_fs_changes(self) -> None:
        """Watch out for changes on filesystem and automatically update device"""

        def file_filter(path: Path) -> bool:
            return path.suffix == ".py"

        async for path in (
            _path
            async for paths in fs_changes(Path("."), min_interval=1, filter_fn=file_filter)
            for _path in paths
        ):
            log().debug("changed: %s", path)
            out_file = self.precompiled_from(path)
            log().debug("precompiled: %s", out_file)
            target_path = path.relative_to(Path(".").absolute())
            log().debug("target_path: %s", target_path)


def main() -> None:
    """Entry point for mpide application"""
    MpIDE().execute()


if __name__ == "__main__":
    main()
