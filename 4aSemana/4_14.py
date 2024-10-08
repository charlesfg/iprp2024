def print_tabuada(a):
    for i in range(1,11):
        print("{0:^5d} x {1:^5d} = {2:^5d}".format(a, i, a*i))
    pass


a = int(input("Insira o número que deseja a tabuada:\n"))
print("-" * 20) 
print_tabuada(a)