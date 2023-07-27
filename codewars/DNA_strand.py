def DNA_strand(dna):
    lst = []
    for i in range (len(dna)):
        if dna[i] == "A":
            lst.append("T")
        elif dna[i] == "T":
            lst.append("A")
        elif dna[i] == "C":
            lst.append("G")
        else:
            lst.append("C")
    return ''.join(lst)