import re

def tinh_sum (input_string):
    numbers = re.findall(r'-', input_string)
    total_sum = sum(int(num) for num in numbers)

    return total_sum


input_string = input("Nhập chuỗi ký tự: ")
result = tinh_sum (input_string)
print(result)
