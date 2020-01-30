import sqlite3
conn = sqlite3.connect('magie.db')

c = conn.cursor()

# c.execute('''CREATE TABLE magieValues
#                (date text, magie text, impuls text, bw text)''')

# Insert a row of data
c.execute("INSERT INTO magieValues VALUES ('2020-01-30','12','49','29')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.



t = ('2020-01-30')
c.execute('SELECT * FROM magie_values')
print(c.fetchone())

conn.close()