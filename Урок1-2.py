# Задание 2.
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# Пример:
# Введите время в секундах: 3600
# Время в формате ч:м:с - 1.0 : 60.0 : 3600

second = int(input('Введите время в секундах: '))
print("Время в формате ч:м:с -", second / 3600, ":", second / 60, ":", second)
