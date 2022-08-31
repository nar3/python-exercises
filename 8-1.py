myfile = open("d:\\11.txt", "w")
while True:
    sentence = input("enter a sentence: ")
    if len(sentence) != 0:
        sentence += "\n"
        myfile.write(sentence)
    else:
        break
myfile.close()
