import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
        return f'{ranks[self.rank]} of {suits[self.suit]}'

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in range(1, 14) for suit in range(4)]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.hand = [deck.deal(), deck.deal()]

    def hit(self, deck):
        self.hand.append(deck.deal())

    def getPoints(self):
        aces = sum(card.rank == 1 for card in self.hand)
        points = sum(min(card.rank, 10) for card in self.hand)
        while points <= 11 and aces:
            points += 10
            aces -= 1
        return points

    def hasBlackjack(self):
        return len(self.hand) == 2 and self.getPoints() == 21

class Dealer(Player):
    def __init__(self, deck):
        super().__init__('DEALER', deck)

def play():
    deck = Deck()
    player = Player('Player 1', deck)
    dealer = Dealer(deck)

    while True:
        print(f'{player.name} hand: {[str(card) for card in player.hand]}')
        print(f'{player.name} points: {player.getPoints()}')
        if player.getPoints() > 21:
            print('Player busts, dealer wins!')
            return
        action = input('Do you want to hit or stay? ').lower()
        if action == 'hit':
            player.hit(deck)
        elif action == 'stay':
            break

    while dealer.getPoints() < 17:
        dealer.hit(deck)

    print(f'Dealer hand: {[str(card) for card in dealer.hand]}')
    print(f'Dealer points: {dealer.getPoints()}')
    if dealer.getPoints() > 21:
        print('Dealer busts, player wins!')
        return 1
    elif dealer.getPoints() > player.getPoints():
        print('Dealer wins!')
        return 0
    elif dealer.getPoints() < player.getPoints():
        print('Player wins!')
        return 1
    else:
        print('Tie game, dealer wins!')
        return 0

if __name__ == '__main__':
    gamescore = 0
    while True:
        gamescore += play()
        again = input('Do you want to play again? (yes/no) ').lower()
        if again != 'yes':
            print(f'Your score was {gamescore}')
            break