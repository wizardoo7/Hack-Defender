from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.home import HomeScreen
from screens.level1 import Level1Screen
from screens.level2 import Level2Screen
from screens.level3 import Level3Screen
from screens.level4 import Level4Screen
from screens.level5 import Level5Screen
from screens.chat_ai import ChatScreen

class HackDefenderApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(Level1Screen(name='level1'))
        sm.add_widget(Level2Screen(name='level2'))
        sm.add_widget(Level3Screen(name='level3'))
        sm.add_widget(Level4Screen(name='level4'))
        sm.add_widget(Level5Screen(name='level5'))
        sm.add_widget(ChatScreen(name='chat'))
        return sm

if __name__ == '__main__':
    HackDefenderApp().run()
