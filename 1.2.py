sec = int(input("ВВедите время в секундах: "))
hour =  sec // 3600
min = sec % 3600 // 60
last_sec = sec - hour * 3600 - min * 60
print(hour, ":", min, ":", last_sec )
