from random import *

# ren luyen su ly list

n = int(input("nhap so phan tu: "))

lst=[0]*n

for i in range(n) :
    lst[i]=randrange(-100,100)


print("list ngau nhien la:" )
print(lst)

print("moi ban them so: ")
value = int(input())
lst.append(value)
print("list moi: ", lst)
