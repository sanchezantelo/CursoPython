# Convert file existing_db.db to SQL dump file dump.sql
import sqlite3

con = sqlite3.connect("basededatos.sqlite")
with open('dump.sql', 'w') as f:
    for line in con.iterdump():
        print(line)
        f.write('%s\n' % line)
con.close()