import sqlite3
conn=sqlite3.connect('FridayProj5.db')
cr=conn.cursor()

cr.execute('''SELECT question, answer FROM Questans''')

triviaQuestions=cr.fetchall()

for question, correct_answer in triviaQuestions:
     print(question)
     answer= input('Your answer: ')
     if answer == correct_answer:
        print ("Correct!\n")
     else:
        print ("Incorrect. The correct answer is "+ correct_answer + '.\n' )

print("Quiz ended.")
print('')

