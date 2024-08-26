def sohh(number):
    total =0
    while number >0:
        total += number%10
        number //=10
    return total==10

x = int(input("n="))

lst = []
for i in range(1000000):
    if sohh(i) == True:
        lst.append(i)
print(lst[x-1])

