import package.Ui_MainWindow as window
import sys

if __name__ == "__main__":
    app = window.QtWidgets.QApplication(sys.argv)
    MainWindow = window.QtWidgets.QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())