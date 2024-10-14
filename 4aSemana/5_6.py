def orig():
    for i in range(3):
        for j in range(1,3):
            print(i/j)
        
def sol():
    i = 0
    j = 1
    while(i < 3):
        while(j < 3):
            print(i/j)
            j +=1
        i+=1
    pass


if __name__ == "__main__":
    orig()
    print("-"* 10)
    sol()