from gettext import dpgettext
from mimetypes import init
from multiprocessing.sharedctypes import Value
from typing import Counter
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty



# main interface-MainWidget
# use dp instead of pixels because dp corresponds to actual size in every device. 
# size: "40dp" , "40dp" --> width, height 
# pos: "100dp", "200dp" --> x, y 
# color: 1, 0, 0, 1 --> r, g, b, a ; a -> alpha (visibility)

# Box Layout: size is relative to resizing of window. 
# size can be changed, by using size_hint: <width in proportion>, <height in proportion>
# size_hint: None, None -> after that size can be fixed. 
# pos_hint: {<"">:} x, center_x, right ; y, center_y, top

class WidgetsEx(GridLayout):
    text = StringProperty("0")
    counter = 1
    count_enable = BooleanProperty(False)
    slider_text = StringProperty("50")
    input_str  = StringProperty()

    # switch_enable = BooleanProperty(False)

    def click(self):
        if self.count_enable:
            self.text = str(int(self.text) + self.counter )
            print(self.text)
    
    def reset(self):
        self.text = "0"
        print(self.text)
        

    def my_toggle(self, toggle):
        print("Toggle state: "+toggle.state)

        if toggle.state == "normal":
            toggle.text = "OFF"
            self.count_enable = False
        else:
            toggle.text = "ON"
            self.count_enable = True
    
    def my_switch(self, switch):
        print(switch.active)
        if switch.active:
            self.count_enable = True
        else:
            self.count_enable = False
    
    # def my_slider(self, slide):
    #     print(int(slide.value))
    #     self.slider_text = str(int(slide.value))

    def text_validate(self, text_inp):
        self.input_str = text_inp.text

class InfoForm(GridLayout):
    # sub = StringProperty("You Entered Nothing")
    sub = StringProperty()
    def submit(self, txt, name, age, likes):
        if name.text == "" or age.text == "" or likes.text == "":
            self.sub = "Enter full details"
        else:
            self.sub = f"Hello {name.text.strip()} you are {age.text.strip()} years old, your likes are {likes.text.strip()}"
            name.text = ""
            age.text = ""
            likes.text = ""
        print(self.sub)


class Box(BoxLayout):
    pass

    '''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    '''

class StackLayoutExample(StackLayout):
    pass

# class scroll(ScrollView):
#     pass

class Grid(GridLayout):
    pass

class Anchor(AnchorLayout):
    pass


class MainWidget(Widget):
    pass


class widgets(App):
    pass

# main
widgets().run()
# Box().run()