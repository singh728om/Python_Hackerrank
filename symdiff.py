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

