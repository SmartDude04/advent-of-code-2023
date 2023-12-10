from functools import cmp_to_key

# Use list comprehension to open the file and parse through
lines = [line.strip().split() for line in open("day-7/day-7.txt", "r")]
RANKING = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


#      Key:
# 6: Five of a kind
# 5: Four of a kind
# 4: Full house
# 3: Three of a kind
# 2: Two pair
# 1: One pair
# 0: High card
# Pass in a string of 5 symbols for the hand
def get_type(hand):
    
    first_card = hand[0]
    second_card = hand[1]
    third_card = hand[2]
    fourth_card = hand[3]
    fifth_card = hand[4]
    
    all_cards = [first_card, second_card, third_card, fourth_card, fifth_card]
    all_cards.sort()    
    card_set = {first_card, second_card, third_card, fourth_card, fifth_card}
    card_set = list(card_set)
    card_dict = {
        first_card: all_cards.count(first_card),
        second_card: all_cards.count(second_card),
        third_card: all_cards.count(third_card),
        fourth_card: all_cards.count(fourth_card),
        fifth_card: all_cards.count(fifth_card)
    }
            
    if len(card_set) == 1:
        return 6
    
    if len(card_set) == 2 and (card_dict[card_set[0]] == 4 or card_dict[card_set[1]] == 4):
        return 5
    
    if len(card_set) == 2:
        return 4
    
    
    if len(card_set) == 3 and (card_dict[card_set[0]] == 3 or card_dict[card_set[1]] == 3 or card_dict[card_set[2]] == 3):
        return 3
    
    if len(card_set) == 3:
        return 2
    
    if len(card_set) == 4:
        return 1
    
    return 0

lines = [
    {"Hand": line[0],
     "Type": get_type(line[0]),
     "Bet": line[1]}
    
    for line in lines
]
       
def compare_values(hand_1, hand_2) -> int:
    
    hand_1_type = get_type(hand_1["Hand"])
    hand_2_type = get_type(hand_2["Hand"])
    
    if hand_1_type != hand_2_type:
        return hand_2_type - hand_1_type
    
    for i, char in enumerate(hand_1["Hand"]):
        if RANKING.index(char) != RANKING.index(hand_2["Hand"][i]):
            return RANKING.index(char) - RANKING.index(hand_2["Hand"][i])
    
    return 0

def get_points(sorted_hands):
    
    sum_points = 0
    for i, hand in enumerate(sorted_hands):
        sum_points += int(hand["Bet"]) * (i + 1)
    
    return sum_points

lines.sort(key=cmp_to_key(compare_values), reverse=True)

print(get_points(lines))