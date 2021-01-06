import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

dcMotorIn1 = 3
dcMotorIn2 = 5
dcMotorSig = 7
GPIO.setup(dcMotorIn1, GPIO.OUT)
GPIO.setup(dcMotorIn2, GPIO.OUT)
GPIO.setup(dcMotorSig, GPIO.OUT)
dcMotor = GPIO.PWM(3, 100)
dcMotor.start(0)
dcMotor.ChangeDutyCycle(0)

def dcMotor_forward():
    GPIO.output(dcMotorIn1, True)
    GPIO.output(dcMotorIn2, False)
    dcMotor.ChangeDutyCycle(25)
    GPIO.output(dcMotorSig, True)

def dcMotor_reverse():
    GPIO.output(dcMotorIn1, False)
    GPIO.output(dcMotorIn2, True)
    dcMotor.ChangeDutyCycle(25)
    GPIO.output(dcMotorSig, True)

dcMotor_forward()
sleep(5)
# GPIO.output(dcMotorSig, False)
dcMotor_reverse()
sleep(5)
# GPIO.output(dcMotorSig, False)

dcMotor.stop()
GPIO.cleanup()

#############################################
#https://www.instructables.com/id/DC-Motor-Control-With-Raspberry-Pi-and-L293D/
#REMEMBER TO TURN ON POWER SOURCE

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
pwm=GPIO.PWM(7, 100)

pwm.start(0)

#to spin forwards, one output is T and other F
GPIO.output(3, True)
GPIO.output(5, False)
#to spin at 25% power
pwm.ChangeDutyCycle(25)
GPIO.output(7, True)
sleep(5)
GPIO.output(7, False)

#to spin other direction, swap T & F
GPIO.output(3, False)
GPIO.output(5, True)
pwm.ChangeDutyCycle(25)
GPIO.output(7, True)
sleep(5)
GPIO.output(7, False)

pwm.stop()
GPIO.cleanup()
