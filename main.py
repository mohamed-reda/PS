# for i in range(1,17):
#     print(f'17 % {i} = {17 % i}')

#
# for i in range(5,100):
#     print(f'{i} % 2 = {i % 2}')
#     print(f'{i} % 4 = {i % 3}')

# n = int(input())
# for i in range(n):
#     testcase = int(input())
#     first = 0
#     second = 0
#     l = 0
#     for in10 in range(2, 10):
#
#         if testcase % in10 != 0 and first == 0:
#             first = in10
#             l = testcase % in10
#         elif testcase % in10 == l and first != 0:
#             second = in10
#             break
#     print(f'{first} {second}')

"""
2
17
5

"""
n = int(input())

for i in range(n):
    testcase = int(input())
    first = 0
    second = 0
    l = set()
    d = {'':''}
    for in10 in range(2, testcase):
        if testcase % in10 in l:
            second = in10
            first = d[testcase % in10]
            break
        if testcase % in10 != 0:
            l .add(testcase % in10)
            d[testcase % in10] = in10


    print(f'{first} {second}')
