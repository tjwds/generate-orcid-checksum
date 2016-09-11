# makedb.py

import sqlite3

conn = sqlite3.connect('../db/allpossibleORCIDs.db')

conn.execute('''CREATE TABLE ORCIDS
       (ID INT PRIMARY KEY     NOT NULL,
       ORCID            INT     NOT NULL);''')

conn.close()
