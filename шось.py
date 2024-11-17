from PyQt5.QtCore import Qt 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Кредитна картка')
        self.setGeometry(100, 100, 400, 200)

        # Створення елементів інтерфейсу
        self.layout = QVBoxLayout()
        
        self.label = QLabel('Введіть номер кредитної карти будь-ласочка')
        self.layout.addWidget(self.label)
        
        self.inputField = QLineEdit()
        self.layout.addWidget(self.inputField)
        
        self.submitButton = QPushButton('Показати число')
        self.submitButton.clicked.connect(self.show_number)
        self.layout.addWidget(self.submitButton)
        
        self.resultLabel = QLabel('')
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

    def show_number(self):
        input_text = self.inputField.text()
        
        # Перевірка, чи введене число є 14-значним
        if len(input_text) == 14 and input_text.isdigit():
            self.resultLabel.setText(f'Номер кредитної карти яку ви ввели: {input_text}')
        else:
            self.resultLabel.setText('Будь ласка, введіть коректний номер кредитної карти')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

