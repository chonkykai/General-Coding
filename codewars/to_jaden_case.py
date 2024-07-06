def to_jaden_case(string):
    string = string.split(" ")
    for i in range (len(string)):
        string[i] = string[i].capitalize()
    
    final = ' '.join(string)
    return final