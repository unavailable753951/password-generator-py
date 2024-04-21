1. Opis projektu:
Projekt ma na celu dostarczenie prostego narzędzia do generowania haseł dla użytkowników, którzy potrzebują zabezpieczyć swoje konta. Program ma być łatwy w użyciu i zapewnić szybkie generowanie haseł o różnej długości i z różnymi rodzajami znaków. Rezultatem projektu będzie prosty interfejs graficzny umożliwiający generowanie haseł oraz ich kopiowanie do schowka.

2. Analiza wymagań:
Wymagania funkcjonalne:

-Generowanie losowych haseł o określonej długości:

-Program powinien umożliwiać użytkownikowi wybór długości generowanego hasła za pomocą suwaka lub innego interaktywnego elementu. Generowane hasło powinno składać się z losowo wybranych znaków. Możliwość wyboru rodzaju znaków w haśle (cyfry, litery, znaki specjalne):

-Użytkownik powinien mieć możliwość wyboru rodzaju znaków, które zostaną użyte do wygenerowania hasła. Dostępne opcje powinny obejmować cyfry, litery (zarówno wielkie, jak i małe) oraz znaki specjalne. Interfejs graficzny umożliwiający wygodne korzystanie z programu:

-Program powinien posiadać interfejs graficzny, który umożliwia łatwe i intuicyjne korzystanie z funkcji generowania i kopiowania haseł. Interfejs powinien zawierać elementy takie jak przyciski, suwaki i etykiety, aby użytkownik mógł łatwo kontrolować proces generowania haseł.

Wymagania niefunkcjonalne:

-Obsługa różnych platform (Windows, macOS, Linux):

-Program powinien być kompatybilny z różnymi systemami operacyjnymi, takimi jak Windows, macOS i Linux, aby użytkownicy mogli korzystać z niego na swoich preferowanych platformach. Wydajność - generator powinien być szybki i niezawodny:

-Proces generowania haseł powinien być szybki i efektywny, nawet przy generowaniu haseł o dużej długości. Program powinien działać stabilnie i niezawodnie, nawet przy intensywnym użytkowaniu. Prosta i intuicyjna obsługa - nawet dla mniej zaawansowanych użytkowników. Interfejs graficzny powinien być zaprojektowany w taki sposób, aby nawet mniej zaawansowani użytkownicy mogli łatwo korzystać z programu bez konieczności wcześniejszego szkolenia lub znajomości zaawansowanych technik.

Dodatkowe informacje:
-Środowisko programistyczne: Program został napisany w środowisku Visual Studio Code.
-Wersja Pythona: Wykorzystano Pythona 3.12.

Wykorzystane biblioteki:

-unittest: Do przeprowadzenia testów jednostkowych.
-kivy: Do tworzenia interfejsu graficznego.
-random: Do generowania losowych haseł.
-pyperclip: Do kopiowania wygenerowanych haseł do schowka.
-Klasy i metody:
-Klasa GeneratorHaslaGUI: Zawiera logikę generowania i wyświetlania haseł oraz obsługę interfejsu graficznego.
-Metody generuj_haslo i kopiuj_haslo: Odpowiadają za generowanie haseł i kopiowanie ich do schowka.
-Metoda on_value_slider_dlugosc: Odpowiada za aktualizację wyświetlanej długości hasła na podstawie wartości suwaka.
-Metoda on_resize: Odpowiada za dostosowanie rozmiaru okna programu.

3. 
Kod przedstawiony to zestaw testów jednostkowych napisanych przy użyciu modułu unittest w języku Python. Testy te są zaprojektowane w celu sprawdzenia poprawności działania klasy GeneratorHaslaGUI, która odpowiada za logikę generowania i wyświetlania haseł w interfejsie graficznym.

4. Testowanie:

Analiza testów:
Testy zostały przeprowadzone w środowisku Kivy, co zapewnia kompleksową ocenę interfejsu graficznego.
Testy jednostkowe są istotne dla potwierdzenia poprawności działania kluczowych funkcji aplikacji, wyniki testu są w pliku TEST.txt
Wyniki testów świadczą o dobrym stanie aplikacji i jej gotowości do użycia przez użytkowników.
Wnioski:
Aplikacja przeszła pomyślnie testy jednostkowe i interfejsu graficznego, co świadczy o jej funkcjonalności i wydajności.
Należy kontynuować monitorowanie i testowanie aplikacji w celu zapewnienia jej ciągłej poprawności i dostosowania do ewentualnych zmian w środowisku uruchomieniowym.