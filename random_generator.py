import random
from PySide6.QtCore import QObject, Signal, Slot
import time

class RandomGenerator(QObject):
    my_signal = Signal(int)

    def __init__(self):
        super().__init__()

    @Slot()
    def generate_random(self):
        for i in range(30):
            a = random.randint(1, 100)
            print(f"生成的随机数: {a}")
            self.my_signal.emit(a)  # 发出信号
            time.sleep(0.1)  # 休眠1秒
