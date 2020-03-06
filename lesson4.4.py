my_list = [6, 34, 34, 55, 1, 7, 7, 154, 82, 82]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)