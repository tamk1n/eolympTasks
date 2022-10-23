import string
alphabet = string.ascii_lowercase

alph = list(alphabet)
def rot13(example):
    rot = ""

    for x in example:
        if x.lower() in alph and alph.index(x.lower())+13 < 26:
            rot+= alph[alph.index(x.lower())+13] if x == x.lower() else alph[alph.index(x.lower())+13].upper()
        elif x.lower() in alph and alph.index(x.lower())-13 > -1:
            rot+= alph[alph.index(x.lower())-13] if x == x.lower() else alph[alph.index(x.lower())-13].upper()
        else:
            rot+=x
    return rot

print(rot13("tamKinn 67__altI $$"))