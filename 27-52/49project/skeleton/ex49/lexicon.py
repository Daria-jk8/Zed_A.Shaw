"""
directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "kill", "eat", "stop"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["bear", "princess", "door", "cabinet"]
# numbers = [1234, 3, 91234]


def scan(input):
    words = input.split()
    operation = ""
    sentence = []

    for word in words:
        if word in directions:
            operation = "direction"
        elif word in verbs:
            operation = "verb"
        elif word in stop_words:
            operation = "stop"
        elif word in nouns:
            operation = "noun"
        elif convert_number(word):
            operation = "number"
            word = convert_number(word)
        else:
            operation = "error"
        sentence.append(operation, word)

    return sentence


def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None
"""


def scan(input):
    lexicon = {
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
    }

    sentence = []
    words = input.split()

    for word in words:
        if word.isdigit():
            word = int(word)
            sentence.append(("number", word))
        elif word in lexicon.keys():
            sentence.append((lexicon[word], word))
        else:
            sentence.append(("error", word))

    return sentence
