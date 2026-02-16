'''Find the sum of all elements in a list

Find the largest and smallest element

Count even and odd numbers

Reverse a list (without using reverse())

Check if a list is sorted

Find the second largest element

Remove duplicates from a list

Count frequency of each element

Find all elements greater than a given number

Merge two lists

Check if an element exists in a list

Find the index of an element

Rotate list left by 1

Rotate list right by 1

Print elements at even indices'''

# -------------------EASY------------------
# Find the largest and smallest element
''''l=[120,213,2,1,23,-10,1231]
maxVal=l[0]
minVal=l[0]
for i in l:
    if i>maxVal:
        maxVal=i
    else:
        minVal=i
print(f"max val->{maxVal} and  min val->{minVal}")'''

# sort a list
'''l=[120,213,2,1,23,-10,1231]
sortedList=[]
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''

# Find the second largest element
'''l=[120,213,2,1,23,-10,1231]
sort=sorted(l,reverse=True)
print(sort[-2])'''

# Count frequency of each element
'''l=[12,3,1,3,2,231,12,2,23,-100]
freq={}
count=0
for i in l:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)'''

# Find intersection of two lists
'''l1=[12,2,12,3,21,73,32,12,2]
l2=[21,12,23,6,9]
for i in l1:
    if i in l2:
        print(i)
    '''    

# ----------------MEDIUM--------------
# Rotate list by K positions
'''l=[10,20,30,40,70]
k=2
k
print(l[-k:]+l[:-k])'''


# Find missing number in a list of 1…N

# Move all zeros to the end
'''l=[12,23,2,0,1,23,0,23]
for i in l:
    if i==0:
        l.remove(i)
        l.append(i)
print(l)'''

# Find all pairs with given sum
'''l=[12,23,5,23,4,7,9,6,3,1]
res=9
sub=set()
for i in l:
    if res-i in sub:
      print(res-i,i)
    sub.add(i)  '''
            
        
        
lst = [2,2,3,3,1,2,3,2,2]
new=set()
count=0
for i in lst:
    ele=0
    
    if i in new:
        count+=1
    new.add(i)
    if count>ele:
        print(i)

