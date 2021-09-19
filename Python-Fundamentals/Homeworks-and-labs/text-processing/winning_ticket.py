import re
tickets_input = input().split(", ")
clean_tickets = []
for entry in tickets_input:
    new_word = re.sub(' +', "", entry)
    clean_tickets.append(new_word)

for ticket in clean_tickets:
    if len(ticket) != 20:
        print("invalid ticket")
    else:
        if 20*"@" in ticket:
            print(f'ticket "{ticket}" - 10@ Jackpot!')
        elif 20*"#" in ticket:
            print(f'ticket "{ticket}" - 10# Jackpot!')
        elif 20*"$" in ticket:
            print(f'ticket "{ticket}" - 10$ Jackpot!')
        elif 20*"^" in ticket:
            print(f'ticket "{ticket}" - 10^ Jackpot!')
        else:
            left_side = ticket[:10]
            right_side = ticket[11:]
            if 6*"@" in left_side and 6*"@" in right_side:
                print(f'ticket "{ticket}" - 6@')
            elif 6*"#" in left_side and 6*"#" in right_side:
                print(f'ticket "{ticket}" - 6#')
            elif 6 * "^" in left_side and 6 * "^" in right_side:
                print(f'ticket "{ticket}" - 6^')
            elif 6 * "$" in left_side and 6 * "$" in right_side:
                print(f'ticket "{ticket}" - 6$')
            elif 7*"@" in left_side and 7*"@" in right_side:
                print(f'ticket "{ticket}" - 7@')
            elif 7*"#" in left_side and 7*"#" in right_side:
                print(f'ticket "{ticket}" - 7#')
            elif 7*"^" in left_side and 7*"^" in right_side:
                print(f'ticket "{ticket}" - 7^')
            elif 7*"$" in left_side and 7*"$" in right_side:
                print(f'ticket "{ticket}" - 7$')
            elif 8 * "@" in left_side and 8 * "@" in right_side:
                print(f'ticket "{ticket}" - 8@')
            elif 8 * "^" in left_side and 8 * "^" in right_side:
                print(f'ticket "{ticket}" - 8^')
            elif 8*"$" in left_side and 8*"$" in right_side:
                print(f'ticket "{ticket}" - 8$')
            elif 8*"#" in left_side and 8*"#" in right_side:
                print(f'ticket "{ticket}" - 8#')
            elif 9 * "@" in left_side and 9 * "@" in right_side:
                print(f'ticket "{ticket}" - 9@')
            elif 9*"#" in left_side and 9*"#" in right_side:
                print(f'ticket "{ticket}" - 9#')
            elif 9*"^" in left_side and 9*"^" in right_side:
                print(f'ticket "{ticket}" - 9^')
            elif 9*"$" in left_side and 9*"$" in right_side:
                print(f'ticket "{ticket}" - 9$')
            else:
                print(f'ticket "{ticket}" - no match')



