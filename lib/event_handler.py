from pynput import keyboard
from pynput import mouse
from lib.activity import Activity

class EventHandler:
    def __init__(self, activity: Activity):
        self.temp_keys = 0
        self.temp_clicks = 0
        self.history = []
        self.activity = activity

    def on_release(self, key):
        self.activity.keyboard += 1

    def on_click(self, x, y, btn, pressed):
        if pressed:
            self.activity.mouse += 1

    def on_scroll(self, w, x, y, z):
        self.activity.mouse += 1
        
    def listen(self):
        mouse_listener = mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll)
        mouse_listener.start()
        kb_listener = keyboard.Listener(on_release=self.on_release)
        kb_listener.start()