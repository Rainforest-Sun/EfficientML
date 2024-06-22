import time
import busio
import board
from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(board.SCL_1, board.SDA_1)
# pca = PCA9685(i2c)
kit = ServoKit(channels=16, i2c=i2c)
# # kit = ServoKit(channels=16)
kit.servo[0].set_pulse_width_range(500, 2500)

def set_servo_angle(angle):
    kit.servo[0].angle = angle
    time.sleep(0.01)
    
def get_servo_angle():
    return kit.servo[0].angle
