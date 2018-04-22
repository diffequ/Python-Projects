# BURAK KORYAN | koryan.ca | burak@koryan.ca | 21 April 2018 #
# Description : SQLite use with Python.Simple dB connection and data insert using Python.
# Example taken from Pythonspot.com #

import sqlite3 as lite
import sys
 
con = None
 
try:
    con = lite.connect('test.db')
except lite.Error, e:   
    print "Error %s:" % e.args[0]
    sys.exit(1)

with con:
 
    cur = con.cursor()  
    cur.execute("SELECT * FROM Users")

    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Nutella')")
    cur.execute("INSERT INTO Users VALUES(2,'Snickers')")
    cur.execute("INSERT INTO Users VALUES(3,'Gofretti')")
    cur.execute("INSERT INTO Users VALUES(5,'Tadelle')")
 
    rows = cur.fetchall()
 
    for row in rows:
        print row
if con:
        con.close()
        
 
 
