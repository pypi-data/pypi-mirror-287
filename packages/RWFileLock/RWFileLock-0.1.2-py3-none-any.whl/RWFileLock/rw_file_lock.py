#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# coding: utf-8

# SPDX-License-Identifier: LGPL-2.1-or-later
# RWFileLock: Readers / writers file lock Python helper class
# Copyright 2020-2024 Barcelona Supercomputing Center (BSC), Spain
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import os
import contextlib
import tempfile
import fcntl

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import (
        Iterator,
        Optional,
        Union,
    )


class LockError(Exception):
    def __init__(self, message: "str"):
        super().__init__(message)


class RWFileLock(object):
    def __init__(self, filename: "Union[str, os.PathLike[str]]"):
        self.lock_fd = os.open(filename, (os.O_RDWR | os.O_CREAT), mode=0o700)
        self.isLocked = False

    def r_lock(self) -> "None":
        if self.isLocked:
            raise LockError("Already locked by ourselves")

        try:
            fcntl.lockf(self.lock_fd, (fcntl.LOCK_SH | fcntl.LOCK_NB))
            self.isLocked = True
        except IOError:
            raise LockError("Already locked by others")

    def r_blocking_lock(self) -> "None":
        if self.isLocked:
            raise LockError("Already locked by ourselves")

        fcntl.lockf(self.lock_fd, fcntl.LOCK_SH)
        self.isLocked = True

    def w_lock(self) -> "None":
        if self.isLocked:
            raise LockError("Already locked by ourselves")

        try:
            fcntl.lockf(self.lock_fd, (fcntl.LOCK_EX | fcntl.LOCK_NB))
            self.isLocked = True
        except IOError:
            raise LockError("Already locked by others")

    def w_blocking_lock(self) -> "None":
        if self.isLocked:
            raise LockError("Already locked by ourselves")

        fcntl.lockf(self.lock_fd, fcntl.LOCK_EX)
        self.isLocked = True

    def unlock(self) -> "None":
        if self.isLocked:
            try:
                fcntl.lockf(self.lock_fd, fcntl.LOCK_UN)
            except IOError:
                raise LockError("Already locked by others")
            finally:
                self.isLocked = False
        else:
            raise LockError("No lock was held")

    @contextlib.contextmanager
    def shared_lock(self) -> "Iterator[None]":
        self.r_lock()
        try:
            yield
        finally:
            self.unlock()

    @contextlib.contextmanager
    def shared_blocking_lock(self) -> "Iterator[None]":
        try:
            self.r_lock()
            yield
        finally:
            self.unlock()

    @contextlib.contextmanager
    def exclusive_lock(self) -> "Iterator[None]":
        self.w_lock()
        try:
            yield
        finally:
            self.unlock()

    @contextlib.contextmanager
    def exclusive_blocking_lock(self) -> "Iterator[None]":
        try:
            self.w_blocking_lock()
            yield
        finally:
            self.unlock()

    def __del__(self) -> "None":
        try:
            os.close(self.lock_fd)
        except:
            pass


if __name__ == "__main__":
    lock = RWFileLock("/tmp/rwfilelock.lock")

    print("Trying getting lock")
    import sys

    sys.stdout.flush()
    try:
        if len(sys.argv) > 1:
            with lock.exclusive_lock():
                import time

                time.sleep(10)
        else:
            with lock.shared_lock():
                import time

                time.sleep(10)
    except LockError:
        print("Unable to get lock")
