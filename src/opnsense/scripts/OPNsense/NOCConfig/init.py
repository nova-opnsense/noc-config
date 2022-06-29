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
        src_logo = os.path.join(dir, "default-logo.svg")
        src_favicon = os.path.join(dir, "favicon.png")
        src_default = os.path.join(dir, "default.volt")

        dst_logo = "/usr/local/opnsense/www/themes/opnsense/build/images/default-logo.svg"
        dst_favicon = "/usr/local/opnsense/www/themes/opnsense/build/images/favicon.png"
        dst_default = "/usr/local/opnsense/mvc/app/views/layouts/default.volt"

        result = {}
        result["pwd"] = os.getcwd()

        result[src_logo] = os.path.exists(src_logo)
        result[dst_logo] = os.path.exists(dst_logo)
        result[src_favicon] = os.path.exists(src_favicon)
        result[dst_favicon] = os.path.exists(dst_favicon)
        result[src_default] = os.path.exists(src_default)
        result[dst_default] = os.path.exists(dst_default)

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
