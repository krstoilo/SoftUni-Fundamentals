def ascii_print(start_char, end_char):
    for n in range(ord(start_char)+1, ord(end_char)):
        print(chr(n), end=" ")


char1 = input()
char2 = input()

ascii_print(char1, char2)