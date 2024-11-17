import os
import re

from PyQt5.QtWidgets import (
    QDialog,
    QMessageBox,
)

from PyQt5.QtGui import (
    QPixmap,
    QIcon,
)

from PyQt5.uic import loadUi

# second dialog for informatin display
class AddPersonDialog(QDialog):

    def __init__(self):
        """
        Initializer for the AddPersonDialog class.

        - Initializes the parent class (QDialog).
        - Loads the UI from a `.ui` file using PyQt's loadUi function.
        - Sets the window icon using a QIcon object with the path to an image file.

        - Connects button box signals (accepted/rejected) to respective methods:
            - `accept`: Handles data validation and closing the dialog on OK.
            - `reject`: Closes the dialog on Cancel.
        """

        super().__init__()
        # loading design - created in QtCreator
        loadUi("AddPerson.ui", self)

        self.setWindowIcon(QIcon('Party.png'))

        # button box created in Qt Designer
        # press button OK
        self.buttonBox.accepted.connect(self.accept)  
        # press butoon Cancel
        self.buttonBox.rejected.connect(self.reject)

    # press button OK
    def accept(self):  
        """
        Accept the data provided through the dialog and validate required fields.

        - Initializes an empty list `self.data` to store collected data.
        - Iterates through input fields (first name, last name, phone, email).
        - For each field:
            - Checks if the field is empty using `field.text()`.
            - If empty:
                - Displays a critical message box with the missing field name
                  using QMessageBox.critical.
                - Resets `self.data` to None to prevent partial data.
                - Returns to avoid further processing.
        - If all fields have data, appends the text from each field to `self.data`.
        - Calls the superclass `accept` method to close the dialog with OK.
        """
        dirname = os.path.dirname(__file__)
        stop_writing = os.path.join(dirname, 'stop_writing.png')

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

                messagebox = QMessageBox(QMessageBox.Information, "Error", f"<FONT COLOR='white'>You must provide a person's {label_text}", buttons=QMessageBox.Ok, parent=self)
                messagebox.setIconPixmap(QPixmap(stop_writing))
                messagebox.exec_()

                self.data = None  # Reset .data  
                return  
            
            if field == self.edit_email:
                email_regex = r'^[a-z0-9.+_-]+@[a-z0-9.-]+\.[a-z]{2,}$'
                if not re.match(email_regex, field.text()):
                    # Display error message for invalid email format
                    messagebox = QMessageBox(QMessageBox.Information, "Error", 
                                            "<FONT COLOR='white'>Invalid email format", 
                                            buttons=QMessageBox.Ok, parent=self)
                    messagebox.setIconPixmap(QPixmap(stop_writing))
                    messagebox.exec_()
                    
                    self.data = None  # Reset .data  
                    return 

            self.data.append(field.text())  
            print(self.data)

        super().accept()

    def get_error_messages(self):
        """
        Returns a list of all error messages encountered during unsuccessful form submission.

        :return: A list of strings containing the error messages.
        """
        error_messages = []
        for field in (self.edit_first_name, self.edit_last_name, self.edit_phone, self.edit_email):
            if not field.text():
                # Extract the field name from the objectName and capitalize the first letter
                field_name = field.objectName().split('_')[1].capitalize()
                error_messages.append(f"You must provide a person's {field_name}")
            elif field == self.edit_email:
                email_regex = r'^[a-z0-9.+_-]+@[a-z0-9.-]+\.[a-z]{2,}$'
                if not re.match(email_regex, field.text()):
                    error_messages.append("Invalid email format")
        return error_messages
