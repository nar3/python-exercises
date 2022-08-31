case = input("enter int number: ")
result = ""
for i in case:
    result += i
    result += "   "
result = result[0:-3]
print("result is:", result)
