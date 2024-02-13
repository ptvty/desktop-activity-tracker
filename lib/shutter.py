import winsound
import datetime
import time
import random
from pynotifier import NotificationClient, Notification
from pynotifier.backends import platform
from mss import mss
from pathlib import Path
from lib.activity import Activity

class Shutter:
    def __init__(self, activity: Activity) -> None:
        now = datetime.datetime.now()
        self.next_shot = now.minute + random.randrange(1, 4)
        self.screenshotter = mss()
        self.screenshotter.compression_level = 9
        self.activity = activity
        print(f'✅ Tracking started for "{self.project_name()}" project')

    def shot(self):
        shot_info = self.shot_info()
        output_path = f'Screenshots/{shot_info['shot_date']}'
        Path(output_path).mkdir(parents=True, exist_ok=True)
        output_file = f'{output_path}/{shot_info['file_name']}.png'
        self.screenshotter.shot(mon=-1, output=output_file)
        self.beep()
        self.notify()
    
    def shot_info(self):
        now = datetime.datetime.now()
        active_minutes = str(self.activity.activity())
        shot_time = time.strftime("%H-") + str(now.minute // 10) + '0'
        shot_date = time.strftime("%Y-%m-%d")
        window_title = self.slugify(self.active_window())
        project_name = self.project_name()
        return {
            'project_name': project_name,
            'window_title': window_title,
            'active_minutes': active_minutes,
            'shot_time': shot_time,
            'shot_date': shot_date,
            'file_name': f'{shot_time} {active_minutes} {project_name} {window_title}'
        }
    
    def beep(self):
        winsound.PlaySound("lib/shutter.wav", winsound.SND_FILENAME)

    def notify(self):
        c = NotificationClient()
        info = self.shot_info()
        title = title=f'Screenshot saved | Project: {info['project_name']} | Activity: {info['active_minutes']}/10'
        message = f'Window: {info['window_title']}'
        notification = Notification(
            title=title if len(title) <= 62 else title[:60] + '...',
            message=message if len(message) <= 122 else message[:120] + '...'[:120]
        )
        c.register_backend(platform.Backend())
        c.notify_all(notification)
        print(f'📸 {info['shot_time']} | {title}')

    def active_window(self):
        import pygetwindow as gw
        window = gw.getActiveWindow()
        return window.title if window else 'No-Title'

    def project_name(self):
        return self.activity.project_name

    def slugify(self, value, allow_unicode=True):
        import unicodedata
        import re
        value = str(value)
        if allow_unicode:
            value = unicodedata.normalize('NFKC', value)
        else:
            value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        value = re.sub(r'[^\w\s-]', '.', value)
        return re.sub(r'[-\s]+', '-', value).strip('-_')