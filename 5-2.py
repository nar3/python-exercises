sentence=list(input('enter the sentence:').split(' '))
res=dict()
for i in sentence:
    if i not in res.keys():
        res.update({i:sentence.count(i)})
res.pop('')
print(res)
