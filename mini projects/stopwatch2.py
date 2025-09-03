import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("00:00:00.00", self)
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.start_btn = QPushButton("Start", self)
        self.stop_btn = QPushButton("Stop", self)
        self.reset_btn = QPushButton("Reset", self)
        self.lap_btn = QPushButton("Lap", self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.setGeometry(700, 300, 400, 200)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.time_label.setAlignment(Qt.AlignCenter)


        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)
        hbox.addWidget(self.stop_btn)
        hbox.addWidget(self.reset_btn)
        hbox.addWidget(self.lap_btn)

        vbox.addLayout(hbox)
        self.setLayout(vbox)





        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.reset_btn.clicked.connect(self.reset)
        self.lap_btn.clicked.connect(self.lap)

        self.timer.timeout.connect(self.update_display)


    def start(self):
        self.timer.start(10)


    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()

        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))


    def lap(self):
        hour = self.time.hour()
        min = self.time.minute()
        second = self.time.second()
        milisec = self.time.msec() // 10



        print(f"{hour:02}:{min:02}:{second:02}.{milisec:02}")


    def format_time(self, time):
        hour = time.hour()
        min = time.minute()
        second = time.second()
        milisec = time.msec() // 10



        return f"{hour:02}:{min:02}:{second:02}.{milisec:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))        





if __name__=="__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())