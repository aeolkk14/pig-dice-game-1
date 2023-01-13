from random import randint



turn = True
    


#player roll and bank
def roll(current, sum):
    roll_dice = randint(1,6)
    print(roll_dice)
    
    if roll_dice == 1:
        current = 0
        print('Change player!')
        turn = False
    else:
        current += roll_dice
        print(f'current= {current}')
        user_choose = input(print('Choose Roll(r) or Bank(b): '))

        if user_choose == 'r':
            roll(current, sum)
        else:
            sum += current
            print(f'sum= {sum}')
            print('Change player!')
            turn = False
            


#Start
print("Let's play pig-dice-game!!")
start = input(print('Choose Roll(r) or Stop(s): '))

while start == 'r':
    
    # First player
    while turn == True:

        current = 0
        sum = 0
        
        dice = randint(1,6)
        print(dice)

        if dice == 1:
            current = 0
            print('Change player!')
            turn = False
        else:
            current += dice
            print(f'current= {current}')
            user_choose = input(print('Choose Roll(r) or Bank(b): '))

            if user_choose == 'r':
                roll(current, sum)
            else:
                sum += current
                print(f'sum= {sum}')
                turn = False
    
    # Change player
    while turn == False:
        
        sum = 0
        current = 0

        dice = randint(1,6)
        print(dice)

        if dice == 1:
            current = 0
            print('Change player!')
            turn = True
        else:
            current += dice
            print(f'current= {current}')
            user_choose = input(print('Choose Roll(r) or Bank(b): '))

            if user_choose == 'r':
                roll(current, sum)
            else:
                sum += current
                print(f'sum= {sum}')
                turn = True

    

