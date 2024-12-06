import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from UI import Ui_MainWindow

class CircleDrawer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        d = random.randint(20, 100)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.circles.append((x, y, d, (r, g, b)))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for (x, y, d, color) in self.circles:
            painter.setBrush(QColor(*color))
            painter.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())