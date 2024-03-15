CREATE TABLE person ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, 
            first_name VARCHAR(40) NOT NULL,
            last_name VARCHAR(40) NOT NULL, 
            phone VARCHAR(40) NOT NULL,
            email VARCHAR(40) NOT NULL 
        )