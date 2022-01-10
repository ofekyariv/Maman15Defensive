import sqlite3


class Database:
    conn = sqlite3.connect('server.db')
    conn.text_factory = bytes
    try:
        conn.executescript("""
         CREATE TABLE clients(ID varchar(128) NOT NULL PRIMARY KEY, UserName varchar(255),
         PublicKey varchar(160), LastSeen Date);
         """)
    except:
        print("Error, Table is already exist")
    try:
        conn.executescript("""
         CREATE TABLE clients(ID varchar(4) NOT NULL PRIMARY KEY, ToClient varchar(16),
         FromClient varchar(16), Type varchar(1), Content Blob);
         """)
    except:
        print("Error, Table is already exist")
