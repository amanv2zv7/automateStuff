#Collatz sequence
#
#
#Input validation using try and except statements



def collatz(number):

        if number%2==0:
            number=number//2
            print(number)
            return(number)
        else:
            number=3*number + 1
            print(number)
            return(number)

        
while True:
    print('Enter a positive integer:')

#error handling
    try:
        num = int(input())
            
        while(num is not 1):
            num=collatz(num)
    except ValueError:
            num=1
            print('Only integer values accepted')
    except KeyboardInterrupt:
            num=1
            print('Keyboard Interrupt')
#option to continue or terminate program    
    if num is 1:
        print('To terminate hit enter, to continue press any other key')
        key=input()
        if key is '':
            break
