# utils/db_utils.py
import mysql.connector
import cx_Oracle
import pyodbc

# MySQL
def mysql_query(query, host, user, password, database):
    """Execute a query on a MySQL database."""
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# Oracle
def oracle_query(query, dsn, user, password):
    """Execute a query on an Oracle database."""
    connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

# SQL Server
def sqlserver_query(query, server, database, user, password):
    """Execute a query on a SQL Server database."""
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password}'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results