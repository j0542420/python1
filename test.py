#print("hello world")

#if 5>2:
    #print("5 is greater than 2")
    # this is how to make a comment in python

# random numbers
#import random
#print(random.randrange(1, 10))

import random
while (True):
    print("can you guess a random number from 1 to 10?")
    
    guess = int(input("Enter the a number between 1 and 10: "))
    
    
    rand = random.randrange(1, 10)

    if (guess < rand):
        print("your number is less than the random number")
    elif guess > rand:
        print("your number is greater than the random number")
    else:
        print("your number is correct")
        pass