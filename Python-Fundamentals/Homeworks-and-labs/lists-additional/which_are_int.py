first_string = input().split(", ")
second_string = input().split(", ")


def substrings_return(string1, string2):
    new_str = []
    for elem in string1:
        for el in string2:
            if elem in el:
                new_str.append(elem)
                break
    return new_str


print(substrings_return(first_string, second_string))