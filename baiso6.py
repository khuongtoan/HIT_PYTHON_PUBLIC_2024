def ewo (matrix):
    new_matrix =[]
    for j in range(len(matrix[0])):
        rows= []
        for i in range(len(matrix)):
            rows.append( matrix[i][j] )
        new_matrix.append(rows)
    return new_matrix

def calculator (operator , *args):
    if operator =='add':
        return sum(args)
    elif operator =="multiply":
        result = 1
        for i in args:
            result *= i
        return result
    elif operator == "max":
        return max(args)
    elif operator == "min":
        return min(args)
    else :
        return "Invalid operator"


## ---------------------------------------------------------
def sum_charater (a):
    sum=0
    while a > 0:
        sum+=a%10
        a//=10
    return sum

def count_step(n):
    step =0
    while n>=10:
        n=sum_charater(n)
        step+=1
    return step, n

def format_phone_number (strings ):
    new_phone=""
    for i in strings :
        if i.isdigit():
            new_phone+=i
    if len(new_phone) != 10:
        return 'invalid phone'
    if new_phone[0] != "0":
        return "invalid phone"
    return new_phone

sa = "012s54dfsafh df +fgss89"
print(format_phone_number(sa))