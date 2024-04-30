
import login_window
import sys
if __name__ == "__main__":
    app = login_window.QApplication(sys.argv)
    login = login_window.loginWidget()
    login.show()
    sys.exit(app.exec_())