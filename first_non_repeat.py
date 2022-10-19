def first_non_repeating_letter(string):
    if len(string)==0:
        return ""
    
    else:
        for letter in string:
            if string.lower().count(letter.lower()) == 1:
                return letter
                break
        return ""