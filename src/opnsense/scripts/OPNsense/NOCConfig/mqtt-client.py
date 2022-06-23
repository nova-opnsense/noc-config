#!/usr/local/bin/python3

'''
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
'''

import time
from mqtt import MQTT, clientid


def on_message_topic1(mqttc, obj, msg):
    print(msg.topic+' (1) '+str(msg.qos)+' '+str(msg.payload))


def on_message_topic2(mqttc, obj, msg):
    print(msg.topic+' (2) '+str(msg.qos)+' '+str(msg.payload))


def main():
    mqttc = MQTT(clientid)
    mqttc.message_callback_add('test/topic1', on_message_topic1)
    mqttc.message_callback_add('test/topic2', on_message_topic2)

    mqttc.bootstrap()
    mqttc.subscribe([('test/topic1', 0),
                    ('test/topic2', 0)])

    mqttc.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(f'KeyboardInterrupt')
            break
        except Exception as e:
            print(f'Exception: {e}')
            break

    mqttc.stop()


if __name__ == '__main__':
    main()
