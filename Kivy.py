from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from functools import partial


#def on_enter(instance, value):
#    print(instance)

class Teste(App):
    def build(self):
        i = 0
        box = BoxLayout()
        self.l1 = Label(text="Contador: "+str(i))
        bt1 = Button(text="BOTÃO 1", on_press=partial(incrementar(i, bt1)))
        box.add_widget(self.l1)
        box.add_widget(bt1)
        return box

    def incrementar( i,button):
        button.text="TESTE"
        self.l1.text = "Contador: "+str(i)



Teste().run()