import random

money = 100

#Write your game of chance functions here
def coin(bet,call):
  flip = random.randint(1,2)
  # checking if bet is possible
  if bet < 0:
    print( 'You cannot bet negative amounts, please bet a positive amount')
    return 0
  if bet == 0:
    print('You cannot bet 0, please bet a higher amount')
    return 0
  if  bet > money :
    print("""Sorry you don't have enough money for that bet""")
    return 0
  # defining heads and tails
  if flip ==1:
    flip = 'heads'
  else:
    flip = 'tails'
  if flip == call and bet > 0:
    print('Result is ' + flip)
    print('You won ' + str(bet))
    return bet
  elif flip != call and bet > 0 :
    print('Result is ' + flip)
    print('You lost ' + str(-bet))
    return (-bet)

def cho_han(bet,result):
   # checking if bet is possible
  if bet < 0:
    print( 'You cannot bet negative amounts, please bet a positive amount')
    return 0
  if bet == 0:
    print('You cannot bet 0, please bet a higher amount')
    return 0
  if  bet > money :
    print("""Sorry you don't have enough money for that bet""")
    return 0
    #rolling dice
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  if (dice1 + dice2) % 2 == 0 and result == 'even':
    print('Dice total is: '+ str(dice1 + dice2))
    print('You won ' + str(bet))
    return bet
  elif (dice1 + dice2) % 2 != 0 and result == 'odd':
    print('Dice total is: '+ str(dice1 + dice2))
    print('You won ' + str(bet))
    return bet
  else:
    print('Dice total is: '+ str(dice1 + dice2))
    print('You lost ' + str(-bet))
    return (-bet)

def cards(bet_p1, bet_p2):
 # checking if your bet is possible:
  if bet_p1 < 0:
    print( 'You cannot bet negative amounts, please bet a positive amount')
    return 0
  if bet_p1  == 0:
    print('You cannot bet 0, please bet a higher amount')
    return 0
  if  bet_p1 > money :
    print("""Sorry you don't have enough money for that bet""")
    return 0
    # determine cards 
  deck= list(range(1,15))*4
  card_p1 = random.choice(deck)
  card_p2 = random.choice(deck)
  if card_p1 > card_p2:
    print('Player 1 has the higher card: ' + str(card_p1) + '. Player 2 has a lower card: '+ str(card_p2))
    print('Player 1 won ' + str(bet_p2))
    return bet_p2
  elif card_p1 < card_p2:
    print('Player 2 has the higher card: '+ str(card_p2) + '. Player 1 has a lower card: '+ str(card_p1))
    print('Player 1 lost ' + str(-bet_p1))
    return (-bet_p1)
  else:
    print('Tie. Player 1 and Player 2 have the same number of card: ' + str(card_p1))
    print('Both players won 0')
    return 0

def roulette(bet,outcome):
   # checking if your bet is possible:
  if bet < 0:
    print( 'You cannot bet negative amounts, please bet a positive amount')
    return 0
  if bet  == 0:
    print('You cannot bet 0, please bet a higher amount')
    return 0
  if  bet > money :
    print("""Sorry you don't have enough money for that bet""")
    return 0
  #playing roulette to get a number
  numb = random.randint(1,36)
  #playing for color
  color = random.randint(1,2)
  if color == 1:
    color = 'black'
  else:
    color = 'red'
  #playing for even or odd
  if numb % 2 == 0 and outcome == 'even':
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You won ' + str(bet))
    return bet
  elif numb % 2 != 0 and outcome == 'odd':
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You won ' + str(bet))
    return bet
  elif color == 'black' and outcome == 'black':
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You won ' + str(bet))
    return bet
  elif color == 'red' and outcome == 'red':
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You won ' + str(bet))
    return bet
  elif numb == outcome:
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You won ' + str(35*bet))
    return 35*bet
  else:
    print('The result is: ' +str(numb) + ', color:' + color)
    print('You lost ' + str(-bet))
    return (-bet)

#Call your game of chance functions here
money += coin(50,'heads')
print(money)
money += cho_han(-60, 'odd')
print(money)
money += cards(20, 30)
print(money)
money += roulette(50, 'red')
print(money)








