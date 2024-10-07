import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PySide6.QtCore import Slot
from random_generator import RandomGenerator  # 导入 RandomGenerator 类
import PySide6.QtGui as QtGui
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("随机数生成器")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()
        self.label = QTextEdit("生成的随机数:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("生成随机数")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        # 实例化 RandomGenerator
        self.random_generator = RandomGenerator()
        # 将信号连接到槽
        self.random_generator.my_signal.connect(self.update_label)

        # 按钮点击时调用 generate_random
        self.button.clicked.connect(self.random_generator.generate_random)

    @Slot(int)
    def update_label(self, *args, **kwargs):
        output = " ".join(map(str, args)) + "\n"
        self.label.moveCursor(QtGui.QTextCursor.End)
        self.label.insertPlainText(output)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
