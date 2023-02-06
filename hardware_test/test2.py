from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Delivery Bot")
        self.setStyleSheet("background-color: #013F78;")
        self.setFixedSize(QSize(1024, 600))
        # self.UiComponents()

        label = QLabel("Please enter passcode")
        label.setFont(QFont('Verdana', 40))
        label.setStyleSheet("color: white")

        line_edit = QLineEdit()
        line_edit.setMaxLength(10)

        line_edit.setPlaceholderText("Enter passcode")
        line_edit.setStyleSheet("background-color: white; padding: 10px;")

        button = QPushButton("Submit", self)
        button.setFixedSize(QSize(100, 30))
        button.setStyleSheet("border-radius : 10; background-color: white")
        button.clicked.connect(self.clickme)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def UiComponents(self):

        button = QPushButton("1", self)
        button.setFixedSize(QSize(98, 423))
        button.setStyleSheet("border-radius : 50;")

		# adding action to a button
        button.clicked.connect(self.clickme)

	# action method
    def clickme(self):


		# printing pressed
        print("pressed")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()



