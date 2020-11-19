import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from random import randint
from PIL import Image, ImageDraw
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.cir = []
        self.pushButton = QPushButton(self)
        self.pushButton.move(10, 10)
        self.pushButton.setText('Запустить')
        self.pushButton.clicked.connect(self.run)

    def initUI(self):
        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle('Случайные окружности')
    
    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.cir.append([randint(0, 800), randint(0, 800), randint(10, 100)])
            for i in self.cir:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                qp.setPen(QColor(r, g, b))
                qp.drawEllipse(i[0], i[1], i[2], i[2]) 

        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())