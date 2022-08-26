def extract_odd_index(str):
    p = ""
    for i in range(len(str)):
        if i % 2 == 0:
            p += str[i]
    return p


str = input("please enter your text: ")
print(extract_odd_index(str))