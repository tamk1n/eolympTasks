def count(string):
    result = {}

    for letter in string:
        count = string.count(letter)
        result[letter] = count
    return result

print(count("AsjfhaaFssS"))