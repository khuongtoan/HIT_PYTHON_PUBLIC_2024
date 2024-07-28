#bai 1

def bai_1 ():
    n= int(input("n= "))
    lst = [int(input()) for i in range(n) ]
    print( lst)

    print("so lan xuat hien cua x:",lst.count())

    replace_element = [8, 5, 4, 0, 1, 3]
    if len(lst) >=8:
        lst[2:8]= replace_element
    print(lst)

    max_value = max (lst)
    min_value = min(lst)
    print("gia tri lon nhat va nho nhat la:",max_value, min_value)

    y =int(input("nhap so y can chen: "))
    lst.insert(0,y)

    ## kiem tra tang, giam dan
    if all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)):
        print("TĂNG")
    elif all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)):
        print("GIẢM")
    else:
        print("NO")

    new_aray =[sum(lst[:i]) for i in range (1,len(lst)+1 ) ],
    print(new_aray)

    my_list =[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
    my_lst = sorted(my_list)
    print(my_lst)
    he_lst = sorted(my_list,key= abs )

def bai_2 ():
    k = int(input("nhap vao so luong phan tu: "))
    a = [int(input(f"nhap vao phan tu thu {i+1}= ")) for i in range (k) ]
    n = int(input("nhap vao n: "))
    m = int(input("nhap vao m: "))

    index=0
    if n*m<= k:
        '''
        lst= []
        for i in range (n):
            rows =[]
            for j in range (m):
                rows.append(a[index])
                index+=1
            lst.append(rows)
        '''
        lst = [[a[i*m+j] for j in range (m)]for i in range (n)]
        print(lst)
    else :
        print("NO")

#bai 3
def bai_3 ():
    x = int(input("len(list1)= "))
    lst1 = [int(input) for i in range (x)]
    y = int(input("len(list2)= "))
    lst2 = [int(input) for i in range(y)]
    print(lst1.reverse())
    lst1.reverse()

    a,b = map(int, input(f"{x}<= a < b <= {y}").split())
    print(lst2[a:b].reverse())
    lst2[a:b].reverse()

    lst3=[]
    for i in range (x) :
        if i%2 ==0:
            lst3.append(lst1[i])
    print (lst3)

    lst4=[]
    index =0
    for i in range (x):
        lst4.append(lst1[i])
        lst4.append(lst2[i])
        index+=1
    while index < len[lst2]:
        lst4.append(lst2[index])
    tmp =[0]

    lst1[0],lst2[0]= lst2[0],lst1[0]
def  bai_4 ():
    strings = input("nhap vao ho va ten: ")
    lst_lower = strings.lower()
    lst = lst_lower.split()

    lst_e = [i.capitalize() for i in lst ]
    result = ' '.join(lst_e)
    print(result)

def bai_5():
    n = int(input("n="))
    so_nguyen = list(map(int, input("Nhập các số nguyên : ").split()))
    lst_like =[]
    so_thich = [1, 3, 5, 7, 9]

    like_number = [num for num in so_nguyen if num%10 in so_thich ]
    like_number.sort()
    print(len(like_number) )
    for i in like_number :
        print(i,end=" ")

