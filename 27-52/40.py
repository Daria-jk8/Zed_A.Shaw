# Modules, Classes, and Objects

# Modules Are Like Dictionaries

# dict style
mystuff = {"apple": "I AM APPLES!"}
print(mystuff["apple"])

# module style
def apple():
    print("I AM APPLES_f!")


a = apple()

# class style
class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand year between."

    def apple(self):
        print("I AM CLASSY APPLES!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(
    ["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]
)

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
