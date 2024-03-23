from kivy.app import App
from kivy.uix.lable import Lable

class MyApp(App):
	def build(self):
		return Lable(text='Hello World')

if __name__ == '__main__':
	MyApp().run()