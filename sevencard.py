# CS 212, hw1-1: 7-card stud
#
# -----------------
#
# best_hand(hand) takes a seven card hand as input 
# and returns the best possible 5 card hand. 

import itertools
import poker

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    handlist = list(itertools.combinations(hand, 5))
    return max(handlist, key=poker.hand_rank)
    
def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_hand()