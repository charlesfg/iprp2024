import random

n = eval(input())
cnt = 0
for i in range(n):
    if random.randint(0,6) % 2 == 0:
        cnt +=1
print("{}x or {}%".format(cnt, int((cnt/n)*100)))