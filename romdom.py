# 创建一个类，这个类每此调用，每500ms产生一个随机数
import time
import random

# 调用pyside6的信号槽put模块
from PySide6.QtCore import QTimer
from PySide6.QtCore import Signal
from PySide6.QtCore import QObject


# my_signal = Signal(int)


class RandomGenerator(QObject):
    my_signal = Signal(int)
    # def __init__(self):
    #     # 初始化时记录当前时间
    #     self.last_call_time = time.time()

    def generate_random(self):

        # 循环300次
        for i in range(30):
            a = random.randint(1, 100)
            print(i, a)
            # my_signal.emit(a)
        # return random.random()
