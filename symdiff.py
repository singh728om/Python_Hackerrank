n=int(input())
m=input()
p=int(input())
o=input()
a=(set(m).intersection(set(o))).pop('')
b=set(m).union(set(o))
print(b.discard(a))


#input format

#user input as integer
#user input
#calculate differnece between two input
"""
2
123 1234
2
234 345
 print-->differnece b/w two input """


