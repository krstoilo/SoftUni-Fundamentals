def return_characters(first_symbol, last_symbol):
    chr_string = ""
    for i in range(ord(first_symbol)+1, ord(last_symbol)):
        chr_string += chr(i) + " "
    return chr_string


sym_1 = input()
sym_2 = input()


print(return_characters(sym_1, sym_2))