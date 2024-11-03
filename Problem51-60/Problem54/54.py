# Poker Hands

from collections import Counter

def card_value(card):
    """Convert card rank to a numeric value."""
    rank = card[0]
    if rank in '23456789':
        return int(rank)
    elif rank == 'T':
        return 10
    elif rank == 'J':
        return 11
    elif rank == 'Q':
        return 12
    elif rank == 'K':
        return 13
    elif rank == 'A':
        return 14
    
def hand_rank(hand):
    values = sorted([card_value(card) for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    value_counts = Counter(values)
    unique_values = sorted(value_counts.keys(), reverse=True)

    is_flush = len(set(suits)) == 1

    is_straight = len(unique_values) == 5 and unique_values[0] - unique_values[4] == 4

    if is_flush and is_straight:
        if unique_values[0] == 14:
            # Royal flush
            return (10, unique_values)

        # Straight Flush
        return (9, unique_values)
    
    if 4 in value_counts.values():
        four_val = [v for v in unique_values if value_counts[v] == 4][0]
        kicker  = [v for v in unique_values if v!= four_val]
        
        # Four of a kind
        return (8, [four_val] + kicker)
    
    if 3 in value_counts.values() and 2 in value_counts.values():
        three_val = [v for v in unique_values if value_counts[v] == 3][0]
        two_val = [v for v in unique_values if value_counts[v] == 2][0]

        # Full house
        return (7, [three_val, two_val])
    
    if is_flush:
        # Flush
        return (6, unique_values)
    
    if is_straight:
        # Straight
        return (5, unique_values)
    
    if 3 in value_counts.values():
        three_val = [v for v in unique_values if value_counts[v] == 3][0]
        kickers = [v for v in unique_values if v != three_val]
        return (4, [three_val] + kickers)
    
    if list(value_counts.values()).count(2) == 2:
        pairs = sorted([v for v in unique_values if value_counts[v] == 2])
        kicker = [v for v in unique_values if value_counts[v] == 1][0]
        # Two pairs
        return (3, pairs + [kicker])
    
    if 2 in value_counts.values():
        pair_val = [v for v in unique_values if value_counts[v] == 2][0]
        kicker = [v for v in unique_values if v != pair_val]
        return (2, [pair_val] + kicker)
    
    return (1, unique_values)

def compare_hand(p1,p2):
    rank1 = hand_rank(p1)
    rank2 = hand_rank(p2)

    if rank1[0] > rank2[0]:
        return "P1"
    elif rank2[0] > rank1[0]:
        return "P2"
    
    for v1, v2 in zip(rank1[1],rank2[1]):
        if v1 > v2:
            return "P1"
        elif v2 > v1:
            return "P2"
        
    return "TIE"


def count_playerone_wins():
    with open("Problem51-60/Problem54/0054_poker.txt","r") as file:
        hands = file.readlines()
    
    count = 0
    for hand in hands:
        hand = hand.replace("\n","").split(" ")
        p1_hand = hand[:5]
        p2_hand = hand[5:]
        print(p1_hand)
        print(p2_hand)

        if compare_hand(p1_hand, p2_hand) == "P1":
            count += 1

    return count

print(count_playerone_wins())

