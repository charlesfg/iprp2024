import random

n = eval(input())
cnt = 0
for i in range(n):
    if random.randint(0,6) % 2 == 0:
        cnt +=1
print(f"{cnt}x or { int((cnt/n)*100)}%")

for i in random.randint()