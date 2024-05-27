from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch

from kivy.lang import Builder
from kivy.app import App
import os

Builder.load_file(os.path.join(os.path.dirname(__file__),'chatScreen.kv'))   

class ChatScreen(MDFloatLayout):
    chat_container = ObjectProperty()

    def load_chats(self):
        data = [{'source': 'img/ansiedade.png', 'username': 'Sol', 'message': 'Como voçê se sente hoje', 'data': 'Today', 'time': '21:23'}
        for i in range (5)]
        self.chat_container.data = data

# INICIO DA CLASSE CHATE ITEM 
class RightContainer(IRightBodyTouch, MDBoxLayout):
	pass

class LeftContainer(ILeftBodyTouch, MDBoxLayout):
	pass

class ChatItem(TwoLineAvatarIconListItem):
	source   = StringProperty()
	username = StringProperty()
	message  = StringProperty()
	time     = StringProperty()
	date     = StringProperty()
	check_icon = StringProperty('numeric-1-circle')

	def on_release(self, *args):
		app = App.get_running_app()
		screen_manager = app.root.screen_manager
		screen_manager.current = 'message'
		message_screen = screen_manager.get_screen('message')
		self.check_icon = ''
		message_screen.load_resource(source=self.source, username=self.username, time=self.time)