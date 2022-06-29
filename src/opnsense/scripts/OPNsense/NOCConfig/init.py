#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
    
"""

import json
import os
from utils import readConfig


def copyFiles():
    try:
        dir = "../../../service/templates/OPNsense/NOCConfig/"
        file_logo = os.path.join(dir, "default-logo.svg")
        file_favicon = os.path.join(dir, "favicon.png")
        file_default = os.path.join(dir, "default.volt")

        msg = ""
        if os.path.exists(file_logo):
            msg += "file_logo already exists. "
        if os.path.exists(file_favicon):
            msg += "file_favicon already exists. "
        if os.path.exists(file_default):
            msg += "file_default already exists. "

        return {
            "message": "Ok! 💖. " + msg,
        }
    except Exception as e:
        return {
            "message": e,
        }


def main():
    print(json.dumps(copyFiles()))


if __name__ == "__main__":
    main()
