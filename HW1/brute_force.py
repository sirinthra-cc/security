import hashlib
import timeit


allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def gen_and_check(hashed_string, previous_string, current_length, total_length):
    if current_length == total_length:
        digest_word = hashlib.md5(str.encode(previous_string)).hexdigest()
        if digest_word == hashed_string:
            return previous_string
    else:
        for char in allowed_chars:
            current_string = previous_string + char
            # print(current_string)
            gen_and_check(hashed_string, current_string, current_length+1, total_length)


def find_password(hashed_string, max_length):

    pwd = ""
    i = 1
    start = timeit.default_timer()
    while i <= max_length:
        pwd = gen_and_check(hashed_string, "", 0, i)
        i += 1
    stop = timeit.default_timer()
    print("run time:", stop - start)

    if pwd is not None:
        print(pwd)
    else:
        print("There are no string in this length match this hash code.")


find_password('e91e6348157868de9dd8b25c81aebfb9', 4)
# print(password)
