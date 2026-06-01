import sys
import psutil

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtCore import QTimer


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI System Optimizer")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.cpu_label = QLabel()
        self.ram_label = QLabel()

        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.ram_label)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)

        self.update_stats()

    def update_stats(self):

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory()

        self.cpu_label.setText(f"CPU Usage: {cpu}%")

        self.ram_label.setText(
            f"RAM Usage: {ram.percent}%"
        )


app = QApplication(sys.argv)

window = Dashboard()
window.show()

sys.exit(app.exec())