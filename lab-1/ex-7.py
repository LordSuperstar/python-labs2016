s=str(input())
print(s[2])
print(s[-2])
print(s[0:5])
print(s[:-2])
print(s[0::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# Почему нельзя заменить print([::-2]) на print([-1::-2]) ?     9 строка
# А вот с print([::-2]) на print([-1::-2]) так работает         8 строка