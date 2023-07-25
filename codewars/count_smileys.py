def count_smileys(arr):
    smiley = []
    eyes = [':', ';']
    nose = ['-', '~']
    mouth = [')', 'D']
    for i in arr:
        if len(i) == 3:
            if i[0] in eyes:
                if i[1] in nose:
                    if i[2] in mouth:
                        smiley.append(i)
        else:
            if i[0] in eyes:
                if i[1] in mouth:
                    smiley.append(i)
    return len(smiley)



print(count_smileys([':)', ';(', ';}', ':-D']))

print(count_smileys([';D', ':-(', ':-)', ';~)']))

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))