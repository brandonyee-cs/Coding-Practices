#!/usr/bin/python

import math

question = input("Enter Question: (1, 2a, 2b, 2c, 3a, 3b): ")

#1: Positive Number Greater Than Two

def posnumsqr(num):
    if num > 2:
        while num > 2:
            num = round(math.sqrt(num), 3)
            print(num)
    else:
        print("ERROR // NUMBER LESS THAN 2")

#2a Passing Rating Calculator
def calcPassRating(c,y,t,i,function = False):
    c = ((c * 100) - 30)/20
    y = (y-3)/4
    t = t * 20
    i = 2.375 - (i * 25)
    passrating = ((c + y + t + i)/6)* 100
    if function == True:
        return round(passrating, 2)
    else:
        print (f"Pass Rating: {round(passrating, 2)}")

#2b Skill Level
def getSkill(passrating):
    if passrating > 95:
        return 'great!', passrating
    elif passrating > 90:
        return 'good.', passrating
    elif passrating > 85:
        return 'mediocre.', passrating
    else:
        return 'poor', passrating

#3a: Ancient Multiplication
def AncientMult(numa,numb):
    count = 0
    while numb > 0:
        if numb % 2 != 0:
            count += numa
        numa *= 2
        numb = numb // 2
    return count + numb

if question == "1":
    num = int(input("Enter an integer greater than 2: "))
    posnumsqr(num)

elif question == '2a':
    C = float(input("Enter completions per attempt: "))
    Y = float(input("Enter Yards Per Attempt: "))
    T = float(input("Touchdown Per Attempt: "))
    I = float(input("Interceptions  Per Attempt: "))

    calcPassRating(C,Y,T,I)

elif question == '2b':
    fbdict = {
        'Donovan McNabb' : [180, 316, 2647, 18, 6],
        'Tom Brady' : {319, 516, 3529, 24, 12},
        'Peyton Manning' : {362, 557, 4397, 31, 9}
    }

    player_name = int(input('Enter a Player\'s Name (1 = Donovan McNabb, 2 = Tom Brady, 3 = Peyton Manning): '))
    if player_name == 1: name = 'Donovan McNabb'
    elif player_name == 2: name = 'Tom Brady'
    elif player_name == 3: name = 'Peyton Manning'
    c, y, t, i = round(fbdict.get(name)[0]/fbdict.get(name)[1], 2), round(fbdict.get(name)[2]/fbdict.get(name)[1], 2), round(fbdict.get(name)[3]/fbdict.get(name)[1], 2), round(fbdict.get(name)[4]/fbdict.get(name)[1], 2)
    passrating = calcPassRating(c,y,t,i,True)
    skillLevel, passrating = getSkill(passrating)
    print(f"{name}, with a pass rating of {passrating}, is considered to be {skillLevel}")

#2c: Modified Version of Both

elif question == '2c':
    C = float(input("Enter completions per attempt: "))
    Y = float(input("Enter Yards Per Attempt: "))
    T = float(input("Touchdown Per Attempt: "))
    I = float(input("Interceptions  Per Attempt: "))

    skillLevel, passrating = getSkill(calcPassRating(C,Y,T,I))
    print(f"The player with a pass rating of {passrating} is considered {skillLevel}")

elif question == '3a':
    numa = int(input("Enter a Value: "))
    numb = int(input("Enter a Value: "))

    num = AncientMult(numa,numb)
    print(num)

elif question == '3b':
    multagain = False
    while multagain != True:
        numa = int(input("Enter a Value: "))
        numb = int(input("Enter a Value: "))

        num = AncientMult(numa,numb)
        print(num)

        multagainquestion = input("Again? (y/n): ")
        if multagainquestion == 'n':
            multagain = True