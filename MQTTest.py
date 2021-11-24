#!/usr/bin/env python3

import sys
import paho.mqtt.client as mqtt

if __name__ == "__main__":

    mode = sys.argv[1]
    print(mode)

    client = mqtt.Client()

    client.connect("192.168.1.20", 1883, 60)

    if mode == "off":
        client.publish("zigbee2mqtt/LampeCave1/set", b'{"state":"OFF"}')
    if mode == "on":
        client.publish("zigbee2mqtt/LampeCave1/set", b'{"state":"ON"}')
    if mode == "soir":
        client.publish("zigbee2mqtt/LampeCave1/set", b'{"brightness":2,"color_temp":500}')
    if mode == "jour":
        client.publish("zigbee2mqtt/LampeCave1/set", b'{"brightness":254,"color_temp":150}')
    if mode == "nuit":
        client.publish("zigbee2mqtt/LampeCave1/set", b'{"color":{"x":0.14912280701754385,"y":0.06140350877192982},"brightness":254}')