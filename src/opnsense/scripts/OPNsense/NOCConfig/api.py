#!/usr/local/bin/python3

'''
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    opnsense api helper
'''

import json
import requests
import argparse
from utils import readConfig

conf = readConfig('/usr/local/etc/nocconfig/api.conf', 'api')

api_key = conf.get('key')
api_secret = conf.get('secret')
api_endpoint = conf.get('endpoint')


def get(api):

    url = f'{api_endpoint}/{api}'

    r = requests.get(url,
                     verify=False,
                     auth=(api_key, api_secret))

    print(f'result: {r}')

    if r.status_code == 200:
        print('Receive status OK')
        response = json.loads(r.text)
        print(f'response: {json.dumps(response)}')
    else:
        print('Connection / Authentication issue, response received:')
        print(r.text)


def post(api, data, contentType):

    url = f'{api_endpoint}/{api}'
    headers = {'content-type': contentType}

    r = requests.post(url,
                      verify=False,
                      data=data,
                      headers=headers,
                      auth=(api_key, api_secret))

    if r.status_code == 200:
        print('Receive status OK')
        response = json.loads(r.text)
        print(f'response: {json.dumps(response)}')
    else:
        print('Connection / Authentication issue, response received:')
        print(r.text)


def main():

    parser = argparse.ArgumentParser(description='OPNsense API client helper')

    parser.add_argument('-m', '--method',
                        type=str,
                        default='GET',
                        help='method `GET`/`POST`, default is `GET`')
    parser.add_argument('-a', '--api',
                        type=str,
                        required=True,
                        help='API url. for example: `nocconfig/ezmesh/get`')
    parser.add_argument('-d', '--data',
                        type=str,
                        help='data')
    parser.add_argument('-t', '--contentType',
                        type=str,
                        default='application/json',
                        help='header content-type: application/json, application/x-www-form-urlencoded, text/plain, text/html')

    args = parser.parse_args()

    method = args.method.upper()
    api = args.api
    data = args.data
    contentType = args.contentType

    if method == 'GET':
        get(api)
    elif method == 'POST':
        post(api, data, contentType)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
