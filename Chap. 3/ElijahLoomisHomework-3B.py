#Elijah Loomis
#Magic Date Program
#The program should then determine whether the
#month times the day equals the year.

print ("Elijah Loomis's Magic Date Validation App")

print ('\n')

userDay = int( input ('Enter the day of the month as an Integer: '))
userMonth = int( input ('Enter the month of the year as an Integer: '))
userYear = int( input ('Enter the year of the Century as a two digit Integer: '))

print ('\n')

if userMonth * userDay == userYear:
    print( str( userMonth ) + "/" + str( userDay ) + "/" + \
           str( userYear ) + " is a Magic Date." )
else:
    print( str( userMonth ) + "/" + str( userDay ) + "/" + \
           str( userYear ) + " is Not a Magic Date." )

input('')
