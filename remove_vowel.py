def removevowel(sentence):
  sentenceList = []
  
  vowels = [ "a", "e", "i", "o", "u"]
  
  for letter in sentence:
    sentenceList.append(letter)
  
  newSentence = ""
  
  for letter in sentenceList:
    for vowel in vowels:
      if letter.upper() == vowel.upper():
        sentenceList.remove(letter)
  newSentence=newSentence.join(sentenceList)
  return newSentence

print(removevowel("My name is Tamkin"))