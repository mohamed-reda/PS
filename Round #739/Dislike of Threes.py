def get_the_indexed_element(index):
    count = 0
    all = 0
    for i in range(1, index + 1):
        all += 1
        if all % 3 == 0:
            # print(i)
            count += 1
        s = f"{all + count}"
        if s[len(s) - 1] == '3':
            count += 1
            s = f"{all}"
        if s[len(s) - 1] == '3':
            count += 1
        all += count
        count = 0

    # print(count_of_3)
    return all


#
# testcase = int(input())
# for i in range(testcase):
#     index = int(input())
#     print(get_the_indexed_element(index))

print(get_the_indexed_element(1))
print(get_the_indexed_element(2))
print(get_the_indexed_element(3))
print(get_the_indexed_element(4))
print(get_the_indexed_element(5))
print(get_the_indexed_element(6))
print(get_the_indexed_element(7))
print(get_the_indexed_element(8))
print(get_the_indexed_element(9))
print(get_the_indexed_element(1000))
"""
10
1
2
3
4
5
6
7
8
9
1000

"""
