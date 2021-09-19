import re

text = input()
title_pattern = r"<title>(.+)</title>"
content_pattern = r"<body>(.+)</body>"
title = re.findall(title_pattern, text)
content = re.findall(content_pattern, text)
title_str = title[0]
content_str = content[0]


def remove_tags(text):
    pattern_tags = r"(<.+?>)"
    n_tag = r"(\\n)"
    tags = list(re.findall(pattern_tags, text))
    if re.search(n_tag, text):
        tags.append(r"\n")
    refined_text = text
    for tag in tags:
        if tag in text:
            refined_text = refined_text.replace(tag, "")
    return refined_text


print(f"Title: {remove_tags(title_str)}")
print(f"Content: {remove_tags(content_str)}")


