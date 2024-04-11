from kivymd.uix.screen import MDScreen

from kivy.lang import Builder
from kivy.clock import Clock

import os

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

Builder.load_file(os.path.join(os.path.dirname(__file__), 'batePapo.kv'))
class BatePapoScreen(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.load,1)

    def load(self, interval):
        self.ids.chats.load_chats()
        self.ids.groups.load_groups()
        self.ids.status.load_status()

class ScreenTab(MDTabsBase, MDFloatLayout):
    pass