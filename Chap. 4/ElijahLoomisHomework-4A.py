# ElijahLoomis4A.py
# This program gets a numeric score from the user and displays the corresponding letter grade
# Elijah Loomis
A_score = 90
B_score = 80
C_score = 70
D_score = 60
print("Elijah Loomis’s Grading Program")
conT = input ('would like to convert a quiz score to a letter grade , y or n :  ')
if conT == 'n':
        exit = input('')
while conT == 'y':
    score = int(input('Enter your test score:'))
    if score < 0 or score > 100:
        cont = input ('re-enter your data y or n: ')
    while score >=0 and score <=100:
        if score >= A_score:
            print('Your grade is A.')
        elif score >= B_score:
            print('Your grade is B.')
        elif score >= C_score:
            print('Your grade is C.')
        elif score >= D_score:
            print('Your grade is D.')
        else:
            print('Your grade is F.')
        conT = input ('would like to convert another quiz score to a letter grade , y or n :  ')
exit = input('')
