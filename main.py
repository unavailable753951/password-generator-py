from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.core.window import Window
import random
import pyperclip

class GeneratorHaslaGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(GeneratorHaslaGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Ustawienia okna programu
        Window.size = (400, 400)
        Window.clearcolor = (54/255, 50/255, 66/255, 1)
        Window.bind(on_resize=self.on_resize)
        Window.minimum_width = 400
        Window.minimum_height = 400

        self.title = "Generator haseł by Łukasz Rosiński 52779"

        # Nagłówek - Tytuł aplikacji
        self.add_widget(Label(text="Twoje wygenerowane hasło", size_hint_y=None, height=30, color=(1, 1, 1, 1)))

        # Pole tekstowe na hasło
        self.pole_hasla = Label(text="", size_hint=(None, None), size=(300, 50), font_size=11, halign='center', valign='middle', text_size=(300, None), pos_hint={'center_x': 0.5})
        self.add_widget(self.pole_hasla)

        # Przyciski Generuj hasło i Kopiuj hasło
        self.przycisk_generuj = Button(text="Generuj hasło", size_hint=(None, None), size=(150, 40), background_normal='', background_color=(0.2, 0.6, 1, 1), pos_hint={'center_x': 0.5})
        self.przycisk_generuj.bind(on_press=self.generuj_haslo)

        self.przycisk_kopiuj = Button(text="Kopiuj hasło", size_hint=(None, None), size=(150, 40), background_normal='', background_color=(0.2, 0.6, 1, 1), pos_hint={'center_x': 0.5})
        self.przycisk_kopiuj.bind(on_press=self.kopiuj_haslo)

        # Layout dla przycisków
        layout_przyciski = BoxLayout(size_hint=(None, None), size=(300, 40), pos_hint={'center_x': 0.5})
        layout_przyciski.add_widget(self.przycisk_generuj)
        layout_przyciski.add_widget(Label(size_hint=(None, None), width=20))
        layout_przyciski.add_widget(self.przycisk_kopiuj)
        self.add_widget(layout_przyciski)

        # Odstęp
        self.add_widget(Label(size_hint_y=None, height=20))

        # Slider dla długości hasła
        self.slider_dlugosc = Slider(min=8, max=128, value=64, step=1, size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5})
        self.slider_dlugosc.bind(value=self.on_value_slider_dlugosc)
        self.label_dlugosc = Label(text="64", size_hint=(None, None), size=(50, 30), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5})
        self.add_widget(self.slider_dlugosc)
        self.add_widget(self.label_dlugosc)
        self.add_widget(Label(text="Długość hasła:", size_hint=(None, None), size=(150, 30), color=(1, 1, 1, 1), pos_hint={'center_x': 0.5}))

        # Własne listy znaków
        self.cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.litery_AZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.litery_az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.znaki_specjalne = ['!', '@', '#', '$', '%', '^', '&', '*']

        # Checkboxy
        self.box_lewy = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5})
        self.box_prawy = BoxLayout(orientation='horizontal', size_hint=(None, None), size=(400, 30), pos_hint={'center_x': 0.5})

        self.checkbox_cyfry = CheckBox(active=True, size_hint=(None, None), size=(30, 30), color=(1, 1, 1, 1))
        self.checkbox_litery_AZ = CheckBox(active=True, size_hint=(None, None), size=(30, 30), color=(1, 1, 1, 1))
        self.checkbox_znaki_specjalne = CheckBox(active=True, size_hint=(None, None), size=(30, 30), color=(1, 1, 1, 1))
        self.checkbox_litery_az = CheckBox(active=True, size_hint=(None, None), size=(30, 30), color=(1, 1, 1, 1))

        self.box_lewy.add_widget(Label(text="Cyfry 0-9:", size_hint=(None, None), size=(150, 30), color=(1, 1, 1, 1)))
        self.box_lewy.add_widget(self.checkbox_cyfry)
        self.box_prawy.add_widget(Label(text="Litery A-Z:", size_hint=(None, None), size=(150, 30), color=(1, 1, 1, 1)))
        self.box_prawy.add_widget(self.checkbox_litery_AZ)

        self.add_widget(self.box_lewy)
        self.add_widget(self.box_prawy)

        self.box_lewy.add_widget(Label(text="Znaki !@#$%^&*:", size_hint=(None, None), size=(150, 30), color=(1, 1, 1, 1)))
        self.box_lewy.add_widget(self.checkbox_znaki_specjalne)
        self.box_prawy.add_widget(Label(text="Litery a-z:", size_hint=(None, None), size=(150, 30), color=(1, 1, 1, 1)))
        self.box_prawy.add_widget(self.checkbox_litery_az)

    def generuj_haslo(self, instance):
        dostepne_znaki = ''
        dlugosc = int(self.slider_dlugosc.value)

        if self.checkbox_cyfry.active:
            dostepne_znaki += ''.join(self.cyfry)
        if self.checkbox_litery_AZ.active:
            dostepne_znaki += ''.join(self.litery_AZ)
        if self.checkbox_znaki_specjalne.active:
            dostepne_znaki += ''.join(self.znaki_specjalne)
        if self.checkbox_litery_az.active:
            dostepne_znaki += ''.join(self.litery_az)

        if not dostepne_znaki:
            self.pole_hasla.text = "Najpierw zaznacz przynajmniej jeden rodzaj znaków."
            return

        haslo = ''.join(random.choices(dostepne_znaki, k=dlugosc))
        self.pole_hasla.text = haslo

    def kopiuj_haslo(self, instance):
        haslo = self.pole_hasla.text
        if not haslo:
            self.pole_hasla.text = "Najpierw wygeneruj hasło."
            return
        pyperclip.copy(haslo)

    def on_value_slider_dlugosc(self, instance, value):
        self.label_dlugosc.text = str(int(value))

    def on_resize(self, instance, width, height):
        Window.size = (400, 400)

class Generator_Hasla_52779(App):
    def build(self):
        return GeneratorHaslaGUI()

if __name__ == '__main__':
    Generator_Hasla_52779().run()
