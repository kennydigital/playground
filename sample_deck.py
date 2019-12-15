import random, numpy

# 13 A, 2,3,4,5,6,7,8,9, 10, J,Q,K
# 4 SUIT: HEARTS, SPAIDS, DIAMONDS, CLUBS
# 52 cards = 13 * 4
listFace=['A', '2', '3', '4', '5', '6','7', '8', '9', '10','J', 'Q','K']
listSuit=["HEARTS", "SPAIDS", "DIAMONDS", "CLUBS"]


class Card:
    cardRank=None
    cardSuit=None

    def __init__(self, cardRank, cardSuit):
        self.cardRank=cardRank
        self.cardSuit=cardSuit



#Dictionary that will hold my cards
deck = {}


# Fill up the deck. We want key:value like this. {0: Object, 1: object}
cardIndex=0
for i in range(13):
    for j in range(4):
       deck[cardIndex]=Card(listFace[i], listSuit[j])
       cardIndex=cardIndex+1

#Listing items of given dictionary
aList = list(deck.items())

#Leveraging numpy to shuffle items in list
numpy.random.shuffle(aList)

#Gettin shuffled dictionary back into dict
deck = dict(aList)

# Print the dictionary
for key,value in deck.items():
    print("{} {} {}".format(key,value.cardRank, value.cardSuit))
