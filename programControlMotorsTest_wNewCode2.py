# issues: servo spazzes and moves to other angles when DC going
# DC stops when press to go L/R
# DC one direction spins faster than other: set faster to forward
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
dcMotor = GPIO.PWM(7, 100)
dcMotor.start(0)
#dcMotor.ChangeDutyCycle(0)

servoMotorIn = 10
servoMotorSig = 12
GPIO.setup(servoMotorIn, GPIO.OUT)
GPIO.setup(servoMotorSig, GPIO.OUT)
servoMotor = GPIO.PWM(12, 50)
servoMotor.start(7.5)
#servoMotor.ChangeDutyCycle(7.5)

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
    GPIO.output(servoMotorIn, True)
    servoMotor.ChangeDutyCycle(2.5)
    GPIO.output(servoMotorSig, True)
    # sleep(1)
    # GPIO.output(servoMotorSig, False)
    # servoMotor.ChangeDutyCycle(0)

def servoMotor_left():
    GPIO.output(servoMotorIn, True)
    servoMotor.ChangeDutyCycle(12.5)
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

GPIO.cleanup()
