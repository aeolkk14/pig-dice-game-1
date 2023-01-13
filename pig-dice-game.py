import random

def roll():
  return random.randint(1,6)

player = [ 'player', 'computer']
score = {'player': 0, 'computer': 0}

random.shuffle(player)

while True:
  for i in player:
    if i == 'player':
      choose = input("ROLL(r) or STOP(s)>" ) 
      turn = 0
      total = 0


