# game 'find number'
# user thinks of number: 1 <= n <= 100
# program tries to guess the number
# commands:
# y - yes (number is correct)
# n - no (number is wrong)
# < - [correct number is] less
# > - [correct number is] bigger

import random

limit = 100
print('Think of number: 0 <= n <=', limit)
a = 0
b = limit

def guess(bot,top):
    curbot = bot
    curtop = top
    current = random.randint(bot,top)
    print('I guess the number is',current)
    print("Type 'y' for 'yes' and 'n' for 'no':")
    yn = input()
    if yn.lower() == 'y':
        print('Game over, the number is found')
        return 0
    if yn.lower() == 'n':
        # ml - 'more or less'
        print('Is your number bigger or smaller then my try?')
        print("Type '>' for more and '<' for less:")
        ml = input()
        if ml == '>':
            guess(current + 1,curtop)
        elif ml == '<':
            guess(curbot,current - 1)

guess(a,b)
            
    
