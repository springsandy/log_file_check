import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDateTime

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString('yyyy년 MM월 dd일 hh:mm:ss'))

        self.setWindowTitle('log 확인하기')
        self.resize(400, 200)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())