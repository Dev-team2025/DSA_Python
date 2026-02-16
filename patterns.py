# for i in range(5):

#     print("* "*i)

n=5

# for i in range(n):
#     val=ord("A")
#     for j in range(n):
#         print(chr(val),end=" ")
#         val+=1
#     print()

# print(chr(23))



for i in range(5):
    for j in range(5):
        if j>=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()