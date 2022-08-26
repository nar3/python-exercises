def prime(a):
    if a > 3:
        if a % 2 == 0:
            return 0
        else:
            for i in range(3, int(a ** 0.5) + 1, 2):
                if a % i == 0:
                    return 0
    elif a == 2 or a == 3:
        return 1
    elif a < 2:
        return 0
    return 1


def main():
    p = list()
    n = int(input("enter number to check: "))
    print("primary is ", end="")
    for i in range(n):
        if prime(i):
            print(i, end=" ")


main()