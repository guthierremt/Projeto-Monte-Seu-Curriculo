import pyodbc
#Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=CrudPython;Trusted_Connection=yes')

cursor = cnxn.cursor()
print(pyodbc.version)