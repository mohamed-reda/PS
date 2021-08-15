# n = int(input())
#
# for i in range(n):
#     testcase = input()
#     first = 0
#     second = 0
#     l = set()
#     d = {'':''}
#     for in10 in range(2, testcase):
#         if testcase % in10 in l:
#             second = in10
#             first = d[testcase % in10]
#             break
#         if testcase % in10 != 0:
#             l .add(testcase % in10)
#             d[testcase % in10] = in10
#
#
#     print(f'{first} {second}')
#

# l=[1 ,5 ,2 ,4,6]
l=[8,2,5,10]
for i in l:
    print(f'{i} % {3} = {i%3}')
