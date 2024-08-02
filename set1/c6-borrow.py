# https://cedricvanrompay.gitlab.io/cryptopals/challenges/01-to-08.html

from c4 import get_remote_content
import base64

def bxor(a, b):
    "bitwise XOR of bytestrings"
    return bytes([ x^y for (x,y) in zip(a, b)])

def hamming_distance(a, b):
    return sum(bin(byte).count('1') for byte in bxor(a,b))

def score_vigenere_key_size(candidate_key_size, ciphertext):
    # as suggested in the instructions,
    # we take samples bigger than just one time the candidate key size
    slice_size = 2*candidate_key_size

    # the number of samples we can make
    # given the ciphertext length
    nb_measurements = len(ciphertext) // slice_size - 1

    # the "score" will represent how likely it is
    # that the current candidate key size is the good one
    # (the lower the score the *more* likely)
    score = 0
    for i in range(nb_measurements):

        s = slice_size
        k = candidate_key_size
        # in python, "slices" objects are what you put in square brackets
        # to access elements in lists and other iterable objects.
        # see https://docs.python.org/3/library/functions.html#slice
        # here we build the slices separately
        # just to have a cleaner, easier to read code
        slice_1 = slice(i*s, i*s + k)
        slice_2 = slice(i*s + k, i*s + 2*k)

        score += hamming_distance(ciphertext[slice_1], ciphertext[slice_2])

    # normalization: do not forget this
    # or there will be a strong biais towards long key sizes
    # and your code will not detect key size properly
    score /= candidate_key_size
    
    # some more normalization,
    # to make sure each candidate is evaluated in the same way
    score /= nb_measurements

    return score

def find_vigenere_key_length(ciphertext, min_length=2, max_length=30):
    # maybe this code is a bit over-sophisticated
    # it just outputs the key size for wich
    # the score at the "score_vigenere_key_size" function is the *lowest*
    key = lambda x: score_vigenere_key_size(x,ciphertext)
    return min(range(min_length, max_length), key=key)

q=get_remote_content('https://cryptopals.com/static/challenge-data/6.txt')
q=base64.b64decode(q)


print(find_vigenere_key_length(q))