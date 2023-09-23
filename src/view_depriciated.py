from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout
import model
from PyQt5.QtCore import QSize

class QueryConstructor(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Query Constructor")

        # Create input fields
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()

        # Create "Run" button
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_query)

        # Create output field
        self.output = QLineEdit()
        self.output.setReadOnly(True)

        # Create and set layout
        layout = QFormLayout()
        layout.addRow(QLabel("Article Link:"), self.input1)
        layout.addRow(QLabel("ChatGPT Question Prompt:"), self.input2)
        layout.addRow(run_button)
        layout.addRow(QLabel("ChatGPT Response:"), self.output)

        self.setLayout(layout)

    def run_query(self):
        input1 = self.input1.text()
        input1 = model.extract_article_text(input1)
        input2 = self.input2.text()
        result = model.chat_gpt_api(input2 + input1)
        print(result)
        self.output.setText(result)

if __name__ == '__main__':
    app = QApplication([])

    window = QueryConstructor()
    window.show()

    app.exec_()