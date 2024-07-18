Password Generator

Description
This project aims to provide a simple tool for generating passwords for users who need to secure their accounts. The program is designed to be user-friendly and provide fast password generation of varying lengths and with different types of characters. The outcome of the project will be a straightforward graphical interface enabling password generation and copying to the clipboard.

Functional Requirements:

    -Generate Random Passwords of Specified Length:
    Users should be able to choose the length of the generated password using a slider or other interactive elements. The generated password should consist of randomly selected characters.

    -Selectable Character Types in Passwords (Digits, Letters, Special Characters):
    Users should have the option to choose the types of characters used to generate passwords. Available options should include digits, uppercase and lowercase letters, and special characters.

    -Graphical User Interface (GUI) for Convenient Usage:
    The program should have a graphical interface that enables easy and intuitive use of password generation and copying functionalities. The interface should include elements such as buttons, sliders, and labels for user control.


Non-functional Requirements

    -Cross-Platform Support (Windows, macOS, Linux):
    The program should be compatible with various operating systems like Windows, macOS, and Linux to accommodate users on different platforms.

    -Performance - Fast and Reliable Password Generation:
    The password generation process should be swift and efficient, even for generating long passwords. The program should operate stably and reliably, even under intensive usage.

    -Simple and Intuitive Operation - Suitable for Less Technical Users:
    The graphical interface should be designed to allow even less technical users to easily operate the program without prior training or knowledge of advanced techniques.

Additional Information


    Development Environment:
        -The program was developed using Visual Studio Code.

    Python Version:
        -Python 3.12 was utilized.

    Used Libraries:
        -unittest: For conducting unit tests.
        -kivy: For creating the graphical interface.
        -random: For generating random passwords.
        -pyperclip: For copying generated passwords to the clipboard.

    Classes and Methods:
        GeneratorHaslaGUI Class:
            -Contains the logic for generating and displaying passwords and handling the graphical interface.
        generate_password and copy_password Methods:
            -Responsible for generating passwords and copying them to the clipboard.
        on_value_slider_length Method:
            -Updates the displayed password length based on the slider value.
        on_resize Method:
            -Adjusts the program window size.


Testing
    Test Analysis
        The tests were conducted in the Kivy environment, providing a comprehensive evaluation of the graphical interface. Unit tests are essential for confirming the correctness of key application functions. Test results are available in the TEST.txt file. The test results indicate the application's good condition and its readiness for use by users.

Conclusion
    The application successfully passed unit tests and graphical interface testing, demonstrating its functionality and performance. Continuous monitoring and testing of the application are necessary to ensure its ongoing correctness and adaptation to any changes in the runtime environment.