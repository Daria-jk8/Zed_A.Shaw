# Strings, Bytes and Character Encodings
#  python3 23.py utf-8 strict --> in the Terminal
#  python3 23.py utf-16 strict --> in the Terminal

from sys import argv

script, input_encoding, error = argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors) 
    
    print(raw_bytes, "<===>", cooked_string)

languages = open("23.txt", encoding="utf-8")
main(languages, input_encoding, error)    