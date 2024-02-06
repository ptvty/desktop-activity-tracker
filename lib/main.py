import time
from lib.activity import Activity
from lib.event_handler import EventHandler
from lib.ticker import Ticker

activity = Activity()
ticker = Ticker(activity)
even_hanlder = EventHandler(activity)

def main():
    even_hanlder.listen()
    while True:
        activity.tick()
        ticker.tick()
        time.sleep(60)