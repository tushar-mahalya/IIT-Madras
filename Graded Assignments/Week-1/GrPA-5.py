#Accept two positive integers x and y as input. Print the number of digits in xy. You should be able to solve this problem using the concepts covered in week-1
x = int(input())
y = int(input())
res = x ** y
res_str = str(res)
print(len(res_str))
