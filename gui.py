import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

from MainWindow import Ui_MainWindow
from lzw import encode, decode, ENCODED


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btnEncode.clicked.connect(self.btnEncode_clicked)
        self.btnDecode.clicked.connect(self.btnDecode_clicked)

    def btnEncode_clicked(self) -> None:
        text = self.txtText.toPlainText()
        
        if text == "":
            print("b")
            return
        
        result = encode(text)

        self.txtDictionary.setText("".join([s for s in result.dictionary]))
        self.txtCode.setText("".join([f'{str(s)}, ' for s in result.code])[:-2])


    def btnDecode_clicked(self) -> None:
        dictionary = self.txtDictionary.toPlainText()
        code = self.txtCode.toPlainText()
        
        if code == "" or dictionary == "":
            print("b")
            return
        
        dictionary_list = [x for x in dictionary]
        code_list = [int(x.strip()) for x in code.split(',')]

        self.txtText.setText(decode(ENCODED(dictionary_list, code_list)))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()