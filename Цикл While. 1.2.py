my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while len(my_list) > 0:
    if (my_list[a]) > a:
        if (my_list[a]) == 0:
            continue
        print(my_list[a])
    a += 1
    if (my_list[a]) < 0:
        break

