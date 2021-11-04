"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    sesli_harfler = "aeiou"
    sayac = 0
    for i in sentence:
        if i in sesli_harfler:
            sayac += 1
    return sayac
