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
        dir = "/usr/local/opnsense/service/templates/OPNsense/NOCConfig/"
        file_logo = os.path.join(dir, "default-logo.svg")
        file_favicon = os.path.join(dir, "favicon.png")
        file_default = os.path.join(dir, "default.volt")

        result = {}
        result["pwd"] = os.getcwd()

        if os.path.exists(file_logo):
            result[file_logo] = "file_logo already exists. "
        else:
            result[file_logo] = "file_logo not found. "

        if os.path.exists(file_favicon):
            result[file_favicon] = "file_favicon already exists. "
        else:
            result[file_favicon] = "file_favicon not found. "

        if os.path.exists(file_default):
            result[file_default] = "file_default already exists. "
        else:
            result[file_default] = "file_default not found. "

        result["message"] = "Ok! 💖. "
        return result
    except Exception as e:
        return {
            "message": e,
        }


def main():
    print(json.dumps(copyFiles(), indent=4))


if __name__ == "__main__":
    main()
