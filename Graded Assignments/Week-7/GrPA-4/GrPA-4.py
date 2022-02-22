n = int(input())
station_dict = dict()

while n > 0:
    train = input()
    num_comps = int(input())
    train_dict = dict()
    for i in range(num_comps):
        comp, count = input().split(',')
        train_dict[comp] = int(count)
    station_dict[train] = train_dict
    n = n - 1
