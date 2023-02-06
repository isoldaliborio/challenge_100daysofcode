
string_variable = "a2jkftn"

new_alphabeth={
    "a":"b",
    "b":"c",
    "c":"d",
    "d":"E",
    "e":"f",
    "f":"g",
    "g":"h",
    "h":"I",
    "i":"j",
    "j":"k",
    "k":"l",
    "l":"m",
    "m":"n",
    "n":"O",
    "o":"p",
    "p":"q",
    "q":"r",
    "r":"s",
    "s":"t",
    "t":"U",
    "u":"w",
    "w":"v",
    "v":"x",
    "x":"y",
    "y":"z",
    "z":"a",
}

new_string = []
for character in string_variable:
    if character in new_alphabeth:
        letters = new_alphabeth[character]
        new_string.append(letters)
    else:
        new_string.append(character)

print("".join(new_string))

# --- .join --- transform a list into a string
# --- .split --- transform a string into a list
    
