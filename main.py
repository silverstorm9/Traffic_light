#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO
import trafficlight
import time
import signal
import sys


def exit(signum, stack):
    # Swith off traffic lights before exiting the program
    traffic_light1.switchOff()
    traffic_light2.switchOff()
    sys.exit(0) # Exit the program


def launchBasicCycle(signum=None, stack=None):
    # Lauch the cycle of traffic lights of a crossroads
    while 1:
        traffic_light1.toRedLight()
        time.sleep(2)
        traffic_light2.toGreenLight()
        time.sleep(10)

        traffic_light2.toRedLight()
        time.sleep(2)
        traffic_light1.toGreenLight()
        time.sleep(10)


def launchBlinkCycle(signum, stack):
    # Blink all traffic light to orange of a crossroads
    while 1:
        traffic_light1.switchOff()
        traffic_light2.switchOff()

        time.sleep(0.5)

        GPIO.output(traffic_light1.orangePin, GPIO.HIGH)
        GPIO.output(traffic_light2.orangePin, GPIO.HIGH)

        time.sleep(0.5)


if __name__ == '__main__':
    # GPIO init
    GPIO.setmode(GPIO.BOARD) # Enable 'board' mode
    GPIO.setwarnings(False) # Disable alert messages

    # Create traffic light objects with theirs pins (in this order : red,orange,green)
    traffic_light1 = trafficlight.TrafficLight(33,35,37)
    traffic_light2 = trafficlight.TrafficLight(36,38,40)

    # Init signal for interruptions
    signal.signal(signal.SIGTERM, exit)                 # To stop the program by using SIGTERM signal :             sudo kill -TERM <pid> 
    signal.signal(signal.SIGUSR1, launchBasicCycle)     # To call back the basic cycle by using SIGUSR1 signal :    sudo kill -USR1 <pid> 
    signal.signal(signal.SIGUSR2, launchBlinkCycle)     # To call the orange blink cycle by using SIGUSR2 signal : sudo kill -USR2 <pid> 

    # Launch the basic cycle by default
    launchBasicCycle()