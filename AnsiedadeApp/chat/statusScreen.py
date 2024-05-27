from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder
from kivy.app import App
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'statusScreen.kv'))

class StatusScreen(MDFloatLayout):
	status_container = ObjectProperty()
	def load_status(self):
		data = [{'source':'img/ansiedade.png', 'username':'Sol', 'date':'Today'}
		for i in range(8)]
		self.status_container.data = data


class StatusItem(TwoLineAvatarIconListItem):
	source  = StringProperty('')
	username = StringProperty('')
	date    = StringProperty('')

	def on_release(self, *args):
		app = App.get_running_app()
		screen_manager = app.root.screen_manager
		screen_manager.current = 'status'
		status_screen = screen_manager.get_screen('status')
		status_screen.load_resource(source=self.source, status_source=self.source, username=self.username, time=self.date)
