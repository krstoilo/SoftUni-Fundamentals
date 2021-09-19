import re


def find_mirrors(matched_words):
    mirrors = []
    for entry in matched_words:
        if entry[1] == entry[2][::-1]:
            mirrors.append(entry[1])
    return mirrors


text_string = input()
pattern = r"(@|#)([A-Za-z]+)\1\1([A-Za-z]+)\1"
if re.search(pattern, text_string):
    matches = re.findall(pattern, text_string)
    print(f"{len(matches)} word pairs found!")
    mirror_words = find_mirrors(matches)
    if len(mirror_words) == 0:
        print("No mirror words!")
    else:
        print("The mirror words are:")
        final_words = ""
        for word in mirror_words:
            final_words += f"{word} <=> {word[::-1]}, "
        print(final_words[:len(final_words)-2])
else:
    print("No word pairs found!")
    print("No mirror words!")