# A function for shuffling list items.
from random import randint
bek = ['ka', 'op', 'be', 'ri']
def randomShuffle(list):
    for i in range(len(list)**2):
        index1 = randint(0, len(list) - 1)
        index2 = randint(0, len(list) - 1)
        value1 = list[index1]
        list[index1] = list[index2]
        list[index2] = value1
    print(list)
randomShuffle(bek)
