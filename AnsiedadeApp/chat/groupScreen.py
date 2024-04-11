from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'groupscreen.kv'))


class GroupScreen(MDFloatLayout):
	group_container = ObjectProperty()
	def load_groups(self):
		data = [{'source':'img/ansiedade.png', 'username':'Sol', 'message':'Ajornada é tão importante quanto ao destino', 'date':'Today', 'time':'10:12 AM'}
		for i in range(30)]
		self.group_container.data = data
	
