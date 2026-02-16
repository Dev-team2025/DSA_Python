# Bubble Sort 
# time complexity is O(n*n)
# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(n):
#     for j in range(n-i-1):
#         if my_array[j]>my_array[j+1]:
#             my_array[j],my_array[j+1]=my_array[j+1],my_array[j]
# print(my_array)

# Quick Sort 
# divide one neutral lesses num on left greater num on right side and after that combine all three with less + nutral + greater
# def quicksort(arr):
#    if len(arr)<=1:
#        return arr
#    else:
#         pivot=arr[0]
#         less_arr=[]
#         more_arr=[]
#         for i in arr[1::]:
#             if i<=pivot:
#                 less_arr.append(i)
#             else:more_arr.append(i)
#         return quicksort(less_arr) + [pivot] + quicksort(more_arr)

# l=[12,23,3,2,3,4,23,3,234]
# rep=[]
# for i in l:
#     if i not in rep:
#         rep.append(i)
# print(rep)

# Merge Sort 
def mergesort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Step 1: Divide
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    # Step 2: Merge
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# Example
arr = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(arr))
