def spin_words(sentence):
    sentList=sentence.split()
    newSent =[]

    for word in sentList:
        if len(word) >4:
            revWord = word[::-1]
            newSent.append(revWord)
        else:
            newSent.append(word)

    new = " ".join(newSent)
    return new