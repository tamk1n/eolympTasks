def spin_words(sentence):
#sentence = "My name is Tamkin"
    sentList=sentence.split()
    newSent =[]

    for word in sentList:
        if len(word) >4:
            wordList = []
            for letter in word:
                wordList.append(letter)
            wordList.reverse()
            rWord =""
            for rletter in wordList:
                rWord+=rletter
            newSent.append(rWord)
        else:
            newSent.append(word)

    new = " ".join(newSent)
    return new