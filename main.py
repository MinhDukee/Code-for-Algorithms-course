# **************************************#
# Load LIBRRARIES
import json
import machine
import network
import time
import urequests as requests

from umqtt.simple import MQTTClient
from uthingsboard.client import TBDeviceMqttClient

import Config
import utils

from bmp180 import BMP180
# **************************************#
#Connect to Network

sta = network.WLAN(network.STA_IF)
connect()
# ***********CLIENT DEVICE****************#
client = TBDeviceMqttClient('thingsboard.cloud', access_token= My_Access_Token) # make a global variable

# **************************************#
# Main Loop

while True:
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL:
        last_update = time.ticks_ms()
        # Connecting to ThingsBoard
        client.connect()
        
        # Sending telemetry
        telemetry = {"temperature": str(bmp.temperature), "altitude": str(bmp.altitude), "pressure": str(bmp.pressure), "Latitude":loc[0], "Longitude":loc[1]}
        try:
            client.send_telemetry(telemetry)
        except ZeroDivisionError:
            print("There has been a error in the BMP180 calculations. Would you like to retry?")
            ans = input("Y or N")
            if a == "Y":
                try:
                    client.send_telemetry(telemetry)
                except ZeroDivisionError:
                    print("System Failed")
                    client.disconnect()
                    print("Disconnecting...")
                    break
            else:
                client.disconnect()
                print("Disconnecting...")
                break
                    
        # Checking for incoming subscriptions or RPC call requests (non-blocking)
        client.check_msg()