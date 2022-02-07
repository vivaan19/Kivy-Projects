from gettext import dpgettext
from mimetypes import init
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp




# main interface-MainWidget
# use dp instead of pixels because dp corresponds to actual size in every device. 
# size: "40dp" , "40dp" --> width, height 
# pos: "100dp", "200dp" --> x, y 
# color: 1, 0, 0, 1 --> r, g, b, a ; a -> alpha (visibility)

# Box Layout: size is relative to resizing of window. 
# size can be changed, by using size_hint: <width in proportion>, <height in proportion>
# size_hint: None, None -> after that size can be fixed. 
# pos_hint: {<"">:} x, center_x, right ; y, center_y, top
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            size = dp(100)
            b = Button(text = str(i+1), size_hint=(None, None), size = (size, size))
            self.add_widget(b)

# class scroll(ScrollView):
#     pass
class Grid(GridLayout):
    pass

class Anchor(AnchorLayout):
    pass


class MainWidget(Widget):
    pass


class first_app(App):
    pass

# main
first_app().run()
# Box().run()