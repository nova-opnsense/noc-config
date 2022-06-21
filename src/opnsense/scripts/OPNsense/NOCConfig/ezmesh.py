#!/usr/local/bin/python3

"""
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

    perform some tests for the nocconfig application
"""
import os
import json
from configparser import ConfigParser

ezmesh_config = '/usr/local/etc/nocconfig/ezmesh.conf'

result = {}
if os.path.exists(ezmesh_config):
    cnf = ConfigParser()
    cnf.read(ezmesh_config)
    if cnf.has_section('ezmesh'):
        try:
            ezmSSID = cnf.get('ezmesh', 'SSID')
            ezmPassword = cnf.get('ezmesh', 'Password')

            result['message'] = f'EzMesh ok! SSID={ezmSSID}, password={ezmPassword}'
            result['SSID'] = ezmSSID
            result['Password'] = ezmPassword

        except Exception as error:
            result['message'] = 'Err[0]: %s' % error
    else:
        # empty config
        result['message'] = 'Err[1]: empty configuration'
else:
    # no config
    result['message'] = 'Err[2]: no configuration file found'


print(json.dumps(result))
