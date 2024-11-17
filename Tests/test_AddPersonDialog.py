import unittest
from PyQt5.QtWidgets import QApplication  # Import QApplication
import sys

# Setting the path to the module to be tested
sys.path.append('../PartyList')

from AddPersonDialog import AddPersonDialog

class TestAddPersonDialog(unittest.TestCase):
    """
    A test suite for the `AddPersonDialog` class.

    This class defines several test cases to verify the functionality of the 
    `AddPersonDialog` class, including handling empty fields and potentially 
    invalid data.
    """

    @classmethod
    def setUpClass(cls):
        """
        Creates a single QApplication instance before running any tests.

        This is necessary because Qt applications require a QApplication object 
        to be present before interacting with graphical elements. This method 
        ensures a single instance is created before tests and closed 
        after all tests are finished.
        """
        cls.app = QApplication(sys.argv)  # Create QApplication instance

    @classmethod
    def tearDownClass(cls):
        """
        Closes the QApplication instance after all tests are finished.

        This method ensures that the QApplication object is properly closed 
        after all tests are complete, preventing resource leaks or unexpected 
        behavior in subsequent tests.
        """
        cls.app.quit()  # Close QApplication

    def setUp(self):
        """
        Sets up a new instance of the `AddPersonDialog` class for each test.

        This method creates a fresh instance of the `AddPersonDialog` class 
        before each test case. This ensures that each test starts with a clean 
        state and avoids any potential interference between tests.
        """
        self.dialog = AddPersonDialog()

    def test_empty_fields(self):
        """
        Tests that the dialog displays error messages for all empty fields.

        This test case simulates leaving all input fields empty in the dialog 
        and verifies that the `accept` method correctly displays error messages 
        for each missing field. The test also asserts that the number of 
        displayed error messages matches the expected number of empty fields.
        """
        self.dialog.edit_first_name.setText("")
        self.dialog.edit_last_name.setText("")
        self.dialog.edit_phone.setText("")
        self.dialog.edit_email.setText("")

        # Call accept and check for error message with expected text
        self.dialog.accept()

        error_messages = self.dialog.get_error_messages()
        self.assertEqual(len(error_messages), 4)  # assert 4 messages displayed

    def test_invalid_email(self):
        # Simulate invalid email
        self.dialog.edit_first_name.setText("John")
        self.dialog.edit_last_name.setText("Doe")
        self.dialog.edit_phone.setText("123-456-7890")
        self.dialog.edit_email.setText("invalid_email")

        ## Call accept and check for error message with expected text
        self.dialog.accept()

        error_messages = self.dialog.get_error_messages()
        self.assertIn("Invalid email format", error_messages)

if __name__ == '__main__':
    unittest.main()

