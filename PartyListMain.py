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
        self.table_party_list.verticalHeader().setStyleSheet('QHeaderView::section {background-color: rgb(60, 60, 60); color: rgb(200, 250, 200); font-size: 6} QToolTip { background-color: #8ad4ff; color: black; border: #8ad4ff solid 1px}')

        self.button_new.clicked.connect(self.openAddPerson)  
        self.button_delete.clicked.connect(lambda: self.deletePerson())
        self.button_delete_all.clicked.connect(lambda: self.deletePeople())
        self.button_close.clicked.connect(app.closeAllWindows)


    def deletePerson(self):  
        """Delete the selected person from the database."""  
        row = self.table_party_list.currentIndex().row()  
        if row < 0:  
            return  

        messageBox = QMessageBox.warning(self, "Warning!", "<FONT COLOR='white'>Really do you want to delete the selected person?", QMessageBox.Ok | QMessageBox.Cancel)  
  
        if messageBox == QMessageBox.Ok:
            self.personModel.deletePerson(row) 

    def deletePeople(self):  
        """Delete all people from the database."""  
      
        messageBox = QMessageBox.warning(self, "Warning!", "<FONT COLOR='white'>Really do you want to delete all people?", QMessageBox.Ok | QMessageBox.Cancel)  
  
        if messageBox == QMessageBox.Ok:
            self.personModel.deletePeople() 

    def openAddPerson(self):  
        """Open the Add Contact dialog."""  
        dialog = AddPersonDialog()  
        if dialog.exec() == QDialog.Accepted:  
            self.personModel.addPerson(dialog.data)  
            self.table_party_list.resizeColumnsToContents()  


# second dialog for informatin display
class AddPersonDialog(QDialog):

    def __init__(self):
        super().__init__()
        # loading design - created in QtCreator
        loadUi("AddPerson.ui", self)

        # button box created in Qt Designer
        # press button OK
        self.buttonBox.accepted.connect(self.accept)  
        # press butoon Cancel
        self.buttonBox.rejected.connect(self.reject)

    # press button OK
    def accept(self):  
        """Accept the data provided through the dialog."""  
        self.data = []  
        for field in (self.edit_first_name, self.edit_last_name, self.edit_phone, self.edit_email):  
            if not field.text():  
                if field == self.edit_first_name:
                    label_text = self.label_first_name.text()
                elif field == self.edit_last_name:
                    label_text = self.label_last_name.text()
                elif field == self.edit_phone:
                    label_text = self.label_phone.text()
                elif field == self.edit_email:
                    label_text = self.label_email.text()


                QMessageBox.critical(  
                    self,  
                    "Error!",  
                    f"<FONT COLOR='white'>You must provide a person's {label_text}",  
                )  
                self.data = None  # Reset .data  
                return  

            self.data.append(field.text())  
            print(self.data)

        super().accept()  


app = QApplication(sys.argv)
connection = Database.createConnection("party_list.db")
mainwindow = PartyWindow()
widget = QtWidgets.QStackedWidget()
widget.setWindowTitle('PARTY LIST')
widget.addWidget(mainwindow)
widget.show()
app.setStyleSheet(Path('styles.qss').read_text())
app.exec()