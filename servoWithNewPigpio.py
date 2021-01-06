#before running, in terminal do: sudo pigpiod, then pigs t
import RPi.GPIO as GPIO
import sys, tty, termios, time
import pigpio

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO2 = pigpio.pi()

dcMotorIn1 = 3
dcMotorIn2 = 5
dcMotorSig = 7
GPIO.setup(dcMotorIn1, GPIO.OUT)
GPIO.setup(dcMotorIn2, GPIO.OUT)
GPIO.setup(dcMotorSig, GPIO.OUT)
dcMotor = GPIO.PWM(7, 100)
dcMotor.start(0)

servoMotorIn = 10
servoMotorSig = 12
GPIO2.set_mode(servoMotorIn, pigpio.OUTPUT)
GPIO2.set_mode(servoMotorSig, pigpio.OUTPUT)
GPIO2.hardware_PWM(servoMotorSig, 800, 250000) # 800Hz 25% dutycycle
# servoMotor = GPIO.PWM(12, 50)
# servoMotor.start(7.5)
GPIO2.set_servo_pulsewidth(servoMotorSig, 0);


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
    dcMotor.ChangeDutyCycle(35)
    GPIO.output(dcMotorSig, True)
    time.sleep(1)
    GPIO.output(dcMotorSig, False)

def dcMotor_reverse():
    GPIO.output(dcMotorIn1, False)
    GPIO.output(dcMotorIn2, True)
    dcMotor.ChangeDutyCycle(35)
    GPIO.output(dcMotorSig, True)
    time.sleep(1)
    GPIO.output(dcMotorSig, False)

def servoMotor_right():
# figure out servo motor control with pigpio so no twitching
# https://www.raspberrypi.org/forums/viewtopic.php?t=140466
# https://www.raspberrypi.org/forums/viewtopic.php?t=72284
    GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
    GPIO2.set_servo_pulsewidth(servoMotorSig, 2000) # safe clockwise
    GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
    time.sleep(1)
    GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

#############################################
# pi.set_PWM_dutycycle(4,   0) # PWM off
# pi.set_PWM_dutycycle(4,  64) # PWM 1/4 on
# pi.set_PWM_dutycycle(4, 128) # PWM 1/2 on
# pi.set_PWM_dutycycle(4, 192) # PWM 3/4 on
# pi.set_PWM_dutycycle(4, 255) # PWM full on
#
# pi.set_servo_pulsewidth(17, 0)    # off
# pi.set_servo_pulsewidth(17, 1000) # safe anti-clockwise
# pi.set_servo_pulsewidth(17, 1500) # centre
# pi.set_servo_pulsewidth(17, 2000) # safe clockwise
#############################################

def servoMotor_left():
    GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
    GPIO2.set_servo_pulsewidth(servoMotorSig, 1000) # safe anti-clockwise
    GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
    time.sleep(1)
    GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

def toggleSteering(direction):

    global wheelStatus

    if(direction == "right"):
        if(wheelStatus == "centre"):
            servoMotor_right()
            wheelStatus = "right"
        elif(wheelStatus == "left"):
            servoMotor.ChangeDutyCycle(7.5)
            wheelStatus = "centre"

    if(direction == "left"):
        if(wheelStatus == "centre"):
            servoMotor_left()
            wheelStatus = "left"
        elif(wheelStatus == "right"):
            servoMotor.ChangeDutyCycle(7.5)
            wheelStatus = "centre"

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

    # The "a" key will toggle the steering left
    if(keyPressed == "a"):
        toggleSteering("left")

    # The "d" key will toggle the steering right
    if(keyPressed == "d"):
        toggleSteering("right")

    # The "x" key will break the loop and exit the program
    if(keyPressed == "x"):
        print("Program Ended")
        break

    # At the end of each loop the acceleration motor will stop
    # and wait for its next command
    dcMotor.ChangeDutyCycle(0)

    # The keyboard character variable will be set to blank, ready
    # to save the next key that is pressed
    keyPressed = ""

GPIO2.stop()
GPIO.cleanup()
