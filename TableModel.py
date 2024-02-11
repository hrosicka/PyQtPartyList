"""This module provides a model to manage the contacts table."""  
  
from PyQt5.QtCore import Qt  
from PyQt5.QtSql import QSqlTableModel  
  
class PersonModel:  
    def __init__(self):  
        self.model = self._createModel()  
 
    @staticmethod  
    def _createModel():  
        """Create and set up the model."""  
        tableModel = QSqlTableModel()  
        tableModel.setTable("person")  
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)  
        tableModel.select()  
        headers = ("ID", "First Name", "Last Name", "Phone", "Email")  
        for columnIndex, header in enumerate(headers):  
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)  
        return tableModel
    

    def deletePerson(self, row):  
        """Remove a person from the database."""  
        self.model.removeRow(row)  
        self.model.submitAll()  
        self.model.select()


        

    