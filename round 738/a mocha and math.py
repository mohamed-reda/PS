n = int(input())


def bitwiseAND(my_list, max_num):
    # get the combination
    for i in range(len(my_list)):
        if my_list[i] == max_num or my_list[len(my_list) - 1 - i] == max_num:
            print(my_list[i] & my_list[len(my_list) - 1 - i])
            return


for i in range(n):
    testcase = int(input())
    list = input().split()
    my_list = []
    max_num = 0
    for ofs in range(testcase):
        current = int(list[ofs])
        if max_num < current:
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
