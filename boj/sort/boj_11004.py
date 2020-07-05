# 11004 K번째 수

a, b = map(int, input().split(' '))
num = list(map(int, input().split(' ')))
num_list = sorted(num)
print(num_list[b-1])