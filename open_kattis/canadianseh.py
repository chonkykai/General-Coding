statement = input("")
statement = statement.split(" ")
if "eh?" == statement[len(statement)-1]:
    print("Canadian!")
else:
    print("Imposter!")