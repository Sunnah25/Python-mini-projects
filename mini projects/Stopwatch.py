import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.watch_label= QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.setGeometry(700, 300, 400, 200)



        vbox = QVBoxLayout()
        vbox.addWidget(self.watch_label)

        self.setLayout(vbox)
        self.watch_label.setAlignment(Qt.AlignCenter)


        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)


        vbox.addLayout(hbox)




        self.setStyleSheet("""
                           QPushButton, QLabel{
                                padding: 20px;
                           }

                           QPushButton{
                                font-size: 50px;
                           }
                           QLabel{
                                font-size: 120px;
                                background-color: rgba( 20, 120, 190, 0.4);
                                border-radius: 20px;
                           }
                           """)



        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.timer.timeout.connect(self.update_display)



    def start(self):
        self.timer.start(10)


    def stop(self):
        self.timer.stop()


    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.watch_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hours = time.hour()
        min = time.minute()
        second = time.second()
        millisec = time.msec() // 10

        return f"{hours:02}:{min:02}:{second:02}.{millisec:02}"


    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.watch_label.setText(self.format_time(self.time))


if __name__=="__main__":
    app = QApplication(sys.argv)
    stop_watch = StopWatch()
    stop_watch.show()
    sys.exit(app.exec_())