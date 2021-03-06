
import random

# Pre-game

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n=5, deck=mydeck):
    handslist = [0] * numhands
    for i in range(numhands):
        hand = random.sample(deck, n)
        handslist[i] = hand
    return handslist

# Game

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    key = key or (lambda x : x)
    curmax = 0
    maxlist = []
    for x in iterable:
        if key(x) > curmax:
            curmax = key(x)
            maxlist = [x]
        elif key(x) == curmax:
            maxlist = maxlist + [x]
    return maxlist

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    acelow = [14, 5, 4, 3, 2]
    # if ranks contains a 2-5 a high ace, bring ace value down
    if ranks == acelow:
        ranks = [5, 4, 3, 2, 1]
    return ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5
    
def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r, s in hand]
    for i in range(4):
        if suits[i] != suits[i+1]:
            return False
    return True

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for x in ranks:
        if ranks.count(x) == n :
            return x
    return None

# FIX THIS!!!
def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    first = 0
    second = 0
    for r in ranks:
        if first == 0 and ranks.count(r) == 2: 
            first = r
        elif ranks.count(r) == 2:
            second = r
    if second == 0: 
        return None
    else: return (max[first, second], min[first, second])

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh,fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert straight(card_ranks(al)) == True 
    assert flush(sf) == True
    assert flush(fk) == False
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'

print test()