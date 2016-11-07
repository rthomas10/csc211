import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
new_column = 'unique_names'
column_type = 'TEXT'
index_name = 'my_unique_index'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute("ALTER TABLE {tn} ADD COLUMN'{cn}' {ct}"\
        .format(tn=table_name, cn=new_column, ct=column_type))
c.execute("UPDATE {tn} SET {cn}='sebastian_r' WHERE {idf}=123456".\
        format(tn=table_name,idf=id_column, cn=new_column))

c.execute('CREATE INDEX {ix} on {tn}({cn})'\
        .format(ix=index_name, tn=table_name, idf=id_column, cn=new_column))

c.execute('DROP INDEX {ix}'.format(ix=index_name))

conn.commit()
conn.close()