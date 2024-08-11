from random import *
import pprint

def bai_1 ( ):
    students = {
        'SV001': 3.2,
        'SV002': 2.8,
        'SV003': 3.6,
        'SV004': 3.4,
        'SV005': 1.9,
        'SV006': 3.0,
    }
    count_stdents = sum(3<=diem<=3.5 for diem in students.values() )
    print("so sv co diem thoa man: ",count_stdents)
    students["sv007"] = 3.8

    students = {k:v for k,v in students.items() if v>=2.0}
    print(students)

def solutoin_2():
    string1 = input()
    count_char = {}
    for char in string1 :
        if char in count_char:
            count_char[char]+=1
        else :
            count_char[char]=1
    print(count_char)

def solution_3():
    n = int(input("n= "))

    list_password = ["CNTT", "KHMT", 'KTPM', "HTTT"]
    x= 2023600000
    account = {}

    for i in range ( 1, n+1):
        ten_tk= x+i
        matkhau = choice(list_password)+str(ten_tk)
        account[f"account{i}"] = {
            "username": ten_tk,
            "password": matkhau
        }
    aa = pprint.PrettyPrinter(indent =4)
    aa.pprint(account)

def solutions_4 ():
    dic = {
        "n":1500,
        "m": 2,
        "CLUSTERS":3,
        "ITER":10000,
        "METHOD":"FCM",
        "MEASURE":"EUCLIDEAN",
        "YEARS":51,
    }
    aa =pprint.PrettyPrinter(indent = 4 )
    aa.pprint(dic)
    dic["MEASURE"]="MANHATAN"
    print(dic["METHOD"] )
    dic["LOSS FUNCTION"] ="NORM_2"
    aa.pprint(dic)
    del dic["YEARS"]
    sti= input("nhap vao xau: ")
    for  v , i in dic.items():
        if sti == str(i):
            print('s trùng với giá trị của: ', v )
    ss = {value for value in dic.values()}
    lst= [value for value in dic.values()]
    print("set: ", ss)
    print("list: ", lst)






solutions_4()