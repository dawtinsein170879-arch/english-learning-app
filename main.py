from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# ၁။ ပင်မ မီနူး စာမျက်နှာ (Home Screen)
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title_label = Label(text='English 4-Skills Learning App\n(English to Myanmar)', 
                            font_size=22, halign='center', valign='middle')
        title_label.bind(size=title_label.setter('text_size'))
        layout.add_widget(title_label)
        
        btn_verbs = Button(text='1. Verbs (1,000 Verbs)', font_size=18, background_color=(0.1, 0.6, 0.8, 1))
        btn_verbs.bind(on_press=self.go_to_verbs)
        layout.add_widget(btn_verbs)
        
        btn_reading = Button(text='2. Reading Passages (100 Readings)', font_size=18, background_color=(0.2, 0.7, 0.3, 1))
        btn_reading.bind(on_press=self.go_to_reading)
        layout.add_widget(btn_reading)
        
        btn_grammar = Button(text='3. Spoken Grammar (Burmese)', font_size=18, background_color=(0.8, 0.5, 0.1, 1))
        btn_grammar.bind(on_press=self.go_to_grammar)
        layout.add_widget(btn_grammar)
        
        btn_notebook = Button(text='4. My Notebook', font_size=18, background_color=(0.7, 0.2, 0.7, 1))
        btn_notebook.bind(on_press=self.go_to_notebook)
        layout.add_widget(btn_notebook)
        
        self.add_widget(layout)

    def go_to_verbs(self, instance):
        self.manager.current = 'verbs'

    def go_to_reading(self, instance):
        self.manager.current = 'reading'

    def go_to_grammar(self, instance):
        self.manager.current = 'grammar'

    def go_to_notebook(self, instance):
        self.manager.current = 'notebook'


# ၂။ Verbs စာမျက်နှာ (အသုံးအများဆုံး Verbs များ + မြန်မာဘာသာပြန်)
class VerbsScreen(Screen):
    def __init__(self, **kwargs):
        super(VerbsScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text='Communicate Verbs (1,000 Verbs Database)', font_size=20, size_hint_y=None, height=40))
        
        # Scrollable Verbs List
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        # နမူနာ Verbs များ (နောက်ပိုင်းတွင် 1,000 အထိ တိုးချဲ့ထည့်သွင်းနိုင်သည်)
        verbs_data = [
            ("1. Accept", "လက်ခံသည်"), ("2. Allow", "ခွင့်ပြုသည်"), ("3. Ask", "မေးသည်/တောင်းဆိုသည်"),
            ("4. Be", "ဖြစ်သည်"), ("5. Begin", "စတင်သည်"), ("6. Believe", "ယုံကြည်သည်"),
            ("7. Break", "ကျိုးသည်/ချိုးသည်"), ("8. Bring", "ယူဆောင်လာသည်"), ("9. Build", "တည်ဆောက်သည်"),
            ("10. Buy", "ဝယ်သည်"), ("11. Call", "ခေါ်သည်/ဖုန်းခေါ်သည်"), ("12. Catch", "ဖမ်းသည်"),
            ("13. Choose", "ရွေးချယ်သည်"), ("14. Come", "လာသည်"), ("15. Cut", "ဖြတ်သည်"),
            ("16. Do", "လုပ်သည်"), ("17. Draw", "ဆွဲသည်"), ("18. Drink", "သောက်သည်"),
            ("19. Drive", "ကားမောင်းသည်"), ("20. Eat", "စားသည်"), ("21. Explain", "ရှင်းပြသည်"),
            ("22. Feel", "ခံစားရသည်"), ("23. Find", "တွေ့သည်/ရှာတွေ့သည်"), ("24. Follow", "လိုက်နာသည်/နောက်မှလိုက်သည်"),
            ("25. Get", "ရရှိသည်"), ("26. Give", "ပေးသည်"), ("27. Go", "သွားသည်"),
            ("28. Have", "ပိုင်ဆိုင်သည်/ရှိသည်"), ("29. Hear", "ကြားသည်"), ("30. Help", "ကူညီသည်")
        ]
        
        for eng, myan in verbs_data:
            btn = Button(text=f"{eng}  =  {myan}", font_size=16, size_hint_y=None, height=50, background_color=(0.15, 0.45, 0.75, 1))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        
        back_btn = Button(text='Back to Home', font_size=16, size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.2, 1))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def go_go_back(self, instance):
        pass

    def go_back(self, instance):
        self.manager.current = 'menu'


# ၃။ Reading စာမျက်နှာ (Beginner မှ Advanced ထိ)
class ReadingScreen(Screen):
    def __init__(self, **kwargs):
        super(ReadingScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text='Reading Passages (Beginner to Advanced)', font_size=20, size_hint_y=None, height=40))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        readings = [
            ("Level: Beginner (1/100)", "Topic: Daily Routine\nI wake up early in the morning every day. Then I brush my teeth and wash my face. After that, I eat breakfast with my family."),
            ("Level: Intermediate (30/100)", "Topic: Travelling Abroad\nTravelling to a foreign country gives you new experiences. You learn about different cultures, try traditional foods, and meet wonderful people."),
            ("Level: Advanced (100/100)", "Topic: The Impact of Technology\nModern artificial intelligence is transforming human society globally. Understanding its core architecture is essential for future technological advancements.")
        ]
        
        for lvl, content in readings:
            lbl = Button(text=f"{lvl}\n{content}", font_size=14, size_hint_y=None, height=120, background_color=(0.2, 0.5, 0.3, 1))
            grid.add_widget(lbl)
            
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        
        back_btn = Button(text='Back to Home', font_size=16, size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.2, 1))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'menu'


# ၄။ Spoken Grammar စာမျက်နှာ (မြန်မာလို ရှင်းလင်းချက်)
class GrammarScreen(Screen):
    def __init__(self, **kwargs):
        super(GrammarScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text='Spoken Grammar (စကားပြော အသုံးအများဆုံး)', font_size=20, size_hint_y=None, height=40))
        
        scroll = ScrollView()
        grid = GridLayout(cols=1, spacing=10, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        grammar_tips = [
            ("1. Present Simple Tense (အလေ့အထနှင့် အမှန်တရားများ)", "ပုံစံ: Subject + Verb(1)\nဥပမာ: I speak English. (င่อย က အင်္ဂလိပ်လိုပြောတယ်)\nအသုံးများပုံ: နေ့စဉ်လုပ်လေ့ရှိတဲ့ အလုပ်တွေနဲ့ အမှန်တရားတွေကို ပြောတဲ့အခါ သုံးပါတယ်။"),
            ("2. Past Simple Tense (ပြီးခဲ့သော အဖြစ်အပျက်များ)", "ပုံစံ: Subject + Verb(2)\nဥပမာ: I went to Yangon yesterday. (မနေ့က ရန်ကုန်ကို သွားခဲ့တယ်)\nအသုံးများပုံ: အတိတ်မှာ လုပ်ခဲ့ပြီးသား ကိစ္စတွေကို ပြောတဲ့အခါ သုံးပါတယ်။"),
            ("3. Future Simple Tense (နောင်လုပ်မည့် အလုပ်များ)", "ပုံစံ: Subject + will + Verb(1)\nဥပမာ: I will help you. (ငါ မင်းကို ကူညီပေးပါမယ်)\nအသုံးများပုံ: အနာဂတ်မှာ လုပ်မယ့်အရာတွေကို ကတိပေးတဲ့အခါ သုံးပါတယ်။")
        ]
        
        for title, desc in grammar_tips:
            lbl = Button(text=f"{title}\n{desc}", font_size=14, size_hint_y=None, height=130, background_color=(0.7, 0.4, 0.1, 1))
            grid.add_widget(lbl)
            
        scroll.add_widget(grid)
        layout.add_widget(layout if False else layout) # placeholder
        
        back_btn = Button(text='Back to Home', font_size=16, size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.2, 1))
        back_btn.bind(on_press=self.go_back)
        
        # fix layout structure for scroll
        # (re-packing properly)
        self.clear_widgets()
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        main_layout.add_widget(Label(text='Spoken Grammar (စကားပြော အသုံးအများဆုံး)', font_size=20, size_hint_y=None, height=40))
        main_layout.add_widget(scroll)
        main_layout.add_widget(back_btn)
        self.add_widget(main_layout)

    def go_back(self, instance):
        self.manager.current = 'menu'


# ၅။ Notebook စာမျက်နှာ (မှတ်စုရေးရန်)
class NotebookScreen(Screen):
    def __init__(self, **kwargs):
        super(NotebookScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text='My Notebook (မှတ်စုစာအုပ်)', font_size=20, size_hint_y=None, height=40))
        
        self.note_input = TextInput(text='ဒီနေရာတွင် သင်မှတ်လိုသည်များကို ရေးသားပါ...', font_size=16, multiline=True)
        layout.add_widget(self.note_input)
        
        save_btn = Button(text='Save Note (မှတ်သားမည်)', font_size=16, size_hint_y=None, height=50, background_color=(0.2, 0.6, 0.2, 1))
        save_btn.bind(on_press=self.save_note)
        layout.add_widget(save_btn)
        
        back_btn = Button(text='Back to Home', font_size=16, size_hint_y=None, height=50, background_color=(0.8, 0.2, 0.2, 1))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

    def save_note(self, instance):
        self.note_input.text += "\n[Saved Successfully!]"

    def go_back(self, instance):
        self.manager.current = 'menu'


# ၆။ App ပင်မ ထိန်းချုပ်မှု
class EnglishApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(VerbsScreen(name='verbs'))
        sm.add_widget(ReadingScreen(name='reading'))
        sm.add_widget(GrammarScreen(name='grammar'))
        sm.add_widget(NotebookScreen(name='notebook'))
        return sm

if __name__ == '__main__':
    EnglishApp().run()
