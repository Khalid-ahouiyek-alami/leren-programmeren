def rainbow_text(text):
    color_codes = [31, 33, 32, 36, 34, 35]
    result = ""
    for i, char in enumerate(text):
        result += "\033[1;{}m{}\033[0m".format(color_codes[i % len(color_codes)], char)
    return result

print(rainbow_text("khalid maak je huiswerk!"))
