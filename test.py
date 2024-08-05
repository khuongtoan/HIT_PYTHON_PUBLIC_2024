def solution_1 ():
    lst = map ( int, input().split())
    tip = tuple(lst)

    couting = [0]*100000
    for i in tip:
        couting[i]+=1
    for i in range(len(couting)) :
        if couting[i] %5==0 and couting[i] % 10 !=0:
            print(i)


def solution_2():
    x = int(input())
    y =0
    step=0
    while y<x:
        y+=3
        step+=1
    print(step)


def solution_3 ():
    input_string = input()
    unique_elements = set()

    for char in input_string:
        if char != ' ':
            unique_elements.add(char)

    result_list = list(unique_elements)

    print(result_list)


def solution_4():
    lst =[input().split(',')]
    sets =()
    my_lst =[]
    for i in lst :
        for j in len(i):
            sets.__add__(lst[i][j])
    print(sets)





