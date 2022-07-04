#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    utility functions helper
    
"""

import os
import random
import string
import json
from configparser import ConfigParser
import logging as log
import coloredlogs

# log = logging.getLogger()

log.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=log.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S")

# coloredlogs.install(level="DEBUG", logger=log,
#                     fmt="%(asctime)s.%(msecs)03d %(hostname)s %(name)s[%(process)d] %(levelname)7s %(message)s")


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


def tryParseJson(str):
    try:  # json
        return json.dumps(json.loads(str), indent=4)
    except:  # text
        return str
