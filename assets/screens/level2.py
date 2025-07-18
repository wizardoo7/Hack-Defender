from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

phishing_questions = [
    ("Your bank emails: 'Update your info urgently here: bit.ly/securebank'", True),
    ("A friend shares a funny video from YouTube.", False),
    ("Message: 'You won a free iPhone, click to claim!'", True),
    ("School sends results link with official domain.", False),
]

class Level2Screen(Screen):
    def __init__(self, **kwargs):
        super(Level2Screen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=15, padding=30)
        self.feedback = Label(text="", font_size=18)
        self.question_index = 0

        self.title = Label(text="Level 2: Spot the Phishing!", font_size=22)
        self.layout.add_widget(self.title)

        self.question_label = Label(text="", font_size=18)
        self.layout.add_widget(self.question_label)

        btn_phishing = Button(text="Phishing", on_release=self.check_phishing)
        btn_safe = Button(text="Safe", on_release=self.check_safe)

        self.layout.add_widget(btn_phishing)
        self.layout.add_widget(btn_safe)
        self.layout.add_widget(self.feedback)

        next_btn = Button(text="Next Level (3)", size_hint=(1, 0.15))
        next_btn.bind(on_release=self.go_next)
        self.layout.add_widget(next_btn)

        self.add_widget(self.layout)
        self.show_question()

    def show_question(self):
        q, _ = phishing_questions[self.question_index]
        self.question_label.text = q

    def check_phishing(self, instance):
        correct = phishing_questions[self.question_index][1]
        if correct:
            self.feedback.text = "✅ Correct! This is phishing."
        else:
            self.feedback.text = "❌ Nope. This one is safe."
        self.next_q()

    def check_safe(self, instance):
        correct = phishing_questions[self.question_index][1]
        if not correct:
            self.feedback.text = "✅ Correct! This is safe."
        else:
            self.feedback.text = "❌ That's phishing. Be careful!"
        self.next_q()

    def next_q(self):
        self.question_index = (self.question_index + 1) % len(phishing_questions)
        self.show_question()

    def go_next(self, instance):
        self.manager.current = 'level3'
