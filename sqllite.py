#  Download and install to browse the data in the database
#  https://github.com/sqlitebrowser/sqlitebrowser/releases

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(383838,'2017-01-15','Ruby',23)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
