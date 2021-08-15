n = int(input())


def bitwiseAND(my_list, max_num):
    # get the combination
    max_com = 0
    first = 0
    second = 0
    # for i in range(int(len(my_list) / 2)):
    #     com = my_list[i] + my_list[len(my_list) - 1 - i]
    #     if max_com < com:
    #         max_com = com
    #     first = my_list[i]
    #     second = my_list[len(my_list) - 1 - i]
    # print(first & second)
    for i in range(int(len(my_list) / 2)):

        # print(f"{my_list[i]} & {my_list[len(my_list) - 1 - i]} is : {my_list[i] & my_list[len(my_list) - 1 - i]}")
        if my_list[i] == max_num or my_list[len(my_list) - 1 - i] == max_num:
            print(my_list[i] & my_list[len(my_list) - 1 - i])
            return
    # # print('-------------------------')


for i in range(n):
    testcase = int(input())
    list = input().split()
    my_list = []
    max_num = 0
    for ofs in range(testcase):
        current = int(list[ofs])
        if max_num < current and ofs > 0:
            max_num = current

        my_list.append(current)
    if testcase % 2 == 0:
        bitwiseAND(my_list, max_num)
    else:
        bitwiseAND(my_list[1:testcase], max_num)

"""
4
2
1 2
3
1 1 3
4
3 11 3 7
5
11 7 15 3 7

"""
