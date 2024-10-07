import sys
import random
from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6 import QtGui


class RandomGenerator(QThread):
    my_signal = Signal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        # 在新线程中循环生成随机数
        for i in range(30):
            a = random.randint(1, 100)
            print(f"生成的随机数: {a}")
            self.my_signal.emit(a)  # 发出信号
            self.msleep(200)  # 控制生成速度，可以根据需要进行调整


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("随机数生成器")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()
        self.label = QLabel("生成的随机数:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("开始生成随机数")
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        # 实例化 RandomGenerator
        self.random_generator = RandomGenerator()
        # 将信号连接到槽
        self.random_generator.my_signal.connect(self.update_label)

        # 按钮点击时启动线程
        self.button.clicked.connect(self.start_generation)

    def start_generation(self):
        self.random_generator.start()  # 启动新线程

    @Slot(int)
    def update_label(self, value):
        output = f"{value} "
        self.label.moveCursor(QtGui.QTextCursor.End)
        self.label.insertPlainText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
