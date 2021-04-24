from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
import webbrowser
import threading
car_model_helper="""
MDTextField:
    hint_text:"Enter your name:"
    icon_right:"car"

    pos_hint:{'center_x':0.5,'center_y':0.7}
    size_hint_x:None
    width:300
"""
price_helper="""
MDTextField:
    input_filter: "float"
    hint_text:"Enter your age:"
    icon_right:"car"
    helper_text:"(in integer)"
    helper_text_mode:"on_focus"
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300
"""
class MainApp(MDApp):
     def build(self):
        screen=Screen()
        label=MDLabel(text="This Machine Learning app is made by Piyush Rai",pos_hint={'center_x':0.5,'center_y':0.9},size_hint_x=None,width=300,on_release=self.show_data)
        label1=MDLabel(text="This will detect weather a person is wearing mask or not",pos_hint={'center_x':0.5,'center_y':0.8},size_hint_x=None,width=300,on_release=self.show_data)
        screen.add_widget(label)
        screen.add_widget(label1)
        '''car_model=MDTextField(text="Enter model year",pos_hint={'center_x':0.7,'center_y':0.9},size_hint_x=None,width=300)
        price=MDTextField(text="Enter the Present Price(in LAKHS)",pos_hint={'center_x':0.7,'center_y':0.8},size_hint_x=None,width=300)
        dis=MDTextField(text="Enter the distance it has travelled(in KMS)：",pos_hint={'center_x':0.7,'center_y':0.7},size_hint_x=None,width=300)
        owner_no=MDTextField(text="Enter the number of owners who have previously owned it(0 or 1 or 2 or 3)",pos_hint={'center_x':0.7,'center_y':0.6},size_hint_x=None,width=300)'''
        self.car_model=Builder.load_string(car_model_helper)
        self.price=Builder.load_string(price_helper)
        btn=MDRectangleFlatButton(text="submit",pos_hint={'center_x':0.5,'center_y':0.3},size_hint_x=None,width=300,on_release=self.show_data)
        screen.add_widget(self.car_model)
        screen.add_widget(self.price)
        screen.add_widget(btn)
        return screen
     def show_data(self , obj):
         webbrowser.open("https://teachablemachine.withgoogle.com/models/p_SB2JlW0/")
MainApp().run()    
