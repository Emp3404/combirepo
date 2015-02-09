#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import tempfile
import atexit
import shutil


# FIXME: Rename default names of temporary files and directories when the
# default name of our utility will be chosen. Now they all have prefix
# "tizen-sanitizer". Also it should be better to have some "macro" for it.


def create_temporary_file(file_suffix):
    """
    Creates temporary file in tmpfs, named as follows:

    /tmp/tizen-sanitizer.<random>.<suffix>

    @param file_suffix      The suffix of temporary file.

    @return                 The path to created temporary file.
    """
    file_descriptor, path = tempfile.mkstemp(prefix='tizen-sanitizer.',
                                             suffix="." + file_suffix)
    file_descriptor.close()  # This helps to avoid the file descriptor leak.
    atexit.register(shutil.rmtree, path)  # It will be removed at exit.
    logging.debug("Created temporary file {0}".format(path))
    return path


# FIXME: Ditto.
def create_temporary_directory(directory_suffix):
    """
    Creates temporary directory in tmpfs, named as follows:

    /tmp/tizen-sanitizer.<random>.<suffix>

    @param file_suffix      The suffix of temporary directory.

    @return                 The path to created temporary directory.
    """
    path = tempfile.mkdtemp(prefix='tizen-sanitizer.',
                            suffix="." + directory_suffix)
    atexit.register(shutil.rmtree, path)  # It will be removed at exit.
    logging.debug("Created temporary file {0}".format(path))
    return path