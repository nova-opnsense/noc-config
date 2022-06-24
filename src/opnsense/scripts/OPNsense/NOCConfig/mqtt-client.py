#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>

    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
    
"""

import json
import time
from mqtt import MQTT, clientid
from api import get, post
from datetime import datetime
from utils import log, tryParseJson


def on_message_hub_status(mqttc, obj, msg):
    """
    /* payload example */
    {
        "id": "hub_407b2187-8233-4037-a2d9-8d85ed2727d1",
        "name": "HUB",
        "status": 3,
        "software_info": {
            "version": "",
            "commit": "786da52c65bf614087ffdeebc41fcfa6f9360ecc",
            "build_date": ""
        },
        "hardware_info": {
            "protocol.ble": true,
            "protocol.zib": true,
            "protocol.zwa": true
        }
    }
    """

    log.debug("[MQTT] %s (%d): \n%s",
              msg.topic, msg.qos,
              tryParseJson(msg.payload))

    try:
        hub = json.loads(msg.payload)
        segmentData = {
            "segment": {
                "enabled": "1",
                "hubId": hub["id"],
                "name": hub["name"],
                "lastUpdate": datetime.now().isoformat(),
                "status": hub["status"],
            }
        }

        # search for existing item
        res = post("nocconfig/segment/searchItem",
                   "current=1&rowCount=1&searchPhrase=%s" % hub["id"],
                   "application/x-www-form-urlencoded")

        if res.status_code != 200:
            log.error(f"[MQTT] unable to search item. status_code: {res}")
            return

        result = json.loads(res.text)

        if result["total"] > 0 and len(result["rows"]) > 0:
            # update exist item
            uuid = result["rows"][0]["uuid"]
            log.debug(f"[MQTT] update exist item {uuid}")
            res = post("nocconfig/segment/setItem/%s" % uuid,
                       json.dumps(segmentData),
                       "application/json")
        else:
            # add new item
            log.debug("[MQTT] add new item")
            res = post("nocconfig/segment/addItem",
                       json.dumps(segmentData),
                       "application/json")

    except Exception as e:
        log.error("[MQTT] Exception: %s", e)


def main():
    mqttc = MQTT(clientid)
    mqttc.message_callback_add("hub/status/#", on_message_hub_status)

    mqttc.bootstrap()
    mqttc.subscribe([
        # ("test/#", 0),
        ("hub/status/#", 0)
    ])

    mqttc.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            log.debug("[MQTT] Ctrl-C")
            break
        except Exception as e:
            log.error("[MQTT] Exception: %s", e)
            break

    mqttc.stop()


if __name__ == "__main__":
    main()
