cards = input().split(":")
new_deck = []
command = input()

while not command == "Ready":
    tokens = command.split()
    if "Add" in command:
        card = tokens[1]
        if card in cards:
            new_deck.append(card)
        else:
            print("Card not found.")
    elif "Insert" in command:
        card = tokens[1]
        index = int(tokens[2])
        if 0 <= index < len(new_deck) and card in cards:
            new_deck.insert(index, card)
        else:
            print("Error!")
    elif "Remove" in command:
        card = tokens[1]
        if card in new_deck:
            new_deck.remove(card)
        else:
            print("Card not found.")
    elif "Swap" in command:
        card1 = tokens[1]
        card2 = tokens[2]
        index1 = new_deck.index(card1)
        index2 = new_deck.index(card2)
        new_deck[index1], new_deck[index2] = new_deck[index2], new_deck[index1]
    elif "Shuffle" in command:
        new_deck.reverse()
    command = input()

print(" ".join(new_deck))
