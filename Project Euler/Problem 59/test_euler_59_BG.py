import pytest
import euler_59_BG as sut

def test_check_password():
    password = ord('a') + ord('a') + ord('a')
    string = [ord('a'), ord('n'), ord('d')]
    encrypted_string = [char^password for char in string]
    assert(sut.check_password(password, encrypted_string) == True)


def test_bad_pass_check_password():
    password = ord('a') + ord('a') + ord('a')
    string = [ord('a'), ord('n'), ord('d')]
    bad_password = password = ord('a') + ord('a') + ord('z')
    encrypted_string = [char ^ password for char in string]
    assert(sut.check_password(bad_password, encrypted_string) == False)


def test_bad_string_check_password():
    password = ord('a') + ord('a') + ord('a')
    string = [ord('a'), ord('d'), ord('d')]
    encrypted_string = [char ^ password for char in string]
    assert(sut.check_password(password, encrypted_string) == False)

def test_in():
    decrypted_string = "and"
    commom_words = ["and", "the", "or"]
    answer = False
    for word in commom_words:
        if decrypted_string.find(word):
            answer = True
    assert(answer)


