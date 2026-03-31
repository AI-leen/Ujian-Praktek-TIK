from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QApplication
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.div1=QWidget()
        label=QLabel("Create Account", self.div1)
        label.setAlignment(Qt.AlignCenter)
        self.div1.setStyleSheet("background-color: black; font: bold 30px; color:white;")
        self.div1.setFixedHeight(80)
        layoutdiv1=QVBoxLayout()
        layoutdiv1.addWidget(label)
        self.div1.setLayout(layoutdiv1)

        self.div2=QWidget()
        self.div2.setFixedHeight(60)
        layoutdiv2=QVBoxLayout()
        self.div2.setLayout(layoutdiv2)

        label1=QLabel("Username")
        label1.setStyleSheet("font-size: 15px;")
        label1.setContentsMargins(40, 0, 40, 0)

        label2=QLabel("Email")
        label2.setStyleSheet("font-size: 15px;")
        label2.setContentsMargins(40, 0, 40, 0)

        label3=QLabel("Password")
        label3.setStyleSheet("font-size: 15px;")
        label3.setContentsMargins(40, 0, 40, 0)

        label4=QLabel("Confirm Password")
        label4.setStyleSheet("font-size: 15px;")
        label4.setContentsMargins(40, 0, 40, 0)

        user=QLineEdit()
        user.setContentsMargins(40, 0, 40, 0)
        user.setFixedHeight(35)
        user.setStyleSheet("font-size: 20px;")
        password=QLineEdit()
        password.setContentsMargins(40, 0, 40, 0)
        password.setFixedHeight(35)
        password.setStyleSheet("font-size: 20px;")
        email=QLineEdit()
        email.setContentsMargins(40, 0, 40, 0)
        email.setFixedHeight(35)
        email.setStyleSheet("font-size: 20px;")
        conf=QLineEdit()
        conf.setContentsMargins(40, 0, 40, 0)
        conf.setFixedHeight(35)
        conf.setStyleSheet("font-size: 20px;")

        layout=QVBoxLayout()
        layout.addWidget(self.div1)
        layout.addWidget(label1)
        layout.addWidget(user)
        layout.addWidget(label2)
        layout.addWidget(email)
        layout.addWidget(label3)
        layout.addWidget(password)
        layout.addWidget(label4)
        layout.addWidget(conf)
        layout.addWidget(self.div2)
        layout.setContentsMargins(0, 0, 0, 0)

        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app=QApplication(sys.argv)
window=MainWindow()
window.setFixedSize(450,500)
window.setWindowTitle("User Registration")
window.show()
app.exec()
