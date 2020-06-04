#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import sys
import time
from webexteamssdk import WebexTeamsAPI
from config import *

"""
Usage:
    Fetches Webex Teams Status and sends MQTT from publisher to subscriber then sleeps every 5 seconds.

Args:
    Found in Config file for ACCESS_TOKEN_ENVIRONMENT_VARIABLE, PORT, SUBSCRIBER_IP
    
Returns:
    Webex Teams Status
    
References:
    Webex API documentation
    For MQTT referenence: http://learnaitech.com/mqtt-introduction-and-example-in-python/ 
"""

#Start of script which cann do MQTT call to establish connection to MQTT subscriber
CONNACK = True
if CONNACK == False:
    raise ValueError (f"Cannot connect to port {CONNACK}")

#This is a function for fetching Webex Status
def status_me():
    api = WebexTeamsAPI (ACCESS_TOKEN_ENVIRONMENT_VARIABLE)
    try:
        while True:
            status = api.people.me().status
            return status
    except KeyboardInterrupt:
        print('Interrupted by keyboard')


#Function for connecting to MQTT and pushing status
def connect_mqtt():
    client = mqtt.Client (client_id='publisher-1')
      # create the client
    client.connect (SUBSCRIBER_IP, PORT) #connect to broker
    client.publish ("webex/status", str(status_me())) #Pushing status as string variable


#Main function which loops and sleeps for 5 seconds
def main():
    while True:
        print(f'Your Current Webex status is: {status_me()}')#Run to show you current result
        try:
            #connect_mqtt() #Uncomment when you setup MQTT variables
            print('Uncomment connect_mqtt() when variables are set')
        except ValueError as e:
            print (e, file=sys.stderr)
        time.sleep (5)


#Call main function
if __name__ == '__main__' :
    main()