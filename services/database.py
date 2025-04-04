import sqlite3

#Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;

# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-LUNNLLH;DATABASE=CrudPython;Trusted_Connection=yes')

cnxn = sqlite3.connect('curriculo.db', check_same_thread=False)

cursor = cnxn.cursor()


