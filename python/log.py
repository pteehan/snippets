""" Simple interface to write to the log.  Also hanldles log setup and config.
Usage:

import log

log.init('mylog', 'logdir') # optional
log.info("Hello")
log.error("Hello")
log.console_level("warning")
log.file_level("info")
"""

import logging as _logging
import colorlog as _colorlog


import os as _os
from logging.handlers import RotatingFileHandler as _RotatingFileHandler

_LEVELS = {'debug': _logging.DEBUG,
          'info': _logging.INFO,
          'warning': _logging.WARNING,
          'error': _logging.ERROR,
          'critical': _logging.CRITICAL}

global_log_name = 'mylog'


def init(log_name=global_log_name, log_dir = 'log'):
    #initialize _logging handlers
    global_log_name = log_name
    filename = log_dir + "/" + log_name + ".log"

    log_dir = _os.path.dirname(filename)
    if not _os.path.isdir(log_dir):
        _os.makedirs(log_dir)

    root = _colorlog.getLogger()
    root.handlers = []
    root.setLevel(_logging.DEBUG)

    add_log_file(filename, "info")

    ch = _colorlog.StreamHandler()

    ch_formatter = _colorlog.ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    ch.setFormatter(ch_formatter)
    root.addHandler(ch)

    console_level("info")
    #logger = _logging.getLogger('ta_util')
    info("Log writing to " + filename + "; run log.init() to change")


def _get_console_handler():
    root = _colorlog.getLogger()
    handlers = root.handlers
    i =list(map(lambda x: type(x)==_colorlog.StreamHandler,
                handlers)).index(True)
    return(handlers[i])

def _get_file_handler():
    root = _colorlog.getLogger()
    handlers = root.handlers
    i = list(map(lambda x: type(x)== _RotatingFileHandler,
                handlers)).index(True)
    return(handlers[i])


def console_level(level):
    """ Sets console log level - must be one of 'debug', 'info', 'warning', 'error', 'critical' """
    if not level.lower() in _LEVELS.keys():
        raise ValueError("level must be one of " + ", ".join(_LEVELS.keys()))
    _get_console_handler().setLevel(_LEVELS.get(level))

def file_level(level):
    """ Sets file log level - must be one of 'debug', 'info', 'warning', 'error', 'critical'"""
    if not level.lower() in _LEVELS.keys():
        raise ValueError("level must be one of " + ", ".join(_LEVELS.keys()))
    _get_file_handler().setLevel(_LEVELS.get(level))


def console_on():
    """ Sets console log to level 'info' (default) """
    console_level("info")

def console_off():
    """ Sets console log to level 'critical' - effectively disables it """
    console_level("critical")

def info(msg, log_name = global_log_name):
    """ Logs a message at 'info' level """
    logger = _colorlog.getLogger(log_name)
    logger.info(msg)

def debug(msg, log_name = global_log_name):
    """ Logs a message at 'debug' level """
    logger = _colorlog.getLogger(log_name)
    logger.debug(msg)

def warning(msg, log_name = global_log_name):
    """ Logs a message at 'warning' level """
    logger = _colorlog.getLogger(log_name)
    logger.warning(msg)

def error(msg, log_name = global_log_name):
    """ Logs a message at 'error' level """
    logger = _colorlog.getLogger(log_name)
    logger.error(msg)


def add_log_file(filename, maxBytes=10000000, backupCount=10, level="info"):
    """ Adds a log file to write to.  log/mylog.log is written
     by default.  You can add an additional file by calling this function. """

     # cap each log at 10 MB, with a total of 10 backups (100 MB total)
    root = _colorlog.getLogger()
    fh = _RotatingFileHandler(filename, maxBytes=10000000,
                                      backupCount=10)
    fh_formatter = _logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    fh.setFormatter(fh_formatter)
    root.addHandler(fh)
    if not level.lower() in _LEVELS.keys():
        raise ValueError("level must be one of " + ", ".join(_LEVELS.keys()))
    fh.setLevel(_LEVELS.get(level))
