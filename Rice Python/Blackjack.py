# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        string = ''
        for card in self.cards:
            string = string + str(card) + ' '
        return string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        for card in self.cards:
            hand_value += VALUES[card.get_rank()]
        for card in self.cards:
            if (card.get_rank() == 'A'):
                if (hand_value + 10 <= 21):
                    return hand_value + 10
                else:
                    return hand_value
        return hand_value
   
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0]+(i*80),pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for each in SUITS:
            for num in RANKS:
                self.cards.append(Card(each,num))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        string = ''
        for card in self.cards:
            string = string + str(card) + ' '
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, score
    outcome = ''
    
    if(in_play):
        outcome = "You forfeited. New round."
        score -= 1
    
    global deck1, player, dealer
    deck1 = Deck()
    deck1.shuffle()
    player = Hand()
    dealer = Hand()
    for i in range(2):
        player.add_card(deck1.deal_card())
        dealer.add_card(deck1.deal_card())
    
    in_play = True

def hit():
    global player, deck1, in_play, score, outcome
    if (in_play):
        if (player.get_value() <= 21):
            player.add_card(deck1.deal_card())
            if (player.get_value() > 21):
                outcome = 'You busted. Dealer wins.'
                score -= 1
                in_play = False
            
       
def stand():
    global player, deck1, dealer, score, in_play, outcome
    if (in_play):
        if (player.get_value() > 21):
            print "You have busted"
        while (dealer.get_value() < 17):
            dealer.add_card(deck1.deal_card())
            if (dealer.get_value() > 21):
                outcome = 'Dealer busted. You win.'
                score += 1
                in_play = False
    
    if(in_play):
        if (player.get_value() > dealer.get_value()):
            outcome = "You win."
            score += 1
            in_play = False
        if (dealer.get_value () >= player.get_value()):
            outcome = "Dealer wins."
            score -= 1
            in_play = False

# draw handler    
def draw(canvas):
    global player, dealer, in_play
    
    canvas.draw_text("Blackjack",[100,75],50,'Blue')
    canvas.draw_text('Score: ' + str(score),[400,75],30,'Black')
    
    canvas.draw_text(outcome,[250,130],30,'Black')
    
    canvas.draw_text("Dealer",[100,130],30, 'Black')
    dealer.draw(canvas, [100, 150])
    
    canvas.draw_text("Player",[100,380],30, 'Black')
    player.draw(canvas, [100, 400])
    
    if(in_play):
        canvas.draw_text("Hit or stand?",[300,380],30,'Black')
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [100 + CARD_CENTER[0], 150 + CARD_CENTER[1]], CARD_SIZE)
    else:
        canvas.draw_text('New deal?',[300,380],30,'Black')


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric