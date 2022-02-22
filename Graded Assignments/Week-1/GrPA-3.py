#Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
num = input()

d1 = int(num[0])
d2 = int(num[2])
d3 = int(num[4])
d4 = int(num[6])
d5 = int(num[8])

dprod = d1 * d2 * d3 * d4 * d5
print(dprod)
