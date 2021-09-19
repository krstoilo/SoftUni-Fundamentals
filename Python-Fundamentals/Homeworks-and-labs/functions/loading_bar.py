progress_number = int(input())


def loading_bar(number):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f'{number}%', end=" ")
        string_bar = "["
        for n in range(number//10):
            string_bar += "%"
        for n in range(number//10, 10):
            string_bar += "."
        string_bar += "]"
        print(string_bar)
        print("Still loading...")


loading_bar(progress_number)
