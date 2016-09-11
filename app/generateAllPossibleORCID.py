# generate all possible results

import sqlite3
from orcidchecksum import generateCheckDigit

conn = sqlite3.connect('../db/allpossibleORCIDs.db')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS orcids")
cur.execute('''CREATE TABLE orcids
       (ORCID            INT     NOT NULL);''')

for x in range(15000000, 35000000):
    rawresult = ('0000000' + str(x) + str(generateCheckDigit(x)))
    resultarray = map(''.join, zip(*[iter(rawresult)]*4))
    result = '-'.join(resultarray)
    cur.execute("INSERT INTO orcids VALUES (?);", (result,))
    print(result)

conn.commit()
conn.close()
