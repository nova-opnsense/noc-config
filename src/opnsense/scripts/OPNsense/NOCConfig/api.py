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

    nocconfig api
'''
import json
import sys
import requests

# define endpoint and credentials
api_key='zEbUWb1MnjVj6ZHIg/NevreMg9oU6JRxo84ZowTXgV6nKpINPSxAQN0vnkftVMb74jvW7zFUWOOaPdUA'
api_secret='W0vVMnqv6HeoZH1Cy38rZCEXx67mZneF7Cc+UyrOQhFIlUHhVkabJosnztubMKMAoNg1O9o3XMs4Jryu'
api_url = 'https://192.168.3.143/api'

def getd(api):

    url = f'{api_url}/{api}'

    # request data
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

def setd(api, data):

    url = f'{api_url}/{api}'
    headers = {'content-type': 'application/json'}

    # request data
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
    args = sys.argv[1:]

    if not args:
        print('usage: [get/set] [api] [data] ')
        sys.exit(1)

    if args[0] == 'get':
        if len(args) < 1:
            print('usage: get <api>')
            sys.exit(1)
        getd(args[1])
    elif args[0] == 'set':
        if len(args) < 2:
            print('usage: set <api> <data>')
            sys.exit(1)
        setd(args[1], args[2])
    else:
        print('command not found')

if __name__ == '__main__':
    main()
