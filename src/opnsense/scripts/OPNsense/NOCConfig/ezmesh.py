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

    perform some tests for the nocconfig application
'''
import os
import json
import sys
import time
from configparser import ConfigParser
from paho.mqtt import client as mqtt


result = {}
ezmSSID = ''
ezmPassword = ''

# get ezmesh configurations
ezmesh_config = '/usr/local/etc/nocconfig/ezmesh.conf'
if os.path.exists(ezmesh_config):
    cnf = ConfigParser()
    cnf.read(ezmesh_config)
    if cnf.has_section('ezmesh'):
        try:
            ezmSSID = cnf.get('ezmesh', 'SSID')
            ezmPassword = cnf.get('ezmesh', 'Password')

            result['SSID'] = ezmSSID
            result['Password'] = ezmPassword

        except Exception as error:
            result['message'] = 'Err[0]: %s' % error
            sys.exit()
    else:
        # empty config
        result['message'] = 'Err[1]: empty configuration'
        sys.exit()
else:
    # no config
    result['message'] = 'Err[2]: no configuration file found'
    sys.exit()


print(json.dumps(result))


mqttHost = ''
mqttPort = 1883
mqttUsername = ''
mqttPassword = ''
mqttTls = ''
mqttClientId = 'nova_mqtt_client'
mqttTopic = 'test/topic'

# get mqtt configurations
mqtt_config = '/usr/local/etc/nocconfig/mqtt.conf'
if os.path.exists(mqtt_config):
    cnf = ConfigParser()
    cnf.read(mqtt_config)
    if cnf.has_section('mqtt'):
        try:
            mqttHost = cnf.get('mqtt', 'host')
            # mqttPort = cnf.get('mqtt', 'port')
            mqttUsername = cnf.get('mqtt', 'username')
            mqttPassword = cnf.get('mqtt', 'password')
            mqttTls = cnf.get('mqtt', 'tls')

        except Exception as error:
            result['message'] = 'Err[0]: %s' % error
            sys.exit()
    else:
        # empty config
        result['message'] = 'Err[1]: empty configuration'
        sys.exit()
else:
    # no config
    result['message'] = 'Err[2]: no configuration file found'
    sys.exit()


print(f'mqttHost = {mqttHost}')
print(f'mqttPort = {mqttPort}')
print(f'mqttUsername = {mqttUsername}')
print(f'mqttPassword = {mqttPassword}')


# connect to mqtt broker
# def on_connect(client, userdata, flags, rc):
#     if rc == 0:
#         print('Connected to MQTT Broker!')
#         msg = '{"hello": "world"}'
#         re = client.publish(mqttTopic, msg)
#         print(f'Published to {mqttTopic}, return code {re}')
#         sys.exit()
#     else:
#         print('Failed to connect, return code %d\n', rc)
#         sys.exit()



# client = mqtt_client.Client(mqttClientId)
# client.username_pw_set(mqttUsername, mqttPassword)
# client.on_connect = on_connect
# client.connect(mqttHost, mqttPort)
# client.loop_start()


def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False#create flag in class
broker="127.0.0.1"
client = mqtt.Client("python1")             #create new instance 
client.username_pw_set('noc', 'Nova@2021')
client.on_connect=on_connect  #bind call back function
client.loop_start()
print("Connecting to broker ",broker)
client.connect(broker)      #connect to broker
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
client.publish("test/topic","hehe")
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect


# while(True):
#     time.sleep(1)
