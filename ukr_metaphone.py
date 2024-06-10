import re as re

substitutions = {
    r"(^| |['’ʼ`])я": "ja",
    r"(^| |['’ʼ`])[єї]": "ji",
    r"(^| |['’ʼ`])(йо|ю)": "ju",
    r"дж": "x",
    r"дз": "s",
    r"(['’ʼ`]|ь)": "",
    r"[ая]": "a",
    r"[бп]": "p",
    r"[вф]": "f",
    r"[гґх]": "h",
    r"[дт]": "t",
    r"[еиієї]": "i",
    r"[жчшщ]": "x",
    r"[зсц]": "s",
    r"[мн]": "n",
    r"[оую]": "u",
    r"й": "j",
    r"к": "k",
    r"л": "l",
    r"р": "r",
}

def pron(word: str):
    word = word.lower()
    for find, repl in substitutions.items(): # consonant substitution
        word = re.sub(find, repl, word)
    return word.upper()

print(pron(str(input("Enter a word: "))))