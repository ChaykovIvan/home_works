grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
studentes = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(studentes)
average_grades = {}

for i, student in enumerate(sorted_students):
    average_grade = sum(grades[i]) / len(grades[i])
    average_grades[student] = average_grade

print("Средний балл каждого ученика:")
for studente, average in average_grades.items():
    print(f"{studente}: {average}")    #я бы добавил в prinr (..{averege:.2f}) для приличного вывода
                                       # для меня это дело эстетики )0))