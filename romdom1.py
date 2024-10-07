# 创建一个类，这个类每此调用，每500ms产生一个随机数
import time
import random

# 调用pyside6的信号槽put模块
from PySide6.QtCore import QObject, Signal, Slot


# my_signal = Signal(int)


class RandomGenerator(QObject):
    my_signal = Signal(str)
    def __init__(self):
        super().__init__()
    @Slot()
    def generate_random(self):
        for i in range(30):
            a = random.randint(1, 100)
            print(i, a)
            self.my_signal.emit(str(a))
            time.sleep(0.5)