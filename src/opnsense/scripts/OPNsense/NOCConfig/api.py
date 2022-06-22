#!/usr/local/bin/python3

'''
    Copyright (c) 2015-2019 Ad Schellevis <ad@opnsense.org>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
    INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.

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
api_type = conf.get('type')


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


def set(api, data):

    url = f'{api_endpoint}/{api}'
    headers = {'content-type': api_type}

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
                        default='get',
                        help='method is `GET` or `SET`, default is `GET`')
    parser.add_argument('-a', '--api',
                        type=str,
                        default='',
                        help='the API url. for example: `nocconfig/ezmesh/get`')
    parser.add_argument('-d', '--data',
                        type=str,
                        default='',
                        help='json data for `set` method')

    args = parser.parse_args()

    method = args.method.upper()
    api = args.api
    data = args.data

    if method == 'GET':
        get(api)
    elif method == 'SET':
        set(api, data)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
