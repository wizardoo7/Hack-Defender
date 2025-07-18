from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Level4Screen(Screen):
    def __init__(self, **kwargs):
        super(Level4Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        self.layout.add_widget(Label(text="Level 4: Public Wi-Fi Safety", font_size=22))
        self.layout.add_widget(Label(text="You’re in a coffee shop. What should you do?", font_size=18))

        btn_wrong = Button(text="Use free Wi-Fi to check bank account", on_release=self.wrong)
        btn_right = Button(text="Connect via VPN before browsing", on_release=self.correct)

        self.feedback = Label(text="", font_size=18)

        self.layout.add_widget(btn_wrong)
        self.layout.add_widget(btn_right)
        self.layout.add_widget(self.feedback)

        next_btn = Button(text="Next Level (5)", size_hint=(1, 0.2))
        next_btn.bind(on_release=self.go_next)
        self.layout.add_widget(next_btn)

        self.add_widget(self.layout)

    def correct(self, instance):
        self.feedback.text = "✅ Good choice! VPN protects your online activity on public Wi-Fi."

    def wrong(self, instance):
        self.feedback.text = "❌ Wrong! Never use public Wi-Fi for sensitive activities without protection."

    def go_next(self, instance):
        self.manager.current = 'level5'
