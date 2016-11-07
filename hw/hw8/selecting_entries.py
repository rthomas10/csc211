import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
some_id = 123456
column_2 = 'my_2nd_column'
column_3 = 'my_3rd_column'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * FROM {tn} WHERE {cn} = "Hi World"'.\
        format(tn=table_name, cn=column_2))
all_rows = c.fetchall()
print('1):', all_rows)

c.execute('SELECT {coi1} FROM {tn} WHERE {coi1}="Hi World"'.\
        format(coi1=column_2, tn=table_name, cn=column_2))
all_rows = c.fetchall()
print('2):', all_rows)

c.execute('SELECT {coi1}, {coi2} FROM {tn} WHERE {coi1}="Hi World"'.\
        format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))
all_rows = c.fetchall()
print('3):', all_rows)

c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World" LIMIT 10'.\
        format(tn=table_name, cn=column_2))
ten_rows = c.fetchall()
print('4):', ten_rows)

c.execute("SELECT * FROM {tn} WHERE {idf} = {my_id}".\
        format(tn=table_name, cn=column_2, idf=id_column, my_id=some_id))
id_exists = c.fetchone()
if id_exists:
    print('5): {}'.format(id_exists))
else:
    print('5): {} does not exist'.format(some_id))

conn.close()
