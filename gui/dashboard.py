import sys
import psutil

from collections import deque

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

from PyQt6.QtCore import Qt, QTimer

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI System Optimizer")

        self.setGeometry(100, 100, 1200, 800)

        self.setStyleSheet("""

            QWidget {
                background-color: #0f1117;
                color: white;
                font-family: Segoe UI;
            }

            QLabel {
                color: white;
            }

            QFrame {
                background-color: #1a1d26;
                border-radius: 12px;
            }

            QTableWidget {
                background-color: #1a1d26;
                border-radius: 10px;
                gridline-color: #2a2d35;
                border: none;
            }

            QHeaderView::section {
                background-color: #242936;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }

        """)

        # MAIN LAYOUT
        self.main_layout = QVBoxLayout()

        self.main_layout.setContentsMargins(20, 20, 20, 20)

        self.main_layout.setSpacing(20)

        # TITLE
        self.title = QLabel("AI SYSTEM OPTIMIZER")

        self.title.setStyleSheet("""

            font-size: 30px;
            font-weight: bold;

        """)

        self.main_layout.addWidget(self.title)

        # TOP CARDS
        self.cards_layout = QHBoxLayout()

        self.cpu_card = self.create_card("CPU Usage")
        self.ram_card = self.create_card("RAM Usage")
        self.alert_card = self.create_card("System Status")

        self.cards_layout.addWidget(self.cpu_card)
        self.cards_layout.addWidget(self.ram_card)
        self.cards_layout.addWidget(self.alert_card)

        self.main_layout.addLayout(self.cards_layout)

        # GRAPH PANEL
        self.graph_frame = QFrame()

        self.graph_layout = QVBoxLayout()

        self.figure = Figure(facecolor="#1a1d26")

        self.canvas = FigureCanvas(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.cpu_data = deque(maxlen=30)
        self.ram_data = deque(maxlen=30)

        self.graph_layout.addWidget(self.canvas)

        self.graph_frame.setLayout(self.graph_layout)

        self.main_layout.addWidget(self.graph_frame)

        # PROCESS TABLE
        self.process_table = QTableWidget()

        self.process_table.setColumnCount(3)

        self.process_table.setHorizontalHeaderLabels([
            "Process Name",
            "PID",
            "RAM %"
        ])

        self.process_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.process_table.setMinimumHeight(250)

        self.main_layout.addWidget(self.process_table)

        self.setLayout(self.main_layout)

        # TIMER
        self.timer = QTimer()

        self.timer.timeout.connect(self.update_stats)

        self.timer.start(2000)

        self.update_stats()

    def create_card(self, title):

        card = QFrame()

        layout = QVBoxLayout()

        title_label = QLabel(title)

        title_label.setStyleSheet("""
            font-size: 16px;
            color: #bbbbbb;
        """)

        value_label = QLabel("0")

        value_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title_label)

        layout.addWidget(value_label)

        card.setLayout(layout)

        card.value_label = value_label

        card.setMinimumHeight(120)

        return card

    def update_stats(self):

        # CPU + RAM
        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory()

        self.cpu_card.value_label.setText(f"{cpu}%")

        self.ram_card.value_label.setText(f"{ram.percent}%")

        # ALERT STATUS
        if ram.percent > 85:
            status = "HIGH RAM USAGE"
        else:
            status = "SYSTEM NORMAL"

        self.alert_card.value_label.setText(status)

        # GRAPH DATA
        self.cpu_data.append(cpu)

        self.ram_data.append(ram.percent)

        self.ax.clear()

        self.ax.plot(self.cpu_data, linewidth=3)

        self.ax.plot(self.ram_data, linewidth=3)

        self.ax.set_ylim(0, 100)

        self.ax.set_facecolor("#1a1d26")

        self.figure.patch.set_facecolor("#1a1d26")

        self.ax.tick_params(colors="white")

        self.ax.spines['bottom'].set_color("white")
        self.ax.spines['left'].set_color("white")

        self.ax.set_title(
            "Live System Performance",
            color="white",
            fontsize=14
        )

        self.ax.legend(
            ["CPU %", "RAM %"]
        )

        self.canvas.draw()

        # PROCESS TABLE
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