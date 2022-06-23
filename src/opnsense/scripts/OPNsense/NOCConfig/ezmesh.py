#!/usr/local/bin/python3

'''
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
'''

import json
from utils import readConfig


ezmConf = readConfig('/usr/local/etc/nocconfig/ezmesh.conf', 'ezmesh')
ezm_ssid = ezmConf.get('ssid')
ezm_pass = ezmConf.get('password')


result = {}


def main():
    result['message'] = 'Hello, world! I am here. 💕💖💖💖💕'
    result['ssid'] = ezm_ssid
    result['password'] = ezm_pass

    print(json.dumps(result))


if __name__ == '__main__':
    main()
