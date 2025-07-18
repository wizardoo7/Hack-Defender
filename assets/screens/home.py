from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        layout.add_widget(Label(text="Hack Defender", font_size=32, bold=True))
        layout.add_widget(Label(text="Learn Cyber Safety the Fun Way!", font_size=18))

        start_btn = Button(text="Start Game", size_hint=(1, 0.2))
        start_btn.bind(on_release=self.go_to_level)
        layout.add_widget(start_btn)

        chat_btn = Button(text="Chat with Cyber Mentor", size_hint=(1, 0.2))
        chat_btn.bind(on_release=self.go_to_chat)
        layout.add_widget(chat_btn)

        self.add_widget(layout)

    def go_to_level(self, instance):
        self.manager.current = 'level1'

    def go_to_chat(self, instance):
        self.manager.current = 'chat'