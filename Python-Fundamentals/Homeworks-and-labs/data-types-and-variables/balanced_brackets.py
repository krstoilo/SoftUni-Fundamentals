n = int(input())
stack = []
is_balanced = True

for lines in range(1, n+1):
    string = input()
    if not stack:
        if string == "(":
            stack.append(string)
        elif string == ")":
            is_balanced = False
    else:
        if string == "(":
            is_balanced = False
        elif string == ")":
            stack.pop()

if not stack and is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')