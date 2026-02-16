# n=5
# def Recur(n):
#     if n<0:
#         return 0
#     else:
#         return n+(Recur(n-1))
    
# obj=Recur(n)
# print(obj)

# arr= [19,21,12,432,12,2,12,324,432,232]
# minval=arr[0]
# for i in arr:    
#     if i < minval:
#         minval = i      
# print(minval) 

# # LArgest Element in an Array0
# # Input: [3, 7, 2, 9, 4]
# # Output: 9

# num = [3, 7, 2, 9, 4]
# minval = num[0]
# for i in num:
#     if i>minval:
#         minval=i
# print(minval)

# Input: [1, 2, 3, 4, 5]
# Output: True         
            
L=[2,7,11,15]
op=18
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]+L[j]==op:
            print(i,j)


