n = int(input())
music_pieces = {}

for pieces in range(n):
    m_p = input().split("|")
    m_p_details = m_p[1:]
    music_pieces[m_p[0]] = m_p_details

command = input()
while command != "Stop":
    token = command.split("|")
    if token[0] == "Add":
        piece = token[1]
        composer = token[2]
        key = token[3]
        if piece in music_pieces:
            print(f"{piece} is already in the collection!")
        else:
            details = []
            details.append(composer)
            details.append(key)
            music_pieces[piece] = details
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif token[0] == "Remove":
        piece = token[1]
        if piece in music_pieces:
            del music_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif token[0] == "ChangeKey":
        piece = token[1]
        key = token[2]
        if piece in music_pieces:
            music_pieces[piece][1] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

sorted_pieces = dict(sorted(music_pieces.items(), key=lambda x: x[0]))
for p, comp in sorted_pieces.items():
    print(f"{p} -> Composer: {comp[0]}, Key: {comp[1]}")
