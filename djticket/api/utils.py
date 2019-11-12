import time
import datetime
import random


def generate_id():
    return int(time.time() + random.randint(1, 1000))


def generate_time():
    return datetime.datetime.now()
