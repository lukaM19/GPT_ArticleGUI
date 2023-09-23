import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from view import QueryConstructor, QueryConstructorApp
from kivy.app import App

class ApiKeyInputWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.label = QLabel("Enter your API key:")
        self.api_key_input = QLineEdit()
        self.save_button = QPushButton("Save")

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.api_key_input)
        layout.addWidget(self.save_button)

        # Set the layout
        self.setLayout(layout)

        # Connect the save button to a function that saves the API key as a string and launches a new window
        self.save_button.clicked.connect(self.save_api_key)

    def save_api_key(self):
        api_key = self.api_key_input.text()
        # Do something with the API key, e.g. save it to a file or use it to make API calls
        print(f"API key entered: {api_key}")
        self.close()
        # Launch a new window
        app = QueryConstructorApp(api_key)
        app.run()

class ApiKeyInputWindowApp(App):
    def build(self):
        return ApiKeyInputWindow()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApiKeyInputWindow()
    window.show()
    sys.exit(app.exec_())