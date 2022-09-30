#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the noc application
    
"""

import json
from utils import readConfig


def getEzmeshConf():
    try:
        ezmConf = readConfig("/usr/local/etc/noc/ezmesh.conf", "ezmesh")
        ezm_ssid = ezmConf.get("ssid")
        ezm_pass = ezmConf.get("password")
        return {
            "message": "Hello, world! I am here. 💕💖💖💖💕",
            "ssid": ezm_ssid,
            "password": ezm_pass
        }
    except Exception as e:
        return {
            "message": e,
        }


def main():
    print(json.dumps(getEzmeshConf()))


if __name__ == "__main__":
    main()
