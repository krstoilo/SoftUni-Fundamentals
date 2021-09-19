string = "Cash$$$$$$Ca$$$$$$sh"

works = False

if 12*"$" in string:
    works = True

if not works:
    print("FAIL")
else:
    print("OK")