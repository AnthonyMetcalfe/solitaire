import math
import random
import numpy as np

# Changeable things:
FINISHFIRSTBOOL = True
LARGESTFIRSTBOOL = True
LASTFIRSTBOOL = True

SUITS = {0: "heart", 2: "diamond", 1: "club", 3: "spade"}
deck = []
stacks = {}
revealedStacks = {}
finishStacks = [0, 0, 0, 0]

ALLCARDS = {}
for i in (range (1,53)):
    ALLCARDS[i] = {}
    ALLCARDS[i]["value"] = math.floor(((i - 1) / 4)) + 1
    ALLCARDS[i]["suit"] = i % 4


def getCard(num):
    return ALLCARDS[num]

# Works properly
# Shuffles the deck, deals the deck, and starts the tracker of the stacks.
def setup():
    if (len(deck) > 0):
        for i in range(0, len(deck)):
            deck.pop()
    for r in np.random.permutation(52):
        deck.append(r+1)
    finishStacks[0] = 0
    finishStacks[1] = 0
    finishStacks[2] = 0
    finishStacks[3] = 0

    for i in (range(1,8)):
        stacks[i] = []

    for i in range(0,7):
        if (i < 1):
            stacks[1].append(deck.pop(0))
        if (i < 2):
            stacks[2].append(deck.pop(0))
        if (i < 3):
            stacks[3].append(deck.pop(0))
        if (i < 4):
            stacks[4].append(deck.pop(0))
        if (i < 5):
            stacks[5].append(deck.pop(0))
        if (i < 6):
            stacks[6].append(deck.pop(0))
        if (i < 7):
            stacks[7].append(deck.pop(0))

    for i in range(1, 8):
        revealedStacks[i] = []
        revealedStacks[i].append(stacks[i][-1])

# Works properly
def moveToStack(cardsArray, index):
    for card in cardsArray:
        stacks[index].append(card)
        revealedStacks[index].append(card)

# Works properly
def moveToFinish(index):
    finishStacks[index] += 1

# Works properly
def removeAllFromStack(index):
    num = len(revealedStacks[index])
    for i in range(0, num):
        stacks[index].pop()
    revealedStacks[index] = []
    if (len(stacks[index]) > 0):
        revealedStacks[index].append(stacks[index][-1])

# Works properly
def removeTopFromStack(index):
    stacks[index].pop()
    revealedStacks[index].pop()

# Works properly and is probably not necessary
def removeFromDeck(index):
    deck.pop(index)

# Works properly
def canMoveToStack(cardArray, bool):
    card = cardArray[0]
    for i in range(1, 8):
        mCard = getCard(card)
        if (len(revealedStacks[i]) == 0):
            if (mCard["value"] == 13 and not bool):
                moveToStack(cardArray, i)
                return True
            else:
                continue
        stay = revealedStacks[i][-1]
        sCard = getCard(stay)
        if ((mCard["suit"] % 2 != sCard["suit"] % 2) and (mCard["value"] + 1 == sCard["value"])):
            moveToStack(cardArray, i)
            return True
    return False

# Works properly
def canMoveToFinish(cardValue):
    card = getCard(cardValue)
    if (finishStacks[card["suit"]] + 1 == card["value"]):
        moveToFinish(card["suit"])
        return True
    else:
        return False

# Should work properly
def scanStacks():
    for index in range(1, 8):
        cardArray = revealedStacks[index]
        if (len(cardArray) > 0):
            if (canMoveToStack(cardArray, cardArray[0] == stacks[index][0])):
                removeAllFromStack(index)
                return True
            if (canMoveToFinish(stacks[index][-1])):
                removeTopFromStack(index)
                return True
    return False

# Should work properly
def scanDeck():
    for i in range(0, len(deck), 3):
        cardArray = [deck[i]]
        if (canMoveToStack(cardArray, False)):
            removeFromDeck(i)
            return True
        if (canMoveToFinish(deck[i])):
            removeFromDeck(i)
            return True
    return False

def play():
    bool = True
    while (bool):
        bool = False
        bool = scanStacks()
        if (not bool):
            bool = scanDeck()


for i in range(0, 100):
    setup()
    play()
    # print("FINISH")
    print(finishStacks)
    # print("STACKS")
    # print(stacks)
    # print("DECK")
    # print(deck)
