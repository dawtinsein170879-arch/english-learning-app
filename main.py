import json
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

VERBS_DATA = [
    {"verb": "accept", "past": "accepted", "pp": "accepted", "mm": "လက်ခံသည်"},
    {"verb": "achieve", "past": "achieved", "pp": "achieved", "mm": "အောင်မြင်သည်/ရရှိသည်"},
    {"verb": "communicate", "past": "communicated", "pp": "communicated", "mm": "ဆက်သွယ်ပြောဆိုသည်"},
]

class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        layout.add_widget(Label(text="[b]English 4 Skills Learning App[/b]", markup=True, font_size='22sp'))
        
        btn_verbs = Button(text="Verbs List", size_hint_y=None, height=50)
        btn_verbs.bind(on_release=lambda x: setattr(self.manager, 'current', 'verbs'))
        
        btn_notebook = Button(text="My Notebook", size_hint_y=None, height=50)
        btn_notebook.bind(on_release=lambda x: setattr(self.manager, 'current', 'notebook'))
        
        layout.add_widget(btn_verbs)
        layout.add_widget(btn_notebook)
        
        self.add_widget(layout)

class VerbsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text="Verbs List", font_size='18sp', size_hint_y=None, height=40))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        for item in VERBS_DATA:
            text = f"V1: {item['verb']} | V2: {item['past']} | V3: {item['pp']}\nMM: {item['mm']}"
            grid.add_widget(Label(text=text, size_hint_y=None, height=60))
            
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        
        back_btn = Button(text="Back", size_hint_y=None, height=40)
        back_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

class NotebookScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text="My Personal Notebook", font_size='18sp', size_hint_y=None, height=30))
        
        self.input_note = TextInput(hint_text="Write note here...", multiline=True)
        layout.add_widget(self.input_note)
        
        btn_layout = BoxLayout(size_hint_y=None, height=40, spacing=10)
        save_btn = Button(text="Save Note")
        save_btn.bind(on_release=self.save_note)
        
        back_btn = Button(text="Back")
        back_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'main'))
        
        btn_layout.add_widget(save_btn)
        btn_layout.add_widget(back_btn)
        layout.add_widget(btn_layout)
        
        self.add_widget(layout)
        self.load_note()

    def save_note(self, instance):
        with open("user_notebook.txt", "w", encoding="utf-8") as f:
            f.write(self.input_note.text)

    def load_note(self):
        if os.path.exists("user_notebook.txt"):
            with open("user_notebook.txt", "r", encoding="utf-8") as f:
                self.input_note.text = f.read()

class EnglishLearningApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main'))
        sm.add_widget(VerbsScreen(name='verbs'))
        sm.add_widget(NotebookScreen(name='notebook'))
        return sm

if __name__ == '__main__':
    EnglishLearningApp().run()
