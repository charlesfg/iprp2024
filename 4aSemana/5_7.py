p1 = input()
p2 = input()

def friend(bigger, smaller):
    cnt = 0
    sz = len(smaller)
    for i in range(0, sz):
        if bigger[i] == smaller[i]:
            cnt +=1
    return cnt/sz >= 0.9


is_friend = False

if len(p1) >= len(p2):
    is_friend = friend(p1, p2)
else:
    is_friend = friend(p2, p1)


print("The word '{}' and '{}' {} friend".format(
    p1, p2, "are" if is_friend else "are not"
))