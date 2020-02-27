a = input(str("введите любое слово: "))
b = input("введите любое число: ")
c = input("введите любое слово: ")
d = input("введите любые цифры: ")
list = [a, b, c, d]
list[0], list[1] = list[1], list[0]
list[2], list[3] = list[3], list[2]
print(list)


