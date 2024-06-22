import cv2
import numpy as np
import torch
import time

from utils.datasets import LoadStreams
from siamfc import TrackerSiamFC
from utils.servo import set_servo_angle, get_servo_angle


def move_motor(x_center, y_center):
    # Move the motor to the center of the detected object
    # x_center, y_center: center of the detected object
    print(f'Move the motor to ({x_center}, {y_center})')
    # Set the angle of the servo motor
    # angle = get_servo_angle()
    # if x_center > 440:
    #     angle -= 5
    # elif x_center < 200:
    #     angle += 5
    # # angle = 90 - (x_center - 320) * 90 / 320
    # if angle < 0:
    #     angle = 0
    # elif angle > 180:
    #     angle = 180

    angle = get_servo_angle()
    # angle -= (x_center - 320) / 320. * 29.
    angle -= (x_center - 320) / 320. * 5
    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180

    # if angle < 0:
    #     angle = 0
    # elif angle > 180:
    #     angle = 180
    set_servo_angle(angle)

if __name__ == '__main__':
    # net_path = "/home/snorlax/Projects/SiamFC-pytorch/siamfc_alexnet_e50.pth"
    # model_path = "weights/pruned_model_40.pth"
    model_path = "weights/SiamFC_100.pth"

    init_time = time.time()

    tracker = TrackerSiamFC(model_path)

    dataset = LoadStreams(sources='0')

    _, _, im0, _ = next(iter(dataset))
    img = cv2.cvtColor(im0[0], cv2.COLOR_BGR2RGB)
    
    w, h = np.array(img.shape[:2]) // 2
    x, y = np.array(img.shape[:2]) // 2 - np.array([w, h]) // 2
    tracker.init(img, np.array([y, x, h, w], dtype=np.float32))

    print(img.squeeze().shape, im0[0].shape, len(im0))

    cv2.imshow("test", im0[0])

    print(">> Init", time.time() - init_time)

    for _, img, im0, _ in dataset:
        st_time = time.time()
        img = cv2.cvtColor(im0[0], cv2.COLOR_BGR2RGB)
        bbox = tracker.update(img)

        print(">> Inference:", time.time() - st_time)

        x, y, w, h = bbox
        cv2.rectangle(im0[0], (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)

        cv2.imshow("test", im0[0])
        cv2.waitKey(1)

        x_center = x + w // 2
        y_center = y + h // 2

        move_motor(x_center, y_center)
       
        print(">> Round:", time.time() - st_time)
