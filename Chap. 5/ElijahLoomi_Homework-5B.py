
def main():
    print ("Elijah Loomis's Prime Number List")
    
    start = input ("would you like to check if a number is prime? 'y' for YES 'n' for NO: ")
    while start == 'y':
        print ("Elijah Loomis's Prime Number Checker" + '\n')
        prini = int(input("Type the range of prime numbers from 2 to: "))
        if prini >= 2:
            isprime(prini)
            start = input('\n' + 'agian? ')
        else:
            prini = int(input("re-enter the value: "))

def isprime(priNI):
    for num in range(2, priNI + 1):
       if num > 1:
           for i in range(2,num):
               if (num % i) == 0:
                   break
           else:
               print(num)

main()
