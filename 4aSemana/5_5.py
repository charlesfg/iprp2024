def orig():
    i = 20
    while (i >= 0):
        print("i= ",i)
        i = i - 2
        
def sol():
    for i in range(20,-1,-2):
        print("i= ",i)
    pass


if __name__ == "__main__":
    orig()
    print("-"* 10)
    sol()