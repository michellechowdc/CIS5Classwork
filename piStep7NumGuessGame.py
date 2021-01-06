from random import randint
# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# 18 yellow low, 23 green correct, 24 red high
# GPIO.setup(18,GPIO.OUT)
# GPIO.setup(23,GPIO.OUT)
# GPIO.setup(24,GPIO.OUT)

randNum = randint (0, 100)
print("\nA random number from 0-100 has been generated.")
userGuess = int(input ("  Guess the number: "))

while userGuess != 101:
    if userGuess >= 0 and userGuess <= 100:
        if userGuess == randNum:
            print("\nCorrect! The number was %d." %(randNum))
            break
        elif userGuess < randNum:
            print("\nToo low!")
            # GPIO.output(18,GPIO.HIGH)
            # time.sleep(1)
            # GPIO.output(18,GPIO.LOW)
        else:
            print("\nToo high!")
            # GPIO.output(24,GPIO.HIGH)
            # time.sleep(1)
            # GPIO.output(24,GPIO.LOW)
    userGuess = int(input ("\nGuess another number from 0-100\n  (or enter 101 to quit): "))

print("\nThank you for playing!\n")
# GPIO.output(23,GPIO.HIGH)
# time.sleep(1)
# GPIO.output(23,GPIO.LOW)
