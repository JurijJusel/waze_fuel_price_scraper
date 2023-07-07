def print_1():
    print("def1 file 1.py")


def print_2():
    print_1()
    print("def2 file 1.py")    
    return "print_2"

print_2()