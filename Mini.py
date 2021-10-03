from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Window.size = 300, 500

class Manager(ScreenManager):
	pass
class Main(Screen):
	pass
class scr2(Screen):
	pass

class Mini(MDApp):
	def build(self):
		self.title = "Changefy"
		self.icon = "language-python"
		

	def change_it(self):

		text = self.root.ids.text
		pattern = self.root.ids.pattern.text
		result = self.root.ids.result
		change_for = self.root.ids.change_for.text
		result = text.replace(pattern, change_for)
		print(text.text.replace(pattern, change_for))

		
	
Mini().run()