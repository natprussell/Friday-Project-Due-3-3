import sqlite3
conn=sqlite3.connect('FridayProj5.db')
cr=conn.cursor()

cr.execute('''SELECT * FROM Questans''')

print(cr.fetchall())