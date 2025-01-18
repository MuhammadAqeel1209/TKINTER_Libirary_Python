import pyodbc 

DRIVER_NAME = 'SQL Server'
SERVER_NAME = 'DESKTOP-FPO2BUS'
DATABASE_NAME = 'PYTHON'

# -->👇👇👇 Syntax to connect the Python connect to sql server
#conn_str = 'Driver={SQL Server};Server=your_server_name;Database=your_database_name;Trust_Connection = yes'
conn_str = 'Driver={SQL Server};Server=DESKTOP-FPO2BUS\SQLEXPRESS;Database=PYTHON;Trust_Connection = yes;'


con = pyodbc.connect(conn_str)
print(con)
