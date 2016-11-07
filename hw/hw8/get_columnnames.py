import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_3'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('PRAGMA TABLE_INFO({})'.format(table_name))

names = [tup[1] for tup in c.fetchall()]
print(names)

conn.close()