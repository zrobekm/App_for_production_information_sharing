import mysql.connector

# Establish a database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Mielonka_13",
    database="testdatabase"
)

mycursor = db.cursor()

create_database_decision = input("Do you want to create new database?[y/n] :")
if create_database_decision == "y":
    database_name = input("Database name: ")
    mycursor.execute(f"CREATE DATABASE {database_name}")
elif create_database_decision == "n":
    pass
else:
    create_database_decision = input("Do you want to create new database?[y/n] :")


# Fetch the list of tables
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()
#print(tables)

# Convert list of tuples to a list of STR table names
list_of_table_names = [table[0] for table in tables]
#print(list_of_table_names)

# Check and create tables crucial for app design
if "clients" not in list_of_table_names:
    mycursor.execute("CREATE TABLE Clients (name VARCHAR(10), Client_ID INT PRIMARY KEY, model_ID INT, order_ID INT)")

if "machines" not in list_of_table_names:
    mycursor.execute("CREATE TABLE Machines (name VARCHAR(10), Machine_ID INT PRIMARY KEY, Process_ID int), ")

if "products" not in list_of_table_names:
    mycursor.execute("CREATE TABLE PRODUCTS (name VARCHAR(10), Product_ID INT PRIMARY KEY)")

if "orders" not in list_of_table_names:
    mycursor.execute("CREATE TABLE ORDERS (name VARCHAR(10), Order_ID int PRIMARY KEY)")

if "process" not in list_of_table_names:
    mycursor.execute("CREATE TABLE PROCESS (name VARCHAR(10), Process_ID int PRIMARY KEY)")

def create_table():
    table_name = ('Cinputreate table (to skip creating enter "skip" command: ')
    if table_name == "skip":
        return
    mycursor.execute(f"CREATE TABLE {table_name}")
    amount_of_columns = int(input("Amount of queries: "))
    while amount_of_columns > 0:
        column_name = input("New column name: ")
        column_type = input("Datatype in new column : ")
        mycursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        amount_of_columns -= 1

def add_primary_key():
    altered_table = input('Add primary key to table.(If you want to skip this step enter "Skip"): ')
    if altered_table == "skip":
        pass
    if altered_table not in tables:
        altered_table = input("This table doesnt exist. Add primary key to different table: ")
    altered_column = input("Assign primary key to column: ")
    while altered_column:
        mycursor.execute(f"ALTER TABLE {altered_table} ADD PRIMARY KEY")

def add_foreing_key():
    table_new_foreign_key = input("Add foreing key to table: ")
    new_foreign_key = input("New foreing key: ")
    referenced_table = input("Referenced table ")
    mycursor.execute(f"ALTER TABLE {table_new_foreign_key} ADD FOREIGN KEY ({new_foreign_key}) REFERENCES {referenced_table}{new_foreign_key}")

def delete_table():
    table_name = input("Table name: ")
    mycursor.execute(f"DROP TABLE DROP IF EXISTS {table_name}")

def add_column():
    Altered_table = input("Table_name: ")
    column_name = input("Column_name: ")
    column_data_type = input("Column_data_type: ")
    mycursor.execute(f"ALTER TABLE {Altered_table} ADD {column_name} {column_data_type}")
