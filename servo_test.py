# alias sudo='sudo env PATH=$PATH:/home/your_username/miniforge3/envs/servo/bin'

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

while True:
    print("111")
    for i in range(0,180,1):
        kit.servo[0].angle = i
        # kit.servo[1].angle = i
        time.sleep(0.01) 
 
    for i in range(180,0,-1):
        kit.servo[0].angle = i
        # kit.servo[1].angle = i
        time.sleep(0.01)