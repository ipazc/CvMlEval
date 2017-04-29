#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Iván de Paz Centeno'

# Code extracted from
# http://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python/22434262#22434262

import os
import sys
from contextlib import contextmanager


def fileno(file_or_fd):
    fd = getattr(file_or_fd, 'fileno', lambda: file_or_fd)()
    if not isinstance(fd, int):
        raise ValueError("Expected a file (`.fileno()`) or a file descriptor")
    return fd


@contextmanager
def stdfile_redirector(to=os.devnull, stdfile=sys.stderr):

    stdfile_fd = fileno(stdfile)

    with os.fdopen(os.dup(stdfile_fd), 'wb') as copied:
        stdfile.flush()

        try:
            os.dup2(fileno(to), stdfile_fd)
        except ValueError:
            with open(to, 'wb') as to_file:
                os.dup2(to_file.fileno(), stdfile_fd)

        try:
            yield stdfile
        finally:
            # restore stdout to its previous value
            stdfile.flush()
            os.dup2(copied.fileno(), stdfile_fd)
