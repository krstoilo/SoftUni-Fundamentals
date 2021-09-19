def calc_index(input_num):
    result = 0
    for n in input_num:
        result += int(n)
    return result


list_nums = input().split()
text = input()
new_str = ""

for n in range(len(list_nums)):
    index = calc_index(list_nums[n])
    text_pos = 0
    for k in range(index):
        text_pos += 1
        if text_pos >= len(text):
            text_pos = 0
    new_str += text[text_pos]
    text = ''.join([text[i] for i in range(len(text)) if i != text_pos])

print(new_str)