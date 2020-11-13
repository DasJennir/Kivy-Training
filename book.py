import kivy
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty #import object from .kv
from kivy.lang import Builder #specify kv

Builder.load_file('./book.kv')

class MyGridLayout(Widget):

    title = ObjectProperty(None)
    author = ObjectProperty(None)
    content = ObjectProperty(None)

    def press(self):
        title = self.title.text
        author = self.author.text
        content = self.content.text

        #self.add_widget(Label(text=f"Book {title} has been publish by {author} {idd}"))
        print(f"Book {title} has been publish by {author} {content}")
        self.title.text = ""
        self.author.text = ""
        self.content.text = ""
    


class BookED(App): #call kv file BookED.kv
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    BookED().run()




''' def __init__(self, **kwargs):

super(MyGridLayout, self).__init__(**kwargs)

#Root Design
self.cols = 1
self.row_force_default=True
self.row_default_height=100
self.col_force_default=True
self.col_default_width=400

#create a second gridlayout
self.top_grid = GridLayout(
    row_force_default=True,
    row_default_height=40,
    col_force_default=True,
    col_default_width=200 #width of each column
)
self.top_grid.cols = 2

self.top_grid.add_widget(Label(text="Title: "))
self.title = TextInput(multiline=False,font_size= 20,)
self.top_grid.add_widget(self.title)

self.top_grid.add_widget(Label(text="Author: "))
self.author = TextInput(multiline=False)
self.top_grid.add_widget(self.author) 

self.top_grid.add_widget(Label(text="Id: "))
self.id = TextInput(multiline=False)
self.top_grid.add_widget(self.id)

self.add_widget(self.top_grid)

self.submit = Button(text="Submit",
font_size= 32, #set font
size_hint_y = None, #if you remove it the size wont change
height= 50 
)
self.submit.bind(on_press=self.press)
self.add_widget(self.submit)'''