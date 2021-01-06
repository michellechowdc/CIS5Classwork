#before running, in terminal do: sudo pigpiod, then pigs t
import time
import pigpio

GPIO2 = pigpio.pi()

servoMotorIn = 10
servoMotorSig = 12
GPIO2.set_mode(servoMotorIn, pigpio.OUTPUT)
GPIO2.set_mode(servoMotorSig, pigpio.OUTPUT)
GPIO2.hardware_PWM(servoMotorSig, 800, 250000) # 800Hz 25% dutycycle
GPIO2.set_servo_pulsewidth(servoMotorSig, 0);

def servoMotor_right():
    GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
    GPIO2.set_servo_pulsewidth(servoMotorSig, 2000) # safe clockwise
    GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
    time.sleep(1)
    GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

def servoMotor_left():
    GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
    GPIO2.set_servo_pulsewidth(servoMotorSig, 1000) # safe anti-clockwise
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

servoMotor_right()
time.sleep(3)
servoMotor_left()
time.sleep(3)


GPIO2.stop()

#############################################
#############################################
#before running, in terminal do: sudo pigpiod, then pigs t
import time
import pigpio

GPIO2 = pigpio.pi()

servoMotorIn = 10
servoMotorSig = 12
GPIO2.set_mode(servoMotorIn, pigpio.OUTPUT)
GPIO2.set_mode(servoMotorSig, pigpio.OUTPUT)
GPIO2.hardware_PWM(servoMotorSig, 800, 250000) # 800Hz 25% dutycycle
GPIO2.set_servo_pulsewidth(servoMotorSig, 0);


GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
GPIO2.set_servo_pulsewidth(servoMotorSig, 2000) # safe clockwise
GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
time.sleep(5)
GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

# def servoMotor_left():
#     GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
#     GPIO2.set_servo_pulsewidth(servoMotorSig, 1000) # safe anti-clockwise
#     GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
#     time.sleep(1)
#     GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

GPIO2.stop()

#############################################
#############################################
import time
import pigpio

GPIO2 = pigpio.pi()

servoMotorIn = 16
servoMotorSig = 18
#GPIO2.set_mode(servoMotorIn, pigpio.OUTPUT)
#GPIO2.set_mode(servoMotorSig, pigpio.OUTPUT)
#GPIO2.hardware_PWM(servoMotorSig, 1000, 500000) # 800Hz 25% dutycycle
#GPIO2.set_servo_pulsewidth(servoMotorIn, 0);


#GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
GPIO2.set_servo_pulsewidth(servoMotorSig, 1000)
time.sleep(1.5)
GPIO2.set_servo_pulsewidth(servoMotorSig, 1500)
time.sleep(1.5)
GPIO2.set_servo_pulsewidth(servoMotorSig, 2000) # safe clockwise
time.sleep(1.5)

# def servoMotor_left():
#     GPIO2.set_PWM_dutycycle(servoMotorIn, 192) # PWM 3/4 on
#     GPIO2.set_servo_pulsewidth(servoMotorSig, 1000) # safe anti-clockwise
#     GPIO2.set_PWM_dutycycle(servoMotorSig, 192) # PWM 3/4 on
#     time.sleep(1)
#     GPIO2.set_PWM_dutycycle(servoMotorSig, 0) # off

GPIO2.set_servo_pulsewidth(servoMotorSig, 0)
GPIO2.stop()
