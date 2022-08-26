import numpy as np

num_of_persons = int(input("enter number of students: "))
id = list()
score = list()

for i in range(num_of_persons):
    id.append(int(input("enter student id number: ")))
    score.append(float(input("enter student score: ")))
unique_score = list(np.unique(score))
if len(unique_score) > 1:
    second_place_score = unique_score[-2]
    second_place_id = list(i for i, n in enumerate(score) if n == second_place_score)
    temp = list()
    for i in second_place_id:
        temp.append(id[i])
    second_place_id = temp
    print(
        "second place score is: %s and their id is %s "
        % (second_place_score, second_place_id)
    )
else:
    print("all people got same score")
