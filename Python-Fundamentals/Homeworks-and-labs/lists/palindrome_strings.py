words_input = input().split()
searched_word = input()


def is_palindrome(str_input):
    return str_input == str_input[::-1]


def count_occurences(str_input, searched):
    counter = 0
    for i in range(len(str_input)):
        if str_input[i] == searched:
            counter += 1
    return counter


palindromes = [word for word in words_input if is_palindrome(word)]
count = count_occurences(words_input, searched_word)

print(palindromes)
print(f"Found palindrome {count} times")
