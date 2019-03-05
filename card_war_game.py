from random import shuffle

suites = 'H D S C'.split()
#this split function will  help to create the list of those cards

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#making card pairing within sets



"""
    mycards = [(s,r) for s in suites for r in ranks]
    or
    mycards = []
    for r in ranks:
        for s in suites:
            mycards.append((s,r))
"""


class Deck:
    """
    this class will help is splitting the deck of cards in two and distributing them ,
    it will use suites and ranks to create the deck of cards
    """
    def __init__(self):
        print("Creating new ordered Deck!")

        self.allcards = [(s,r) for s in suites for r in ranks]

    def shuffle(self):
        print("shuffling deck")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
        #will return the two halfs in tuples

class Hand():
    #this class willbe used to make add or remove cards from the deck of mycards
    def __init__(self,cards):
        self.cards  = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():
    #this will hold the name of players turn and also the instance of poped out cards
    def __init__(self,name,hand):
        self.name = name
        self.hand= hand
    #hand will be passed as the object of Hand class
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed:{}".format(self.name,drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if(len(self.hand.cards)<3):
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
                return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) !=0


print("lets play")

#making deck
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#creating players
comp = Player("computer",Hand(half1))

name = input("what is ur name")

user = Player(name,Hand(half2))
total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds+=1
    print("time for new round")
    print("current standings")
    print(user.name+"has the count :"+str(len(user.hand.cards)))
    print(comp.name+"has the count :"+str(len(comp.hand.cards)))
    print('Draw a card')
    print('\n')

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if(c_card[1]==p_card[1]):
        war_count+=1

        print("war!")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if ranks.index(c_card[1]) < ranks.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print ("game over , number of rounds:"+str(total_rounds))
print("a war happened"+str(war_count)+"times")
