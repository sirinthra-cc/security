import hashlib
import timeit


def find_password(hashed_string):
    f = open('./words.txt', 'r', encoding='utf-8')
    for line in f:
        word = line.rstrip()
        digested_word = hashlib.md5(str.encode(word)).hexdigest()
        if digested_word == hashed_string:
            return word

password = find_password('e91e6348157868de9dd8b25c81aebfb9')
print(password)

