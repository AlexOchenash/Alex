winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
month = int(input("введите цифру от 1 до 12: "))
if month in winter:
    print("winter")
if month in spring:
        print("spring")
if month in summer:
        print("summer")
if month in autumn:
        print("autumn")

winter = {12: "des", 1: "jan", 2: "feb"}
spring = {3: "mar", 4: "apr", 5: "may"}
summer = {6: "june", 7: "jul", 8: "aug"}
autumn = {9: "sep", 10: "oct", 11: "nov"}
month = int(input("введите цифру от 1 до 12: "))
if month in winter:
    del winter
    print("winter")
if month in spring:
    del spring
    print("spring")
if month in summer:
    del summer
    print("summer")
if month in autumn:
    del autumn
    print("autumn")