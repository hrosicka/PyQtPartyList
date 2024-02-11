from PyQt5.QtWidgets import QMessageBox  
from PyQt5.QtSql import QSqlDatabase, QSqlQuery  
  
  
def _createPersonTable():  
    """Create the person table in the database."""  
    createTableQuery = QSqlQuery()  
    return createTableQuery.exec(  
        """ 
        CREATE TABLE IF NOT EXISTS person ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL, 
            phone VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL 
        ) 
        """  
    )  
  
  
def createConnection(databaseName):  
    """Create and open a database connection."""  
    connection = QSqlDatabase.addDatabase("QSQLITE")  
    connection.setDatabaseName(databaseName)  
  
    if not connection.open():  
        QMessageBox.warning(  
            None,  
            "Person",  
            f"Database Error: {connection.lastError().text()}",  
        )  
        return False  
  
    _createPersonTable()  
    return True  