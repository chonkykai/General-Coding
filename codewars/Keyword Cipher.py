def keyword_cipher(msg, keyword):
    msg = msg.lower()

    standard_key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'
                    ,'q','r','s','t','u','v','w','x','y','z',' ']
    ls = [x for x in keyword]
    ls = list(dict.fromkeys(ls))
    cyper_key = ls + standard_key
    cyper_key = list(dict.fromkeys(cyper_key))

    ms = [x for x in msg]
    jumbled_numbers = []
    for i in range (len(ms)):
        jumbled_numbers.append(standard_key.index(ms[i]))

    jumbled_alp = []
    for i in range (len(jumbled_numbers)):
        jumbled_alp.append(cyper_key[jumbled_numbers[i]])
    jumbled_output = ''.join(jumbled_alp)
    return jumbled_output