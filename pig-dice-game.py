from random import randint

current = 0
sum = 0

#player roll
def roll():
  roll_dice = print(randint(1,7))
  return roll_dice

#player bank
def bank():
  sum += current
  print(sum)



