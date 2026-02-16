# a=10
# b=20
# # print(a+b)

# # in not in
# l=[10,20,30]
# print(50 not in l) #true
# print(10 in l) #True

# identity
# a=10
# b=10

# print(a is not b)

# if condition:
#     statement
# a=100
# if(a>10):
#     print("true")
# elif (a<20 ):print("its is not")
# else:print("false")

# loops
# -10 0 +10
# 1 start index 10 end index 2 step counter
# l=[10,20,30,40]
# for i in l:
#     print(i)

# for i in range(5):
#     for j in range(i):
#         print("* "*i+1)


for i in range(5):
    for j in range(5):
        print( "* ",end=" ")
    print()

val=ord("A")
for i in range(5):
    for j in range(5):
        print(chr(val),end=" ")
        val+=1
        if val>ord("Z"):
            val=ord("A")
    print()

n=5
for i in range(5):
    for j in range(5):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for i in range(n):
    for j in range(n-i):
        print("* ",end=" ")
    print( )

for i in range(n):
    for j in range(n):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n):
    for j in range(n+i):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()