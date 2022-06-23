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
import json
import time
from paho.mqtt import client as mqtt
from utils import str2bool, randId, readConfig


mqttConf = readConfig('/usr/local/etc/nocconfig/mqtt.conf', 'mqtt')
mqtt_host = mqttConf.get('host')
mqtt_port = int(mqttConf.get('port'))
mqtt_username = mqttConf.get('username')
mqtt_password = mqttConf.get('password')
mqtt_tls = str2bool(mqttConf.get('tls'))
mqtt_clientid = f'{mqttConf.get("clientid")}-{randId(6)}'

mqttTopicTest = 'test/topic'
mqttPayloadTest = '{"message": "hello world!"}'

result = {}


def mqttSendMessage():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            client.isConnected = True
            print("Connected!")
        else:
            print("Bad connection Returned code=", rc)

    mqtt.Client.isConnected = False
    client = mqtt.Client(mqtt_clientid)
    client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.loop_start()
    print(f"Connecting to {mqtt_host}...", )
    client.connect(host=mqtt_host, port=mqtt_port)
    while not client.isConnected:
        time.sleep(1)
    client.publish(mqttTopicTest, mqttPayloadTest)
    client.loop_stop()
    client.disconnect()

    result['message'] = 'message is published'


def main():
    mqttSendMessage()
    print(json.dumps(result))


if __name__ == '__main__':
    main()
