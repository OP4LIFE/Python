'''
The function simulates the reverse() list method.
If we, for example, have a list list1 = ['0', '1', '2', '3'],
the function will duplicate the first half of the list 
and reassign the values in two halves as follows:
list1[0] = list1[3] 
list1[1] = list1[2] 
# And then it switches to the duplicated list.
list1[2] = list2[1] 
list1[3] = list2[0] 
 
'''
def reverse(list1):
    # Duplication
    list2 = list1[:round(len(list1) / 2)]
    # Reassingation
    for i in range(0, len(list1)):
        if i < len(list1) / 2:
            list1[i] = list1[len(list1) - 1 - i]
        elif i != len(list1) / 2:
            list1[i] = list2[len(list1) - 1 - i]

''' 
The upper program can also achieve the results only by
duplicating the original list and reassigning all values.
'''
def reverse2(list1):
#    list2 = list1
    list2 = list1[:]
    for i in range(0, len(list1)):
        list1[i] = list2[len(list1) - 1 - i]
   
li = [0, 1, 2, 3, 4, 5, 6]
reverse(li)
print('Using reverse(): ' + str(li))
reverse(li)
reverse2(li)
print('Using reverse2(): ' + str(li))

'''
Misunderstanding accured at line 28, where I thought the statement
created a new object, not just a referetion to the same one.
'''
