import sys
import Database
import TableModel

from pathlib import Path

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QDialog,
    QMainWindow,
    QMessageBox,
    QTableView

)

from PyQt5.QtGui import (
    QColor,
    QPixmap,
    QIcon,
    QRegExpValidator,
    QValidator,
)

from PyQt5.QtWidgets import QApplication  

from PyQt5 import QtCore

from PyQt5.uic import loadUi



class PartyWindow(QMainWindow):  
    """Main Window."""  
  
    def __init__(self, parent=None):  
        """Initializer."""  
        super().__init__(parent)
        self.personModel = TableModel.PersonModel()  
        loadUi("PartyList.ui", self)

        self.table_party_list.setModel(self.personModel.model)
        self.table_party_list.setSelectionBehavior(QAbstractItemView.SelectRows) 
        self.table_party_list.horizontalHeader().setStyleSheet('QHeaderView::section {background-color: rgb(69, 86, 206); color: rgb(250, 250, 250); font-weight: bold;} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')
        self.table_party_list.verticalHeader().setStyleSheet('QHeaderView::section {background-color: rgb(60, 60, 60); color: rgb(250, 210, 210); font-size: 6} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

        self.button_delete.clicked.connect(lambda: self.deletePerson())
        self.button_close.clicked.connect(app.closeAllWindows)


    def deletePerson(self):  
        """Delete the selected contact from the database."""  
        row = self.table_party_list.currentIndex().row()  
        if row < 0:  
            return  

        messageBox = QMessageBox.warning(self, "Warning!", "<FONT COLOR='white'>Really do you want to delete the selected person?", QMessageBox.Ok | QMessageBox.Cancel)  
  
        if messageBox == QMessageBox.Ok:
            self.personModel.deletePerson(row) 

app = QApplication(sys.argv)
connection = Database.createConnection("party_list.db")
mainwindow = PartyWindow()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('PARTY LIST')
widget.addWidget(mainwindow)
widget.show()
app.setStyleSheet(Path('styles.qss').read_text())
app.exec()