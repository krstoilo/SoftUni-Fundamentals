cards = input().split()
n_shuffles = int(input())

half = len(cards) // 2
top_card = cards[0]
bottom_card = cards[-1]

shuffled_cards = []

for shuffles in range(n_shuffles):
    left_cards = []
    right_cards = []

    for index in range(1, half):
        left_cards.append(cards[index])
    for index in range(half, len(cards)-1):
        right_cards.append(cards[index])

    for index in range(0, len(left_cards)):
        shuffled_cards.append(right_cards[index])
        shuffled_cards.append(left_cards[index])

    cards = shuffled_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffled_cards = []

print(cards)
