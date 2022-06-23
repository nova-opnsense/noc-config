#!/usr/local/bin/python3

'''
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>

    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
'''

import argparse
import time
from mqtt import MQTT, clientid


def main():

    parser = argparse.ArgumentParser(
        description='NOC mqtt client publish helper')

    parser.add_argument('-t', '--topic',
                        type=str,
                        required=True,
                        help='topic name')
    parser.add_argument('-p', '--payload',
                        type=str,
                        required=True,
                        help='payload data')

    args = parser.parse_args()

    topic = args.topic
    payload = args.payload

    mqttc = MQTT(clientid)

    mqttc.bootstrap()

    mqttc.start()

    while not mqttc.isConnected:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(f'KeyboardInterrupt')
            break
        except Exception as e:
            print(f'Exception: {e}')
            break

    rc = mqttc.publish(topic, payload)

    # time.sleep(10)
    mqttc.stop()


if __name__ == '__main__':
    main()
