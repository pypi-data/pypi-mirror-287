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

"""Stuff we need only on the development host"""

import logging
import os
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType

from mpide.target.mpide.misc import file_checksum


def log() -> logging.Logger:
    """Returns the logger instance to use here"""
    return logging.getLogger("trickkiste.mpide.utils")


def load_module(filepath: str | Path) -> ModuleType:
    """(Re)loads a python module specified by @filepath"""
    log().debug("load module '%s' from '%s'", Path(filepath).stem, filepath)
    spec = spec_from_file_location(Path(filepath).stem, filepath)
    if not (spec and spec.loader):
        raise RuntimeError("Could not load")
    module = module_from_spec(spec)
    assert module
    assert isinstance(spec.loader, SourceFileLoader)
    loader: SourceFileLoader = spec.loader
    # here the actual track definition takes place
    loader.exec_module(module)
    return module


def mpyfy(source_path: Path | str, mpy_cross: Path | str) -> Path:
    """Takes a filename and in case it's being identified as .mpy a precompiled
    mpy file gets generated from the correspondent py file and it's path is
    returned. Just return the original filename without any action otherwise
    """
    path = Path(source_path)
    if path.suffix != ".py":
        return path
    cs_file = Path("mpy_cache") / f"{path.stem}-{file_checksum(path.as_posix())}.mpy"
    if not cs_file.exists():
        cs_file.parent.mkdir(parents=True, exist_ok=True)
        os.system(f"{mpy_cross} {path.as_posix()} -o {cs_file}")
    return cs_file
