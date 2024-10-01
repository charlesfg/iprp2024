import sys


# def print_subs(s, n):
#     for i in range(len(s)-n+1):
#         print(s[i:i+n])

def print_subs(s, n):
    for i in range(len(s)-n+1):
        for j in range(n):
            print(s[i+j], end="")
        print(" ")
    
if len(sys.argv) < 3:
    print("Forneça a string de entrada e o número de caracteres")
    sys.exit(0)
    
s_input = sys.argv[1]
n = eval(sys.argv[2])

print_subs(s_input, n)


