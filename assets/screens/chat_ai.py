from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from utils.ai_engine import get_chatbot_response

class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=15, padding=30)

        self.layout.add_widget(Label(text="Cyber Mentor", font_size=26, bold=True))
        self.chat_label = Label(text="Ask me anything about cyber safety!", font_size=18)
        self.layout.add_widget(self.chat_label)

        self.input = TextInput(hint_text="Type your question...", multiline=False, size_hint=(1, 0.15))
        self.layout.add_widget(self.input)

        ask_btn = Button(text="Ask", size_hint=(1, 0.15))
        ask_btn.bind(on_release=self.ask_question)
        self.layout.add_widget(ask_btn)

        back_btn = Button(text="Back to Home", size_hint=(1, 0.15))
        back_btn.bind(on_release=self.go_home)
        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def ask_question(self, instance):
        question = self.input.text
        response = get_chatbot_response(question)
        self.chat_label.text = f"Mentor: {response}"

    def go_home(self, instance):
        self.manager.current = 'home'
