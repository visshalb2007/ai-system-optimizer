import sys
import psutil

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem
)

from PyQt6.QtCore import QTimer


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI System Optimizer")
        self.setGeometry(100, 100, 700, 500)

        self.layout = QVBoxLayout()

        # Labels
        self.cpu_label = QLabel()
        self.ram_label = QLabel()

        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.ram_label)

        # Process Table
        self.process_table = QTableWidget()

        self.process_table.setColumnCount(3)

        self.process_table.setHorizontalHeaderLabels([
            "Process Name",
            "PID",
            "RAM %"
        ])

        self.layout.addWidget(self.process_table)

        self.setLayout(self.layout)

        # Timer
        self.timer = QTimer()

        self.timer.timeout.connect(self.update_stats)

        self.timer.start(2000)

        self.update_stats()

    def update_stats(self):

        # CPU + RAM
        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory()

        self.cpu_label.setText(
            f"CPU Usage: {cpu}%"
        )

        self.ram_label.setText(
            f"RAM Usage: {ram.percent}%"
        )

        # Process List
        processes = []

        for process in psutil.process_iter(
            ['pid', 'name', 'memory_percent']
        ):

            try:
                info = process.info

                processes.append([
                    info['name'],
                    info['pid'],
                    round(info['memory_percent'], 2)
                ])

            except:
                pass

        processes = sorted(
            processes,
            key=lambda x: x[2],
            reverse=True
        )

        top_processes = processes[:10]

        self.process_table.setRowCount(
            len(top_processes)
        )

        for row, process in enumerate(top_processes):

            self.process_table.setItem(
                row,
                0,
                QTableWidgetItem(str(process[0]))
            )

            self.process_table.setItem(
                row,
                1,
                QTableWidgetItem(str(process[1]))
            )

            self.process_table.setItem(
                row,
                2,
                QTableWidgetItem(str(process[2]))
            )


app = QApplication(sys.argv)

window = Dashboard()

window.show()

sys.exit(app.exec())