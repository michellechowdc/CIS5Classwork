import time

import pigpio

pi = pigpio.pi() # Connect to local Pi.

pi.set_servo_pulsewidth(17, 1000)
time.sleep(0.5)
pi.set_servo_pulsewidth(17, 1500)
time.sleep(0.5)
pi.set_servo_pulsewidth(17, 2000)
time.sleep(0.5)
pi.set_servo_pulsewidth(17, 1500)
time.sleep(0.5)
#############################
import time

import pigpio

IN1=8
IN2=25

pigpio.start()

pigpio.set_mode(IN1, pigpio.OUTPUT)
pigpio.set_mode(IN2, pigpio.OUTPUT)

pigpio.write(IN2, 0)
pigpio.write(IN1, 1) #forward

time.sleep(1)

pigpio.write(IN1, 0) # stop

pigpio.write(IN2, 1) # backward

time.sleep(1)

pigpio.write(IN2, 0) # stop

for p in range(256):
   pigpio.set_PWM_dutycycle(IN1, p) # forward with increasing speed
   time.sleep(0.2)

time.sleep(1)

pigpio.write(IN1, 0) #stop

pigpio.stop()
#########################
#!/usr/bin/env python

# PPM_to_servo.py
# 2019-10-09
# Public Domain

import time
import pigpio # http://abyz.me.uk/rpi/pigpio/python.html

IN_GPIO=4 # the PPM input GPIO
OUT_GPIO=[5, 6, 7, 8, 9, 10, 11, 12] # The servo output GPIO

start_of_frame = False
channel = 0
last_tick = None

def cbf(gpio, level, tick):
   global start_of_frame, channel, last_tick
   if last_tick is not None:
      diff = pigpio.tickDiff(last_tick, tick)
      if diff > 3000: # start of frame
         start_of_frame = True
         channel = 0
      else:
         if start_of_frame:
            if channel < len(OUT_GPIO):
               pi.set_servo_pulsewidth(OUT_GPIO[channel], diff)
               channel += 1
   last_tick = tick

pi = pigpio.pi()
if not pi.connected:
   exit()

pi.set_mode(IN_GPIO, pigpio.INPUT)

cb = pi.callback(IN_GPIO, pigpio.RISING_EDGE, cbf)

time.sleep(60)

cb.cancel()

pi.stop()
#########################################

# switch servo off
pi.set_servo_pulsewidth(17, 0);

pi.stop()


import RPi.GPIO as GPIO
import sys, tty, termios, time

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

servoMotorIn = 10
servoMotorSig = 12
GPIO.setup(servoMotorIn, GPIO.OUT)
GPIO.setup(servoMotorSig, GPIO.OUT)
servoMotor = GPIO.PWM(10, 100)
servoMotor.start(0)
servoMotor.ChangeDutyCycle(0)
# setAngle(0)
##########SET START TO 0 HERE

# getch is to determine which key pressed, then return key as variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# declares which way motors spin accordingly
def dcMotor_forward():
    GPIO.output(dcMotorIn1, True)
    GPIO.output(dcMotorIn2, False)
    dcMotor.ChangeDutyCycle(50)
    GPIO.output(dcMotorSig, True)

def dcMotor_reverse():
    GPIO.output(dcMotorIn1, False)
    GPIO.output(dcMotorIn2, True)
    dcMotor.ChangeDutyCycle(25)
    GPIO.output(dcMotorSig, True)

def servoMotor_right():
    angle = 175
    duty = angle / 18 + 2
    GPIO.output(servoMotorIn, True)
    servoMotor.ChangeDutyCycle(duty)
    GPIO.output(servoMotorSig, True)
    # sleep(1)
    # GPIO.output(servoMotorSig, False)
    # servoMotor.ChangeDutyCycle(0)

def servoMotor_left():
    angle = 45
    duty = angle / 18 + 2
    GPIO.output(servoMotorIn, True)
    servoMotor.ChangeDutyCycle(duty)
    GPIO.output(servoMotorSig, True)
    # sleep(1)
    # GPIO.output(servoMotorSig, False)
    # servoMotor.ChangeDutyCycle(0)

# toggle steering
def toggleSteering(direction):

    global wheelStatus

    if(direction == "right"):
        if(wheelStatus == "centre"):
            servoMotor_right()
            wheelStatus = "right"
        elif(wheelStatus == "left"):
            servoMotor_right()
            wheelStatus = "right"
        elif(wheelStatus =="right"):
            servoMotor.ChangeDutyCycle(0)
            wheelStatus = "right"

    if(direction == "left"):
        if(wheelStatus == "centre"):
            servoMotor_left()
            wheelStatus = "left"
        elif(wheelStatus == "right"):
            servoMotor_left()
            wheelStatus = "left"
        elif(wheelStatus =="left"):
            servoMotor.ChangeDutyCycle(0)
            wheelStatus = "left"

# all motors don't move when starting
GPIO.output(dcMotorIn1, False)
GPIO.output(dcMotorIn2, False)
GPIO.output(servoMotorIn, False)

# assign global variable
wheelStatus = "centre"

# loop to get keyboard data and run motors
while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    keyPressed = getch()

    if(keyPressed == "w"):
        dcMotor_forward()

    if(keyPressed == "s"):
        dcMotor_reverse()

    if(keyPressed == "a"):
        toggleSteering("left")

    if(keyPressed == "d"):
        toggleSteering("right")

    if(keyPressed == "x"):
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    dcMotor.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    keyPressed = ""

GPIO.cleanup()

#############################################
# def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(servoMotorIn, True)
    GPIO.output(servoMotorSig, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)

    GPIO.output(servoMotorSig, False)
    pwm.ChangeDutyCycle(0)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                #setAngle(45)
                GPIO.output(dcMotorIn1,GPIO.HIGH)
                GPIO.output(dcMotorIn2,GPIO.LOW)
                pwm.ChangeDutyCycle(25)
                GPIO.output(dcMotorSig,GPIO.HIGH)
                setAngle(45)
                #GPIO.output(servoMotor, GPIO.HIGH)
                #pwm.ChangeDutyCycle(4.5)
                #GPIO.output(servoMotor, False)
                #pwm.ChangeDutyCycle(0)
            elif char == curses.KEY_DOWN:
                setAngle(45)
                GPIO.output(dcMotorIn1,GPIO.LOW)
                GPIO.output(dcMotorIn2,GPIO.HIGH)
                pwm.ChangeDutyCycle(25)
                GPIO.output(dcMotorSig,GPIO.HIGH)
                #GPIO.output(motor2a,GPIO.LOW)
                #GPIO.output(motor2b,GPIO.HIGH)
                #GPIO.output(motor2e,GPIO.HIGH)
            elif char == curses.KEY_RIGHT:
                setAngle(175)
                GPIO.output(dcMotorIn1,GPIO.HIGH)
                GPIO.output(dcMotorIn2,GPIO.LOW)
                pwm.ChangeDutyCycle(25)
                GPIO.output(dcMotorSig,GPIO.HIGH)
                #GPIO.output(motor2a,GPIO.LOW)
                #GPIO.output(motor2b,GPIO.HIGH)
                #GPIO.output(motor2e,GPIO.HIGH)
            elif char == curses.KEY_LEFT:
                setAngle(310)
                GPIO.output(dcMotorIn1,GPIO.HIGH)
                GPIO.output(dcMotorIn2,GPIO.LOW)
                pwm.ChangeDutyCycle(25)
                GPIO.output(dcMotorSig,GPIO.HIGH)
                #GPIO.output(motor2a,GPIO.HIGH)
                #GPIO.output(motor2b,GPIO.LOW)
                #GPIO.output(motor2e,GPIO.HIGH)
            elif char == 10:
                GPIO.output(dcMotorIn1,GPIO.LOW)
                GPIO.output(dcMotorIn2,GPIO.LOW)
                pwm.ChangeDutyCycle(25)
                GPIO.output(dcMotorSig,GPIO.LOW)
                setAngle(45)
                #GPIO.output(motor2a,GPIO.LOW)
                #GPIO.output(motor2b,GPIO.LOW)
                #GPIO.output(motor2e,GPIO.LOW)

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
