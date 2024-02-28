import sqlite3
conn=sqlite3.connect('FridayProj5.db')
cr=conn.cursor()

cr.execute("SELECT name FROM sqlite_master WHERE type= 'table';")

print(cr.fetchall())

# table name QuestAns