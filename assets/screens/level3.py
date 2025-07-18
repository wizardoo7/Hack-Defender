from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Level3Screen(Screen):
    def __init__(self, **kwargs):
        super(Level3Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        self.layout.add_widget(Label(text="Level 3: Safe Browsing", font_size=22))

        self.question = Label(text="Which website is safer to visit?", font_size=18)
        self.layout.add_widget(self.question)

        btn_safe = Button(text="https://www.school.edu/grades", on_release=self.correct)
        btn_unsafe = Button(text="http://freemovie-downloader.ru", on_release=self.wrong)

        self.layout.add_widget(btn_safe)
        self.layout.add_widget(btn_unsafe)

        self.feedback = Label(text="", font_size=18)
        self.layout.add_widget(self.feedback)

        next_btn = Button(text="Next Level (4)")
        next_btn.bind(on_release=self.go_next)
        self.layout.add_widget(next_btn)

        self.add_widget(self.layout)

    def correct(self, instance):
        self.feedback.text = "✅ Yes! Secure domains use HTTPS and come from trusted sources."

    def wrong(self, instance):
        self.feedback.text = "❌ No! That link looks unsafe — always check the domain."

    def go_next(self, instance):
        self.manager.current = 'level4'
