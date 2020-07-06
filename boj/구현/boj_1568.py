# boj 1568 새

N = int(input())
m = 0
count = 0

while True :
    m +=1
    if N > m:
        N-=m
        count +=1
    elif N < m:
        m=0
    elif N == m:
        count+=1
        break
print(count)