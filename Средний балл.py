grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
sorted_1 = sum(grades[0]) / len(grades[0])
sorted_2 = sum(grades[1]) / len(grades[1])
sorted_3 = sum(grades[2]) / len(grades[2])
sorted_4= sum(grades[3]) / len(grades[3])
sorted_5= sum(grades[4]) / len(grades[4])
my_dict = {(students[0]): sorted_1,(students[1]): sorted_2,(students[2]): sorted_3,(students[3]): sorted_4,(students[4]): sorted_5}
print(my_dict)