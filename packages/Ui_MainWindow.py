from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QWidget
from PySide2 import QtWidgets

import package.ui_behavior as uibehavior


class Ui_MainWindow(object):
    ed = ''
    behavior = uibehavior.Behavior()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(700, 550)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 200, 601, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")


        self.horizontalLayout.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(68, 75, QSizePolicy.Minimum, QSizePolicy.Expanding)


        self.horizontalLayout.addItem(self.verticalSpacer)

        self.encryptionChoiceBar = QComboBox(self.horizontalLayoutWidget)
        self.encryptionChoiceBar.setObjectName(u"encryptionChoiceBar")
        self.encryptionChoiceBar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                               "color: rgb(0,0,0);")
        self.encryptionChoiceBar.setFrame(True)
        self.encryptionChoiceBar.addItem('AES')
        self.encryptionChoiceBar.addItem('BlowFish')
        self.encryptionChoiceBar.addItem('Twofish')



        self.horizontalLayout.addWidget(self.encryptionChoiceBar)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(310, 460, 95, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.donePushButton = QPushButton(self.horizontalLayoutWidget_3)
        self.donePushButton.setObjectName(u"donePushButton")
        self.donePushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
                                          "background-color: rgb(255, 85, 0);")
        self.donePushButton.clicked.connect(lambda : self.behavior.done(self.encryptionChoiceBar.currentIndex(), self.passField.text()))

        self.horizontalLayout_3.addWidget(self.donePushButton)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(40, 350, 601, 71))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.horizontalLayoutWidget_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.uploadLabel = QLabel(self.frame)
        self.uploadLabel.setObjectName(u"uploadLabel")
        self.uploadLabel.setGeometry(QRect(0, 20, 121, 31))
        self.uploadPushButton = QPushButton(self.frame)
        self.uploadPushButton.setObjectName(u"uploadPushButton")
        self.uploadPushButton.setGeometry(QRect(150, 20, 81, 28))
        self.uploadPushButton.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.uploadPushButton.setAutoRepeat(False)
        self.uploadPushButton.setAutoExclusive(False)
        self.uploadPushButton.setAutoDefault(True)
        self.uploadPushButton.setFlat(False)
        self.uploadPushButton.clicked.connect(self.browse)

        self.horizontalLayout_6.addWidget(self.frame)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(40, 140, 481, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.horizontalLayoutWidget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.encRadioButton = QRadioButton(self.widget_2)
        self.encRadioButton.setObjectName(u"encRadioButton")
        self.encRadioButton.setGeometry(QRect(0, 10, 88, 21))
        self.encRadioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.encRadioButton.clicked.connect(self.behavior.encrypt)
        self.decRadioButton = QRadioButton(self.widget_2)
        self.decRadioButton.setObjectName(u"decRadioButton")
        self.decRadioButton.setGeometry(QRect(250, 10, 112, 21))
        self.decRadioButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.decRadioButton.clicked.connect(self.behavior.decrypt)

        self.horizontalLayout_4.addWidget(self.widget_2)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(120, 10, 321, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.verticalLayoutWidget_2)
        self.widget_21.setObjectName(u"widget_21")
        self.Title = QLabel(self.widget_21)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 161, 65))
        self.Title.setStyleSheet(u"font: 26pt \"Broadway\";\n"
                                 "font: 24pt \"Niagara Engraved\";")
        self.Title2 = QLabel(self.widget_21)
        self.Title2.setObjectName(u"Title2")
        self.Title2.setGeometry(QRect(10, 80, 161, 21))

        self.verticalLayout.addWidget(self.widget_21)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 81, 81))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetPhoto = QWidget(self.gridLayoutWidget)
        self.widgetPhoto.setObjectName(u"widgetPhoto")
        self.photo = QLabel(self.widgetPhoto)
        self.photo.setObjectName(u"photo")
        self.photo.setGeometry(QRect(0, 0, 81, 81))
        self.photo.setStyleSheet(
            u"image: url(designer/icon/logo.png);")

        self.gridLayout.addWidget(self.widgetPhoto, 0, 0, 1, 1)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(40, 270, 601, 61))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.horizontalLayoutWidget_2)
        self.widget_22.setObjectName(u"widget_22")
        self.passLabel = QLabel(self.widget_22)
        self.passLabel.setObjectName(u"passLabel")
        self.passLabel.setGeometry(QRect(0, 10, 91, 31))
        self.passField = QLineEdit(self.widget_22)
        self.passField.setObjectName(u"passField")
        self.passField.setEnabled(True)
        self.passField.setGeometry(QRect(120, 10, 311, 31))
        self.passField.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.passField.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.widget_22)

        self.horizontalLayoutWidget_6 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(40, 430, 601, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.horizontalLayoutWidget_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.checkBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.uploadPushButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CryptoFly", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:10pt; "
                                                        u"color:#ffffff;\">Select the encryption/decryption of your "
                                                        u"choice</span></p></body></html>",
                                                        None))
        self.donePushButton.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.uploadLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" "
                                                                          u"font-size:10pt; color:#ffffff;\">Upload "
                                                                          u"the file</span></p></body></html>", None))
        self.uploadPushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.encRadioButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decRadioButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" "
                                                                    u"font-size:36pt; font-weight:600; "
                                                                    u"color:#ff5500;\">CryptoFly</span></p></body></html>",
                                                      None))
        self.Title2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" "
                                                                     u"font-size:7pt; font-weight:600; "
                                                                     u"color:#ffffff;\">Encrypt and decrypt "
                                                                     u"files</span></p></body></html>", None))
        self.photo.setText("")
        self.passLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" "
                                                                        u"font-size:10pt; "
                                                                        u"color:#ffffff;\">Password</span></p></body></html>",
                                                          None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Remember these as default for future "
                                                                       u"operations", None))

    # retranslateUi
    @Slot()
    def browse(self):
        filename = QFileDialog.getOpenFileName()
        self.behavior.browse(filename[0])