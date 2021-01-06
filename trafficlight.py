import RPi.GPIO as GPIO
import time

class TrafficLight():
    """ This class permits the manipulation of a traffic light or two opposite traffic lights """

    def __init__(self, redPin, orangePin, greenPin):
        # Set GPIOs pin number for each LEDs
        self.redPin = redPin
        self.orangePin = orangePin
        self.greenPin = greenPin

        # Enable GPIOs control as outputs
        GPIO.setup(redPin, GPIO.OUT)
        GPIO.setup(orangePin, GPIO.OUT)
        GPIO.setup(greenPin, GPIO.OUT)

        GPIO.output(self.orangePin, GPIO.HIGH) # By default, switch the orange light on


    def toGreenLight(self):
        # The traffic light turns green
        self.switchOff()
        GPIO.output(self.greenPin, GPIO.HIGH)


    def toOrangeBlink(self, timeOrangeOn=0.5):
        # The traffic light flashes orange for 0.5s by default
        self.switchOff()
        GPIO.output(self.orangePin, GPIO.HIGH)
        time.sleep(timeOrangeOn)
        GPIO.output(self.orangePin, GPIO.LOW)


    def toRedLight(self, timeOrangeOn=2):
        # The traffic light turns red
        self.switchOff()
        self.toOrangeBlink(timeOrangeOn)
        GPIO.output(self.orangePin, GPIO.LOW)
        GPIO.output(self.redPin, GPIO.HIGH)


    def switchOff(self):
        # THe traffic light goes out
        GPIO.output(self.redPin, GPIO.LOW)
        GPIO.output(self.orangePin, GPIO.LOW)
        GPIO.output(self.greenPin, GPIO.LOW)