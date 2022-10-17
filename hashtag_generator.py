def generate_hashtag(sentence):
    if len(sentence.strip()) ==0:
        return False
    titled = sentence.title().strip()
    list = titled.split()
    list.insert(0,"#")
    hashtag = "".join(list)
    if len(hashtag) >140:
        return False
    return hashtag

print(generate_hashtag(""))