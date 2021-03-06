from enum import Enum


class CarStatus(Enum):
    STOPPED = 0
    TAKING_IMAGE = 2
    IMAGE_TAKEN = 3
    UPLOADING_IMAGE = 4
    IMAGE_UPLOADED = 5
    ANALYSING_IMAGE = 6
    TRAFFIC_LIGHT_DETECTED = 7
    TRAFFIC_LIGHT_NOT_PRESENT = 8
    MOVING_FORWARD = 9
    MOVING_BACKWARD = 10
