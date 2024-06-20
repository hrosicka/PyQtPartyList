"""This module provides a model to manage the contacts table in a Qt application.

It uses PyQt's QSqlTableModel to interact with the database and provides methods
for CRUD (Create, Read, Update, Delete) operations on the contacts data.
"""
  
from PyQt5.QtCore import Qt  
from PyQt5.QtSql import QSqlTableModel  
  
class PersonModel:  
    def __init__(self):
        """
        Initializes the model by creating a QSqlTableModel instance
        and setting it up to manage the "person" table.
        """
        self.model = self._createModel()  

    @staticmethod  
    def _createModel():  
        """
        Creates and configures a QSqlTableModel instance for the "person" table.

        - Sets the table name to "person".
        - Sets the edit strategy to OnFieldChange for immediate updates.
        - Executes a select query to retrieve initial data.
        - Sets the column headers using a provided list.

        Returns:
            The configured QSqlTableModel instance.
        """  
        tableModel = QSqlTableModel()  
        tableModel.setTable("person")  
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)  
        tableModel.select()  
        headers = ("ID", "First Name", "Last Name", "Phone", "Email")  
        for columnIndex, header in enumerate(headers):  
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)  
        return tableModel

    def deletePerson(self, row):
        """
        Removes a person from the database at the specified row index.

        - Removes the row from the QSqlTableModel.
        - Submits all changes to the database.
        - Refreshes the model data by executing a select query.

        Args:
            row (int): The index of the row to be deleted.
        """
        self.model.removeRow(row)  
        self.model.submitAll()  
        self.model.select()

    def deletePeople(self):  
        """
        Removes all people from the database.

        - Iterates through all rows in reverse order (to avoid index issues).
        - Removes each row from the QSqlTableModel.
        - Submits all changes to the database.
        - Refreshes the model data by executing a select query.
        """  
        raw = self.model.rowCount()
        while (raw >= 0):
            self.model.removeRow(raw)
            raw = raw - 1
        self.model.submitAll()  
        self.model.select()

    def addPerson(self, data):  
        """
        Adds a new person to the database.

        - Gets the current number of rows (for insertion position).
        - Inserts a new row at the end of the table.
        - Iterates through the provided data list and sets the values
          in the corresponding columns of the new row.
        - Submits all changes to the database.
        - Refreshes the model data by executing a select query.

        Args:
            data (list): A list containing the person's data for each column.
        """
        rows = self.model.rowCount()  
        self.model.insertRows(rows, 1)  
        for column, field in enumerate(data):  
            self.model.setData(self.model.index(rows, column + 1), field)  
        self.model.submitAll()  
        self.model.select()  
    

    def get_all_people(self):
        """
        Retrieves all people data from the database and returns them as a list of dictionaries.

        - Checks if the select query was successful.
        - Gets the number of columns for iteration.
        - Iterates through all rows and creates a dictionary for each person's data.
        - Uses column headers as dictionary keys (assuming consistent data structure).
        - Appends each person's data dictionary to a list and returns it.

        Returns:
            list: A list containing dictionaries representing all people data.
        """
        all_people = []
        if self.model.select():
            # Get column count (assuming consistent data structure)
            column_count = self.model.columnCount()

            # Loop through all rows
            for row in range(self.model.rowCount()):
                person_data = {}
                for col in range(column_count):
                    # Access data using index and Qt.DisplayRole
                    value = self.model.data(self.model.index(row, col), Qt.DisplayRole)
                    # Use column headers as dictionary keys (assuming they exist)
                    headers = ("ID", "First Name", "Last Name", "Phone", "Email")
                    if col < len(headers):
                        person_data[headers[col]] = value
                all_people.append(person_data)

        return all_people
    

    def get_current_row(self, row):
        """Retrieves the data from the currently selected row as a dictionary.

        Returns:
            A dictionary containing the data from the selected row, or None if no row is selected.
        """
        column_count = self.model.columnCount()

        person_data = {}
        for col in range(column_count):
            # Access data using index and Qt.DisplayRole
            value = self.model.data(self.model.index(row, col), Qt.DisplayRole)
            # Use column headers as dictionary keys (assuming they exist)
            headers = ("ID", "First Name", "Last Name", "Phone", "Email")
            if col < len(headers):
                person_data[headers[col]] = value

        return person_data