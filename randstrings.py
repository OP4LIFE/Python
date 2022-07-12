import string, random

# Min, max word length
wlen = [int(input("Minimun word lenght: ")), int(input("Maximum word length: "))]
# Max list length
llen = int(input("Maximum list length: "))


alphabet = list(string.ascii_lowercase)
randlist = []
for u in range(llen):
    randword = ''
    for i in range(random.randint(wlen[0], wlen[1])):
        randletter = alphabet[random.randint(1, len(alphabet) - 1)]
        randword += randletter
    
    randlist.append(randword)
    
for word in randlist:
    print(word)

