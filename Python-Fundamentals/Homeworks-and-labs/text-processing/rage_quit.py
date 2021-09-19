user_input = input()
result = ""
unique_chars = []
start = 0
while start < len(user_input)-1:
    sequence = ""
    repeats = ""
    for n in range(start, len(user_input)):
        if not user_input[n].isdigit():
            sequence += user_input[n]
            unique_chars.append(user_input[n].lower())
        else:
            if n == len(user_input)-1:
                repeats += user_input[n]
                start = n+1
                break
            else:
                repeats += user_input[n]
                if not user_input[n+1].isdigit():
                    start = n+1
                    break
    reps = int(repeats)
    result += sequence.upper() * reps

num_unique = len(set(unique_chars))
print(f"Unique symbols used: {num_unique}")
print(result)
