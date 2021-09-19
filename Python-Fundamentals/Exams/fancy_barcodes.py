import re


def is_valid(barcode_text):
    pattern = r"(@#+)([A-Z][a-zA-Z0-9]+[A-Z])(@#+)"
    if re.search(pattern, barcode_text):
        matches = re.findall(pattern, barcode_text)
        if len(matches[0][1]) >= 6:
            return True
    return False


def calculate_product_group(barcode_text):
    pattern = r"(@#+)([A-Z][a-zA-Z0-9]+[A-Z])(@#+)"
    match = re.findall(pattern, barcode_text)
    text = match[0][1]
    pr_group = ""
    for ch in text:
        if ch.isdigit():
            pr_group += ch
    if pr_group == "":
        return "00"
    else:
        return pr_group


n = int(input())
for groups in range(n):
    barcode_text = input()
    if is_valid(barcode_text):
        group = calculate_product_group(barcode_text)
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")