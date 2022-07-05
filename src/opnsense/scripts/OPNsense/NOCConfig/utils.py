#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    utility functions helper
    
"""

import os
import re
import sys
import random
import string
import json
from configparser import ConfigParser
import logging
from logging import handlers
import platform


LOGFILE = "/var/log/noc.log"
FORMAT = "%(asctime)s.%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)7s %(message)s"


class HostnameFilter(logging.Filter):
    hostname = platform.node()

    def filter(self, record):
        record.hostname = HostnameFilter.hostname
        return True


log = logging.getLogger("")
log.setLevel(logging.DEBUG)
format = logging.Formatter(
    fmt=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S")


ch = logging.StreamHandler(sys.stdout)
ch.addFilter(HostnameFilter())
ch.setFormatter(format)
log.addHandler(ch)

fh = handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*5), backupCount=7)
fh.addFilter(HostnameFilter())
fh.setFormatter(format)
log.addHandler(fh)

# log.basicConfig(
#     format="%(asctime)s %(levelname)-8s %(message)s",
#     level=log.DEBUG,
#     datefmt="%Y-%m-%d %H:%M:%S")


def str2bool(str):
    return str.lower() in ["true", "1", "t", "y", "yes"]


def randId(n: int):
    return "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def readConfig(config_file, section):
    if os.path.exists(config_file):
        cnf = ConfigParser()
        cnf.read(config_file)
        if cnf.has_section(section):
            try:
                return dict(cnf.items(section))
            except Exception:
                return None
        else:
            # empty config
            return None
    else:
        # no config
        return None


def tryParseJson(obj):
    try:  # json
        if isinstance(obj, str):
            return json.dumps(json.loads(obj), indent=4)
        else:
            return json.dumps(obj, indent=4)
    except:  # text
        return obj


def fmtNova():
    return '''

    ███╗░░██╗░█████╗░██╗░░░██╗░█████╗░
    ████╗░██║██╔══██╗██║░░░██║██╔══██╗
    ██╔██╗██║██║░░██║╚██╗░██╔╝███████║
    ██║╚████║██║░░██║░╚████╔╝░██╔══██║
    ██║░╚███║╚█████╔╝░░╚██╔╝░░██║░░██║
    ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝

    '''
