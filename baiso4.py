def Bai_1():
    tuple_old = ('0','4','5','6','8')
    new_tuple = tuple(int(x) for x in tuple_old )
    TBC = sum(new_tuple)/len(new_tuple)
    print(TBC)

def bai_2 ():
    Table_1 = {3,4,5,7, 8}
    Table_2 = {3, 4, 8, 5, 45}
    print("ban so 1: ")
    for i in Table_1 :
        print(i,end=' ')

    print("\nban so 2: ")
    for i in Table_2 :
        print(i,end=' ')
    print()
    union_set = Table_1.union(Table_2)
    if len(union_set) != 0:
        print("có sinh viên đăng kí cả 2 bàn")
        print("các sinh viên đăng kí tại cả 2 bàn là ")
        print(union_set)
    print("các sinh viên đăng kí tại bàn 1 mà không đăng kí ở bàn 2 là ")
    dif_Set = Table_1.difference(Table_2)
    print(dif_Set)
def bai_3 ():
    n,m= map(int, input("nhap n va m: ").split())
    set_1 = set(map(int,input("nhap vao day so: ").split()))
    set_a = set(map(int,input("nhap vao A: ").split()))
    set_b = set(map(int,input("nhap vao B: ").split()))
    gol_H  = 0
    for i in set_1:
        if i in set_a :
            gol_H+=1
        if i in set_b:
            gol_H -=1
    print(gol_H)

def bai_4 ():
    ra = int(input("nhap n: "))
    set_input= set(map(int,input("nhap vao tap hop: ").split()))
    lst = list(set_input)
    max_type = int(input("nhap vao sum max: "))
    lst.sort()
    sum_current =0
    for an in lst:
        sum_current+=an
        if sum_current> max_type:
            break
        print(an,end=' ')

def bai_5 ():
    n = int(input("Nhập số lượng xâu ký tự: "))
    a = [input(f"Nhập xâu ký tự thứ {i + 1}: ").strip() for i in range(n)]
    b = tuple(a)
    count_numbers = sum(1 for item in b if item.isdigit())
    print("Tuple:", b)
    print("Số lượng phần tử có dạng số:", count_numbers)

