import sys
import time
from datetime import datetime, timedelta
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QWidget
)
from PySide6.QtGui import QFont, QColor, QPalette
from PySide6.QtCore import Qt, QTimer, Signal, Slot
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl

class ClockApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Professional Clock App")
        self.setGeometry(100, 100, 360, 320)  # Increased height to accommodate new buttons

        # Set up the main layout
        main_layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)

        # Set cursive font
        cursive_font = QFont("Brush Script MT", 12)
        self.setFont(cursive_font)

        # Clock section
        self.clock_label = QLabel()
        self.clock_label.setFont(QFont("Brush Script MT", 43))
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                background-color: #333333;
                padding: 12px;
                border-radius: 6px;
            }
        """)

        # Stopwatch section
        self.stopwatch_label = QLabel("00:00:00")
        self.stopwatch_label.setFont(QFont("Brush Script MT", 29))
        self.stopwatch_label.setAlignment(Qt.AlignCenter)
        self.stopwatch_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                background-color: #555555;
                padding: 6px;
                border-radius: 3px;
            }
        """)
        
        button_style = """
            QPushButton {
                color: white;
                padding: 6px 12px;
                border: none;
                border-radius: 3px;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        
        self.stopwatch_start_button = QPushButton("Start")
        self.stopwatch_start_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #4CAF50;"))
        
        self.stopwatch_stop_button = QPushButton("Stop")
        self.stopwatch_stop_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #F44336;"))
        
        self.stopwatch_reset_button = QPushButton("Reset")
        self.stopwatch_reset_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #2196F3;"))

        stopwatch_layout = QHBoxLayout()
        stopwatch_layout.addWidget(self.stopwatch_label)
        stopwatch_layout.addWidget(self.stopwatch_start_button)
        stopwatch_layout.addWidget(self.stopwatch_stop_button)
        stopwatch_layout.addWidget(self.stopwatch_reset_button)

        # Timer section
        self.timer_label = QLabel("00:00:00")
        self.timer_label.setFont(QFont("Brush Script MT", 29))
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                background-color: #555555;
                padding: 6px;
                border-radius: 3px;
            }
        """)
        
        self.timer_5min_button = QPushButton("+5 min")
        self.timer_10min_button = QPushButton("+10 min")
        self.timer_20min_button = QPushButton("+20 min")
        self.timer_decrease_button = QPushButton("-1 min")
        
        for button in [self.timer_5min_button, self.timer_10min_button, self.timer_20min_button, self.timer_decrease_button]:
            button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #FF9800;"))
        
        self.timer_start_button = QPushButton("Start Timer")
        self.timer_start_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #4CAF50;"))
        
        self.timer_stop_button = QPushButton("Stop Timer")
        self.timer_stop_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #F44336;"))

        timer_button_layout = QHBoxLayout()
        timer_button_layout.addWidget(self.timer_5min_button)
        timer_button_layout.addWidget(self.timer_10min_button)
        timer_button_layout.addWidget(self.timer_20min_button)
        timer_button_layout.addWidget(self.timer_decrease_button)
        
        timer_control_layout = QHBoxLayout()
        timer_control_layout.addWidget(self.timer_start_button)
        timer_control_layout.addWidget(self.timer_stop_button)

        # Alarm section
        self.alarm_time_edit = QLineEdit()
        self.alarm_time_edit.setPlaceholderText("HH:MM:SS")
        self.alarm_time_edit.setFont(QFont("Brush Script MT", 14))
        self.alarm_time_edit.setAlignment(Qt.AlignCenter)
        self.alarm_time_edit.setStyleSheet("""
            QLineEdit {
                background-color: #FFFFFF;
                color: #333333;
                padding: 6px;
                border: 1px solid #555555;
                border-radius: 3px;
            }
        """)
        self.alarm_set_button = QPushButton("Set Alarm")
        self.alarm_set_button.setStyleSheet(button_style.replace("background-color: #45a049;", "background-color: #9C27B0;"))
        
        self.alarm_label = QLabel("Alarm not set")
        self.alarm_label.setFont(QFont("Brush Script MT", 11))
        self.alarm_label.setAlignment(Qt.AlignCenter)
        self.alarm_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                background-color: #555555;
                padding: 6px;
                border-radius: 3px;
            }
        """)
        self.alarm_checkbox = QCheckBox("Alarm Enabled")
        self.alarm_checkbox.setStyleSheet("""
            QCheckBox {
                color: #FFFFFF;
                font-size: 10px;
            }
            QCheckBox::indicator {
                width: 12px;
                height: 12px;
            }
            QCheckBox::indicator:unchecked {
                border: 1px solid #FFFFFF;
                background-color: #333333;
            }
            QCheckBox::indicator:checked {
                border: 1px solid #FFFFFF;
                background-color: #4CAF50;
                image: url(data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'%3E%3C/polyline%3E%3C/svg%3E);
            }
        """)

        alarm_layout = QHBoxLayout()
        alarm_layout.addWidget(self.alarm_time_edit)
        alarm_layout.addWidget(self.alarm_set_button)
        alarm_layout.addWidget(self.alarm_checkbox)

        # Add sections to the main layout
        main_layout.addWidget(self.clock_label)
        main_layout.addLayout(stopwatch_layout)
        main_layout.addWidget(self.timer_label)
        main_layout.addLayout(timer_button_layout)
        main_layout.addLayout(timer_control_layout)
        main_layout.addLayout(alarm_layout)
        main_layout.addWidget(self.alarm_label)

        # Connect signals and slots
        self.stopwatch_start_button.clicked.connect(self.start_stopwatch)
        self.stopwatch_stop_button.clicked.connect(self.stop_stopwatch)
        self.stopwatch_reset_button.clicked.connect(self.reset_stopwatch)
        self.timer_5min_button.clicked.connect(lambda: self.adjust_timer(5))
        self.timer_10min_button.clicked.connect(lambda: self.adjust_timer(10))
        self.timer_20min_button.clicked.connect(lambda: self.adjust_timer(20))
        self.timer_decrease_button.clicked.connect(lambda: self.adjust_timer(-1))
        self.timer_start_button.clicked.connect(self.start_timer)
        self.timer_stop_button.clicked.connect(self.stop_timer)
        self.alarm_set_button.clicked.connect(self.set_alarm)
        self.alarm_checkbox.toggled.connect(self.enable_alarm)

        # Initialize timers and variables
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)

        self.stopwatch_timer = QTimer()
        self.stopwatch_timer.timeout.connect(self.update_stopwatch)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.stopwatch_running = False
        self.stopwatch_elapsed = timedelta()
        self.timer_remaining = timedelta()
        self.alarm_set = False
        self.alarm_time = None

        # Set up sound effects
        self.alarm_sound = QSoundEffect()
        self.alarm_sound.setSource(QUrl.fromLocalFile("alarm_tone.mp3"))
        self.timer_sound = QSoundEffect()
        self.timer_sound.setSource(QUrl.fromLocalFile("timer_tone.mp3"))

        # Set the application palette
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(51, 51, 51))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.setText(current_time)

    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_start_time = datetime.now() - self.stopwatch_elapsed
            self.stopwatch_timer.start(100)
            self.stopwatch_running = True

    def stop_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_timer.stop()
            self.stopwatch_running = False

    def reset_stopwatch(self):
        self.stopwatch_timer.stop()
        self.stopwatch_running = False
        self.stopwatch_elapsed = timedelta()
        self.update_stopwatch_display()

    def update_stopwatch(self):
        self.stopwatch_elapsed = datetime.now() - self.stopwatch_start_time
        self.update_stopwatch_display()

    def update_stopwatch_display(self):
        total_seconds = int(self.stopwatch_elapsed.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        self.stopwatch_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def adjust_timer(self, minutes):
        self.timer_remaining += timedelta(minutes=minutes)
        if self.timer_remaining < timedelta():
            self.timer_remaining = timedelta()
        self.update_timer_display()

    def start_timer(self):
        if self.timer_remaining > timedelta():
            self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def update_timer(self):
        if self.timer_remaining > timedelta():
            self.timer_remaining -= timedelta(seconds=1)
            self.update_timer_display()
        else:
            self.timer.stop()
            self.timer_sound.play()

    def update_timer_display(self):
        total_seconds = int(self.timer_remaining.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def set_alarm(self):
        alarm_time_str = self.alarm_time_edit.text()
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S")
            self.alarm_time = alarm_time
            self.alarm_label.setText(f"Alarm set for {alarm_time_str}")
            self.alarm_set = True
            self.alarm_checkbox.setChecked(True)
        except ValueError:
            self.alarm_label.setText("Invalid time format")

    def enable_alarm(self, enabled):
        self.alarm_set = enabled

    def check_alarm(self):
        if self.alarm_set and self.alarm_time:
            current_time = datetime.now()
            if current_time.hour == self.alarm_time.hour and current_time.minute == self.alarm_time.minute and current_time.second == self.alarm_time.second:
                self.alarm_label.setText("Alarm triggered!")
                self.alarm_label.setStyleSheet("color: red;")
                self.alarm_sound.play()
            else:
                self.alarm_label.setStyleSheet("color: white;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock_app = ClockApp()
    clock_app.show()
    sys.exit(app.exec())
