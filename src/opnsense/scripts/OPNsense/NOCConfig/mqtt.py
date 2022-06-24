#!/usr/local/bin/python3

"""
    Copyright (c) 2021-2022 Nova Intelligent Technology JSC.,
    Author: hai.nt <hai.nt@novaintechs.com>
    
    All rights reserved.

    --------------------------------------------------------------------------------------

    perform some tests for the nocconfig application
    
"""

import paho.mqtt.client as mqtt
from utils import str2bool, randId, readConfig, log


mqttConf = readConfig("/usr/local/etc/nocconfig/mqtt.conf", "mqtt")
mqtt_host = mqttConf.get("host")
mqtt_port = int(mqttConf.get("port"))
mqtt_username = mqttConf.get("username")
mqtt_password = mqttConf.get("password")
mqtt_tls = str2bool(mqttConf.get("tls"))

clientid = f"{mqttConf.get('clientid')}-{randId(6)}"


class MQTT(mqtt.Client):

    def __init__(self, *args, **kwargs):
        super(MQTT, self).__init__(*args, **kwargs)
        self.isConnected = False
        self.id = self._client_id.decode("utf-8")

    def on_connect(self, mqttc, obj, flags, rc):
        log.debug(f"[MQTT] [{self.id}] Connected: {rc}")
        if rc == 0:
            self.isConnected = True

    def on_disconnect(self, mqttc, obj, rc):
        log.debug(f"[MQTT] [{self.id}] Disconnected: {rc}")

    def on_connect_fail(self, mqttc, obj):
        log.debug(f"[MQTT] [{self.id}] Connection failed.")

    def on_message(self, mqttc, obj, msg):
        log.debug(
            f"[MQTT] [{self.id}] Message received: {msg.topic} {msg.qos} {msg.payload}")

    def on_publish(self, mqttc, obj, mid):
        log.debug(f"[MQTT] [{self.id}] Published: {mid}")

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        log.debug(f"[MQTT] [{self.id}] Subscribed: {mid} {granted_qos}")

    def on_log(self, mqttc, obj, level, string):
        log.debug(f"[MQTT] [{self.id}] {string}")

    def bootstrap(self):
        self.username_pw_set(mqtt_username, mqtt_password)
        self.connect(mqtt_host, mqtt_port, 60)
        log.debug(f"[MQTT] [{self.id}] Connecting to {mqtt_host}...", )

    def start(self):
        log.debug(f"[MQTT] [{self.id}] Starting...")
        self.loop_start()

    def stop(self):
        log.debug(f"[MQTT] [{self.id}] Stopped")
        self.disconnect()
        self.loop_stop()
