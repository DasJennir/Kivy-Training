import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):

        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Title: "))
        self.title = TextInput(multiline=False)
        self.add_widget(self.title)

        self.add_widget(Label(text="Author: "))
        self.author = TextInput(multiline=False)
        self.add_widget(self.author)

        self.add_widget(Label(text="Id: "))
        self.id = TextInput(multiline=False)
        self.add_widget(self.id)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        title = self.title.text
        author = self.author.text
        idd = self.id.text

        self.add_widget(Label(text=f"Book {title} has been publish by {author} {idd}"))
        self.title.text = ""
        self.author.text = ""
        self.id.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()