def my_f():
    try:
        num1 = int(input("введите число "))
        num2 = int(input("введите число "))
    except ZeroDivisionError:
        return
    itog = num1 / num2
    return itog
itog = my_f()
print(itog)
