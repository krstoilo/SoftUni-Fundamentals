cards = input().split()
shuffles = int(input())


def shuffle_cards(cards):
    first_half = cards[:len(cards)//2]
    sec_half = cards[len(cards)//2:len(cards)]
    shuffle = first_half + sec_half
    shuffle[::2] = first_half
    shuffle[1::2] = sec_half
    return shuffle


for n in range(shuffles):
    cards = shuffle_cards(cards)

print(cards)