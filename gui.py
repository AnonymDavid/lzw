import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from typing import List

from MainWindow import Ui_MainWindow
from lzw import encodeFull, decodeFull, encodeTable, decodeTable, ENCODED, FIELD


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btnEncode.clicked.connect(self.btnEncode_clicked)
        self.btnDecode.clicked.connect(self.btnDecode_clicked)

    def refreshTable(self, table:List[FIELD]):
        while (self.tblTable.rowCount() > 0):
            self.tblTable.removeRow(0)
        
        for i in range(len(table)):
            self.tblTable.insertRow(i)
            self.tblTable.setItem(i, 0, QTableWidgetItem(str(table[i].m)))
            self.tblTable.setItem(i, 1, QTableWidgetItem(str(table[i].n)))
            self.tblTable.setItem(i, 2, QTableWidgetItem(table[i].char))
            self.tblTable.setItem(i, 3, QTableWidgetItem(table[i].series))

    def btnEncode_clicked(self) -> None:
        text = self.txtText.toPlainText()
        
        if text == "":
            return
        
        table = encodeFull(text)

        self.refreshTable(table)

        result = encodeTable(table)

        self.txtDictionary.setText("".join([s for s in result.dictionary]))
        self.txtCode.setText("".join([f'{str(s)}, ' for s in result.code])[:-2])

        self.txtCompression.setText(f'{round(((len(table) - 1) / len(text)) * 100, 2)} %')


    def btnDecode_clicked(self) -> None:
        dictionary = self.txtDictionary.toPlainText()
        code = self.txtCode.toPlainText()
        
        if code == "" or dictionary == "":
            return
        
        dictionary_list = [x for x in dictionary]
        code_list = [int(x.strip()) for x in code.split(',')]

        table = decodeFull(ENCODED(dictionary_list, code_list))

        self.refreshTable(table)

        text = decodeTable(table)

        self.txtText.setText(text)

        self.txtCompression.setText(f'{round(((len(table) - 1) / len(text)) * 100, 2)} %')


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()