import unittest
from kivy.clock import mainthread
from kivy.tests.async_common import UnitKivyApp
from kivy.tests.common import GraphicUnitTest
from main import GeneratorHaslaGUI

class TestGeneratorHaslaGUI(GraphicUnitTest):

    @mainthread
    def test_generowanie_hasla(self):
        app = UnitKivyApp()

        # Utwórz instancję interfejsu
        gui = GeneratorHaslaGUI()

        # Symuluj kliknięcie przycisku generowania hasła
        gui.generuj_haslo(None)

        # Sprawdź, czy pole hasła nie jest puste po kliknięciu przycisku
        self.assertNotEqual(gui.pole_hasla.text, "")

    @mainthread
    def test_kopiowanie_hasla(self):
        app = UnitKivyApp()

        # Utwórz instancję interfejsu
        gui = GeneratorHaslaGUI()

        # Symuluj kliknięcie przycisku kopiowania hasła
        gui.kopiuj_haslo(None)

        # Sprawdź, czy skopiowane hasło jest identyczne z wygenerowanym hasłem
        self.assertEqual(gui.pole_hasla.text, pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
