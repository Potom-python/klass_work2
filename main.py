import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QMainWindow):
    def __init__(self):
        super(CircleDrawer, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, d) in self.circles:
            painter.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())