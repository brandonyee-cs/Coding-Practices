def Course_Information(): 
    print('Course Information')

    room = { 
    'CS101' : '3004',
    'CS102' : '4501',
    'CS103' : '6755',
    'NT110' : '1244',
    'CM241' : '1411'
    }; instructor = {
        'CS101' : 'Haynes',
        'CS102' : 'Alvarado',
        'CS103' : 'Rich',
        'NT110' : 'Burke',
        'CM241' : 'Lee'
    }; time = {
        'CS101' : '8:00 AM',
        'CS102' : '9:00 AM',
        'CS103' : '10:00 AM',
        'NT110' : '11:00 AM',
        'CM241' : '1:00 PM'
    }
    
    userinput = input("Enter Course Number: ")

    if  userinput in room:
        print(f"{userinput}: Room {room[userinput]}, Instructor {instructor[userinput]}, Time  {time[userinput]}")
    else:
        print("Error // Course Not Available.")

Course_Information()

def NameandEmailAddresses():
    print("Email List:")
    loop = True

    phonebook = {}

    while loop == True:

        userinput = input('Enter Option (d for delete, a for add, l for lookup, q for quit): ')

        if userinput == 'd':
            keytodelete = input('Enter  name to be deleted: ')
            del phonebook[keytodelete]

        elif userinput == 'a':
            keytoadd = input('Enter name to be added: ' )
            numbertoadd = input('Enter corresponding email: ')
            phonebook[keytoadd] = numbertoadd

        elif userinput == 'l':
            keytolookup = input('Enter name to be looked up: ')
            if keytolookup in phonebook:
                print(f"{keytolookup}'s email is {phonebook[keytolookup]}")
            else:
                print("Error // Name Not Available")
        
        elif userinput == 'q':
            loop = False

        else: 
            print('Error // Option is not Available.')

NameandEmailAddresses()

import random

def calculate_hand_value(hand):
        value = 0;aces = 0

        for card in hand:

            if card[0] in ['Jack', 'Queen', 'King']: value += 10
            elif card[0] == 'Ace': aces += 1; value += 11
            else: value += int(card[0])

        while value > 21 and aces: value -= 10; aces -= 1
        return value
    
def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def play_game(deck):
    player1_hand = []; player2_hand = []

    while True:
        player1_hand.append(deal_card(deck));player2_hand.append(deal_card(deck))
        player1_value = calculate_hand_value(player1_hand); player2_value = calculate_hand_value(player2_hand)
        print(f"Player 1's hand: {player1_hand} (Value: {player1_value})"); print(f"Player 2's hand: {player2_hand} (Value: {player2_value})")

        if player1_value > 21: print("Player 1 busts! Player 2 wins!"); return
        elif player2_value > 21: print("Player 2 busts! Player 1 wins!"); return

def blackjack():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']; ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    loop = True
    
    deck = [(rank, suit) for rank in ranks for suit in suits]

    while loop == True:
        play_game(deck)
        if deck:
            print("Press Enter to play another game... (q to quit)"); quit = input()
            if quit == 'q': loop = False

blackjack()