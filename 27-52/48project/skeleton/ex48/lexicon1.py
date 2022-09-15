WORD_TYPES = {
    "north": "direction",
    "south": "direction",
    "east": "direction",
    "west": "direction",
    "down": "direction",
    "up": "direction",
    "left": "direction",
    "right": "direction",
    "back": "direction",
    "go": "verb",
    "kill": "verb",
    "eat": "verb",
    "stop": "verb",
    "the": "stop",
    "in": "stop",
    "of": "stop",
    "from": "stop",
    "at": "stop",
    "it": "stop",
    "bear": "noun",
    "princess": "noun",
    "door": "noun",
    "cabinet": "noun",
    1234: "number",
    3: "number",
    91234: "number",
}

user_input = input("> ")


def convert_number(word):
    try:
        return int(word)
    except:
        return None


def scan(sentence):
    words = sentence.split()
    results = []

    for word in words:
        word_type = WORD_TYPES.get(word)

        if word_type == None:
            # it might be a number, so try converting
            number = convert_number(word)

            if number != None:
                results.append(("number", number))
            else:
                results.append(("error", word))
        else:
            results.append((word_type, word))
    return results


scan(user_input)
