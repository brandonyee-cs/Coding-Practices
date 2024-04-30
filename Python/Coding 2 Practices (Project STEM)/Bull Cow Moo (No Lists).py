#Brandon Yee, Allen Xia, Jack Scioscia, Markus Soennichsen 
import random
#Functions
def checknumrepeat(num1,num2):
  if num1 == num2: 
    return False
  else: 
    return True
def generate_number():
  dig1 = random.randint(1,9)
  truefalsenum = False
  while truefalsenum != True:
    dig2 = random.randint(1,9)
    truefalsenum = checknumrepeat(dig1, dig2)
  truefalsenum = False
  while truefalsenum != True:
    dig3 = random.randint(1,9)
    truefalsenumctrl = checknumrepeat(dig1, dig3)
    truefalsenumalt = checknumrepeat(dig2, dig3)
    if truefalsenumctrl == True and truefalsenumalt == True:
      truefalsenum = True
  return dig1, dig2, dig3
#Identifies bull, cow, moo
def identify_cow(num1, num2, num3, dig1, dig2, dig3):
  cowcount = 0
  if dig1 == num2 or dig1 == num3:
    cowcount = cowcount + 1
  if dig2 == num1 or dig2 == num3:
    cowcount = cowcount + 1
  if dig3 == num1 or dig3 == num2:
    cowcount = cowcount + 1
  return cowcount
def identify_bull(num1, num2, num3, dig1, dig2, dig3):
  bullcount = 0
  if dig1 == num1:
    bullcount = bullcount + 1
  if dig2 == num2:
    bullcount = bullcount + 1
  if dig3 == num3:
    bullcount = bullcount + 1
  return bullcount
def identify_moo(cowcount, bullcount):
  moocount = 0
  if cowcount == 0 and bullcount == 0:
    moocount = 1
  return moocount
def bullcowmoostring(bullcount, cowcount, moocount):
  bullcowmoostring = ""
  bullflag = 0
  if bullcount != 0:
    for i in range(1, bullcount + 1):
      bullcowmoostring = bullcowmoostring + "Bull "
      if bullcount > 0:
        bullflag = True
  if cowcount != 0:
    for i in range(1, cowcount + 1):
      bullcowmoostring = bullcowmoostring + "Cow "
  for i in range(moocount):
    if bullflag != True:
      bullcowmoostring = bullcowmoostring + "Moo "
    else:
      pass
  return bullcowmoostring
def wincheck(bullcount):
  if bullcount == 3:
    return True
  else: 
    return False
def average(totalGuesses, totalGames):
  average = totalGuesses / totalGames
  return average
#Game Loop
playing = True
print("Welcome to the Number Guessing Game!\nI'm thinking of a 3-digit number.\nEach digit is between 1 and 9.\nTry to guess the number.\nYou have 10 attempts to guess the number.\nGood luck!\n-----------------------------------------")
totalGuesses = 0
gameGuesses = 0
totalGames = 0
while playing == True:
  dig1, dig2, dig3 = generate_number()
  win_flag = False
  while win_flag != True:
    guess = int(input("Guess a three digit number: "))
    if guess > 999 or guess < 111:
      print("Guess a number between 111 and 999")
    else:
      print("You guessed: " + str(guess))
      gameGuesses += 1
      totalGuesses += 1
    num1 = (guess % 1000 - guess % 100)/100
    num2 = (guess % 100 - guess % 10)/10
    num3 = guess % 10
    bullcount = identify_bull(num1, num2, num3, dig1, dig2, dig3)
    cowcount = identify_cow(num1, num2, num3, dig1, dig2, dig3)
    moocount = identify_moo(cowcount, bullcount)
    Bullcowmoostring = bullcowmoostring(bullcount, cowcount, moocount)
    print(Bullcowmoostring)
    win_flag = wincheck(bullcount)
  print('You Won!')
  if gameGuesses == 1:
    print ("Brilliant!")
  elif gameGuesses <= 3:
    print ("Expert.")
  elif gameGuesses <= 5:
    print ("Good.")
  elif gameGuesses > 5:
    print ("Needs practice.")
  totalGames += 1
  totalGuesses += gameGuesses
  playagain = input("Would you like to play again? (y/n): ")
  if playagain == "n":
    playing = False
#averages guesses
averagetotalGuesses = average(totalGuesses, totalGames)
print("You averaged " + str(averagetotalGuesses) + " guesses per game.")