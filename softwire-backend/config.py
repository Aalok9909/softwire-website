# config.py
import mysql.connector
import os 

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  
        database="softwire_db"          
    )

# connection = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASS"),
#     database=os.getenv("DB_NAME")
# )
