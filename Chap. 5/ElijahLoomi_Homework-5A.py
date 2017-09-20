##Elijah Loomis
##Homework 5A

##Prime Number Checker

def main():
    start = input ("would you like to check if a number is prime? 'y' for YES 'n' for NO: ")
    print('\n')
    while start == 'y':
        print ("Elijah Loomis's Prime Number Checker" + '\n')
        num = int(input("type in an integer: "))
        if num >= 2:
            isprime(num)

            
        else:
            num = int(input("re-enter the value: "))

def isprime(nuM):
    x = True 
    for i in range(2, nuM):
       if nuM%i == 0:
           x = False
           break 


    if x:
        print ('\n')
        print (nuM , "is prime" + '\n')
        start = input ("would you like to check if another number is prime? 'y' for YES 'n' for NO: ")
        print ('\n')
    else:
        print ('\n')
        print (nuM , "is not prime" + '\n')
        start = input ("would you like to check if another number is not prime? 'y' for YES 'n' for NO: ")
        print ('\n')


main()
