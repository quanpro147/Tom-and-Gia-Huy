import sys
from PyQt5 import QtWidgets
from UI.user_interface.login import LoginWidget

def GiaoDien():
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = LoginWidget()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    print(123)
    sys.exit(app.exec_())
    print(123)

#GiaoDien()