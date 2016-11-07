import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_3'
id_field = 'id'
date_col = 'date'
time_col = 'time'
date_time_col = 'date_time'
field_type = 'TEXT'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('CREATE TABLE {tn} ({fn} {ft} PRIMARY KEY)'\
        .format(tn=table_name, fn=id_field, ft=field_type))


c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
        .format(tn=table_name, cn=date_col))

c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES('some_id1', DATE('now'))"\
        .format(tn=table_name, idf=id_field, cn=date_col))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
        .format(tn=table_name, cn=time_col))

c.execute("UPDATE {tn} SET {cn}=TIME('now') WHERE {idf}='some_id1'"\
        .format(tn=table_name, idf=id_field, cn=time_col))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}'"\
        .format(tn=table_name, idf=id_field, cn=date_time_col))

c.execute("UPDATE {tn} SET {cn}=(CURRENT_TIMESTAMP) WHERE {idf}='some_id1'"\
        .format(tn=table_name, idf=id_field, cn=date_time_col))

c.execute("SELECT {idf} FROM {tn} WHERE {cn} BETWEEN '2013-03-06 10:10:10' AND 2015-03-06 10:10:10"\
        .format(idf=id_field, tn=table_name, cn=date_time_col))
all_date_times = c.fetchall()
print('4) all entries between ~2013 - 2015:', all_date_times)

c.execute("SELECT {idf} FROM {tn} WHERE DATE ('now') = {dc} >= AND DATE('now') - {tc} >= 12"\
        .format(idf=id_field, tn=table_name, dc=date_col, tc=time_col))
all_1day12hrs_entries = c.fetchall()
print('5) entries older than 1 day:', all_1day12hrs_entries)

conn.commit()
conn.close()