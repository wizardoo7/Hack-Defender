from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.ai_engine import get_password_feedback

class Level1Screen(Screen):
    def __init__(self, **kwargs):
        super(Level1Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        self.feedback_label = Label(text="", font_size=18)

        self.layout.add_widget(Label(text="Level 1: Choose the Strongest Password", font_size=22, bold=True))

        options = [
            "12345678",
            "P@ssw0rd!",
            "qwerty",
            "letmein2024",
            "MyDog123!",
            "abc123456",
            "CyberN1nja!",
            "pass1234"
        ]

        for option in options:
            btn = Button(text=option, size_hint=(1, 0.2))
            btn.bind(on_release=self.check_password)
            self.layout.add_widget(btn)

        self.layout.add_widget(self.feedback_label)

        next_btn = Button(text="Next Level (2)", size_hint=(1, 0.2))
        next_btn.bind(on_release=self.go_next)
        self.layout.add_widget(next_btn)

        self.add_widget(self.layout)

    def check_password(self, instance):
        password = instance.text
        feedback = get_password_feedback(password)
        self.feedback_label.text = f"Feedback: {feedback}"

    def go_next(self, instance):
        self.manager.current = 'level2'
