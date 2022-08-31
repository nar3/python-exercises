def histogram(List):
    for i in List:
        p = i
        while p > 0:
            print("*", end="")
            p -= 1
        print("")


histogram([3, 6, 4, 3, 6, 5])
