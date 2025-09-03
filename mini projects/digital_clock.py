import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00",self)
        self.timer = QTimer(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)


        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)


        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size:120px;"
                                      "color: green;")
        self.setStyleSheet("background-color: black;")








        font_id = QFontDatabase.addApplicationFont(r"mini projects/ds_digital/DS-DIGIT.TTF")
        '''
           You tell PyQt: “Hey, here's a custom font file I want to use.”
            addApplicationFont() loads it into PyQt's font library.
            It gives you back an ID number (font_id) so you can find it later.
                👉 Real-world analogy: You bought a pack of special stickers for digital numbers and put them into your toolbox.
                The shopkeeper gives you a receipt ID (font_id) to identify that sticker pack.
        '''



        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        '''
           Every font file may have one or more font families inside (like bold, italic, etc.).
            applicationFontFamilies(font_id) returns a list of names.
            [0] just picks the first one.
        '''



        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)








        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()



    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__=="__main__":
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show()
    sys.exit(app.exec_())