# testdb.py

import sqlite3

conn = sqlite3.connect('../db/test.db')

cursor = conn.execute('''SELECT * FROM orcids ORDER BY RANDOM() LIMIT 1;''')

for row in cursor:
   print(row[0])
