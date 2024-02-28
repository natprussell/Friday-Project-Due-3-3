import sqlite3
conn=sqlite3.connect('FridayProj5.db')
cr=conn.cursor()

cr.execute('''PRAGMA table_info(Questans);''')

columns_info= cr.fetchall()

for column_info in columns_info:
    print(column_info[1])

# column names id, question, answer