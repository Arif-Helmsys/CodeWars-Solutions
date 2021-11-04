"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples

`pig_it('Pig latin is cool') # igPay atinlay siay oolcay`
`pig_it('Hello world !')     # elloHay orldway !`
"""

def pig_it(text):
    text = text.split()
    count = 0
    string = ""
    for i in text:
        string += str(text[count][1:])+f"{i[0]}ay "
        count += 1
    return string.rstrip(" ").replace("!ay","!").replace("ay!","!").replace("?ay","?").replace("ay?","?").replace("ay.",".").replace(".ay",".")
