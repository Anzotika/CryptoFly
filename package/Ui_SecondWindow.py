from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(460, 150)
        SecondWindow.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"background-color: rgb(0, 0, 0);")
        SecondWindow.setIconSize(QSize(10, 10))
        SecondWindow.setAnimated(True)
        self.centralwidget = QWidget(SecondWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.encDecData = QLabel(self.centralwidget)
        self.encDecData.setObjectName(u"encDecData")
        self.encDecData.setGeometry(QRect(70, 60, 300, 30))
        self.icon = QLabel(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(0, 10, 61, 41))
        self.icon.setStyleSheet(u"image: url(:/newPrefix/logo.png);")
        self.checkmark = QLabel(self.centralwidget)
        self.checkmark.setObjectName(u"checkmark")
        self.checkmark.setGeometry(QRect(360, 50, 51, 31))
        self.checkmark.setStyleSheet(u"image: url(:/newPrefix/check-mark.png);")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SecondWindow)
        self.statusbar.setObjectName(u"statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)

        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, SecondWindow):
        SecondWindow.setWindowTitle(QCoreApplication.translate("SecondWindow", u"CryptoFly", None))
        self.encDecData.setText(QCoreApplication.translate("SecondWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Your file has been encrypted/decrypted</span></p></body></html>", None))
        self.icon.setText("")
        self.checkmark.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())