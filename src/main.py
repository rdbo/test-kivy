from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
#kivy.require("1.9.1")

class MainApp(App):
    def build(self):
        return Button(text="test-app")

if(__name__ == "__main__"):
    MainApp().run()