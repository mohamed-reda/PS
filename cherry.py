from ch1.cf import min_max


def min_max(data):
    # if len(data) == 1:
    #     return 0, 0
    maxNumber = data[0]
    minNumber = data[0]
    for index in range(len(data)):
        data[index] = int(data[index])
        if data[index] > maxNumber:
            maxNumber = data[index]
        if data[index] < minNumber:
            minNumber = data[index]
    return minNumber, maxNumber


"""
n = int(input())
for i in range(n):
    l = int(input())
    mylist = input().split()
    max_of_all = 0
    max_of_all = int(mylist[0])
    second = int(mylist[1])
    for index in range(1, l):
        my_int = int(mylist[index])
        if max_of_all < my_int:
            second = max_of_all
            max_of_all = my_int
        if my_int > second and my_int != max_of_all:
            second = my_int
    print(max_of_all * second)
    # print(min_max(n))
"""
n = int(input())
for i in range(n):
    l = int(input())
    mylist = input().split()
    first = int(mylist[0])
    second = int(mylist[1])
    big_max = first * second
    mylist = [int(mylist[ofs]) for ofs in range(l)]
    small_max_min = first * second
    for index in range(0, l):
        for pairs_until_index in range(index + 1, l):
            small_max = 0
            small_min = 0
            small_min, small_max = min_max(mylist[index:pairs_until_index])
            small_max_min = small_min * small_max
            # print(mylist[index:pairs_until_index + 1])
            # print(f'the smallest is: {small_min} and the largest is {small_max}')
            # print(f'max * min {small_min * small_max}')
            # print('---------------------------------------')

            if big_max < small_max_min:
                big_max = small_max_min
    print(big_max)

"""
4
3
2 4 3
4
3 2 3 1
2
69 69
6
719313 273225 402638 473783 804745 323328

1
3
2 4 3

"""
