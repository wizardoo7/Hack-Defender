from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

statements = [
    ("It's okay to reuse passwords for different accounts.", False),
    ("You should install updates regularly.", True),
    ("Antivirus is not useful anymore.", False),
    ("Multi-Factor Authentication (MFA) adds extra security.", True),
]

class Level5Screen(Screen):
    def __init__(self, **kwargs):
        super(Level5Screen, self).__init__(**kwargs)
        self.statement_index = 0
        self.layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        self.layout.add_widget(Label(text="Level 5: Cyber True or False", font_size=22))

        self.statement_label = Label(text="", font_size=18)
        self.feedback = Label(text="", font_size=18)

        btn_true = Button(text="True", on_release=self.check_true)
        btn_false = Button(text="False", on_release=self.check_false)

        self.layout.add_widget(self.statement_label)
        self.layout.add_widget(btn_true)
        self.layout.add_widget(btn_false)
        self.layout.add_widget(self.feedback)

        finish_btn = Button(text="🎉 Finish Game", size_hint=(1, 0.2))
        finish_btn.bind(on_release=self.go_home)
        self.layout.add_widget(finish_btn)

        self.add_widget(self.layout)
        self.show_statement()

    def show_statement(self):
        statement, _ = statements[self.statement_index]
        self.statement_label.text = statement

    def check_true(self, instance):
        self.check_answer(True)

    def check_false(self, instance):
        self.check_answer(False)

    def check_answer(self, user_answer):
        correct = statements[self.statement_index][1]
        if user_answer == correct:
            self.feedback.text = "✅ Correct!"
        else:
            self.feedback.text = "❌ Not quite right."

        self.statement_index = (self.statement_index + 1) % len(statements)
        self.show_statement()

    def go_home(self, instance):
        self.manager.current = 'home'
