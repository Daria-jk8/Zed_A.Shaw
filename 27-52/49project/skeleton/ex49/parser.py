class ParserError(Exception):
    pass


class Sentence(object):
    def __init__(self, subject, verb, number, obj):
        # remember we take ("noun", 'princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.number = number[1]
        self.object = obj[1]

    def to_tuple(self):
        return (self.subject, self.verb, self.number, self.object)

    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(word_list, word_type):
        while peek(word_list) == word_type:
            match(word_list, word_type)

    def parse_verb(word_list):
        skip(word_list, "stop")

        if peek(word_list) == "verb":
            return match(word_list, "verb")
        else:
            raise ParserError("Expected a verb next.")

    def parse_numbers(word_list):
        skip(word_list, "stop")

        if peek(word_list) == "number":
            return match(word_list, "number")
        else:
            return ("number", 1)

    def parse_object(word_list):
        skip(word_list, "stop")
        next_word = peek(word_list)

        if next_word == "noun":
            return match(word_list, "noun")
        elif next_word == "direction":
            return match(word_list, "direction")
        else:
            raise ParserError("Expected a noun or direction next.")

    def parse_subject(word_list, subj):
        subj = parse_subject(word_list)
        verb = parse_verb(word_list)
        obj = parse_object(word_list)

        return Sentence(subj, verb, obj)

    def parse_sentence(word_list):
        skip(word_list, "stop")
        next_word = peek(word_list)

        if next_word == "noun":
            subj = match(word_list, "noun")
            return parse_subject(word_list, subj)
        elif next_word == "verb":
            return parse_subject(word_list, ("noun", "player"))
        else:
            raise ParserError("Must start with noun or verb, not: %s" % next_word)
