import random


def palindrome(word):
    a = list(word)
    #random.shuffle(a)
    print (a)
    #b = a[::-1]
    b = list(reversed(word))
    print(b)
    if a == b:
	    print ("It is a palindrome")
    else:
	    print("Not one")
	
palindrome('malayalam')

word = 'aeioubcdfg'

print (word [:3])
print(word [3:])
l1= [1,4,3,2,0]
l2=[4,65,1,56,90]
l1.extend(l2)
print(sorted(l1))