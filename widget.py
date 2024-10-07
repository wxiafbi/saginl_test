# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtGui
import romdom1
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.random_generator = romdom1.RandomGenerator()
        self.random_generator.my_signal.connect(self.custom_print)
        self.ui.pushButton.clicked.connect(romdom1.RandomGenerator.generate_random)
        # self.random_generator.my_signal.connect(self.custom_print)
    
    def custom_print(self, *args, **kwargs):
        output = " ".join(map(str, args)) + "\n"
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.ui.textEdit.insertPlainText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
