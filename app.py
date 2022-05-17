import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QSizePolicy,
)


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.msg_error = 'Conta inválida.'
        self.display_style = \
            '* {background-color: #FFF; color: black; font-size: 30px; padding-left: 15px;}'
        self.equal_style = "background-color: #52bee7; font-weight: bold"
        self.backspace_style = "background-color: #52e781; font-weight: bold;"
        self.c_style = "background: rgb(236,86,86); font-weight: bold;"

        self.buttons = buttons = [
            ['7', '8', '9', '+', ["C", self.reset_display, self.c_style]],
            ['4', '5', '6', '-', ['<-', self.backspace , self.backspace_style]],
            ['1', '2', '3', '%', '.'],
            ['(', '0', ')', '*', ['=', self.equal, self.equal_style]],
        ]

        self.setWindowTitle('Calculadora Python')
        self.setFixedSize(400, 400)
        self.cw = QWidget(parent)
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            self.display_style
        )
        self.display.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        self.add_buttons(buttons)

        self.setCentralWidget(self.cw)

    def add_button(self, btn, row, column, rowspan, colspan, func=None, style=None):
        self.grid.addWidget(btn, row, column, rowspan, colspan)
        if style:
            btn.setStyleSheet(style)
        if func:
            self.listen_event(btn, func)
        else:
            self.listen_event(btn, lambda: self.display.setText(
                self.display.text() + btn.text()))
        btn.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Expanding)

    def backspace(self):
        self.display.setText(self.display.text()[:-1])

    def add_buttons(self, button_list: list):
        for row, buttons_list in enumerate(button_list, 1):
            for column, button in enumerate(buttons_list):
                if type(button) == list:
                    value, func, style = button 
                    self.add_button(
                        QPushButton(value), row, column, 1, 1, func, style)
                else:
                    self.add_button(QPushButton(button), row, column, 1, 1)

    def listen_event(self, btn, func):
        btn.clicked.connect(
            func
        )

    def equal(self):
        try:
            value = self.display.text()
            if value.count('%') > 0:
                value = value.replace('%', '/')
            if value.count('^') > 0:
                value = value.replace('^', '**')
            self.display.setText(
                str(eval(value))
            )
        except Exception:
            value = self.display.text()
            self.display.setText(self.msg_error)
    
    def reset_display(self):
        self.display.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
