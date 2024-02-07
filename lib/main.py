import time
from lib.activity import Activity
from lib.event_handler import EventHandler
from lib.ticker import Ticker
from lib.helpers import console_args, null_stderr

def main():
    args = console_args()
    if not args.enable_stderr:
        null_stderr()

    activity = Activity(args.project_name)
    ticker = Ticker(activity)
    even_hanlder = EventHandler(activity)
    even_hanlder.listen()
    while True:
        activity.tick()
        ticker.tick()
        time.sleep(60)