import datetime
import random
from mss import mss
from lib.activity import Activity
from lib.shutter import Shutter

class Ticker:
    def __init__(self, activity: Activity) -> None:
        now = datetime.datetime.now()
        self.next_shot = now.minute + random.randrange(1, 4)
        self.screenshotter = mss()
        self.screenshotter.compression_level = 9
        self.shutter = Shutter(activity)

    def tick(self):
        now = datetime.datetime.now()
        if now.minute % 10 == 0:
            rand_offset = random.randrange(0, 10)
            self.next_shot = now.minute + rand_offset
        if now.minute == self.next_shot:
            self.shutter.shot()