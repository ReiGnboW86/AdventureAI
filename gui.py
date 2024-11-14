import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLineEdit

class AdventureGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Adventure AI')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.text_box = QTextEdit(self)
        self.text_box.setReadOnly(True)
        layout.addWidget(self.text_box)

        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        central_widget.setLayout(layout)

    def display_scene(self, scene_text):
        self.text_box.append(scene_text)

    def get_player_input(self):
        return self.input_field.text()

def run_gui():
    app = QApplication(sys.argv)
    gui = AdventureGUI()
    gui.show()
    sys.exit(app.exec_())
