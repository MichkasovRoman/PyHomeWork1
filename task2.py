# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

threeDigitNumber = int(input('Введите трехзначное число: '))
module = abs(threeDigitNumber)
hundreds = module // 100       # количество сотен в заданном числе
tens = module % 100 // 10      # количество десятков в заданном числе
units = module % 10            # количество единиц в заданном числе

if len(str(module)) > 3 :
    print('Некорректный формат записи числа.')
else:
    sumOfDigits = hundreds + tens + units
    print(f'Сумма цифр введенного вами числа: {sumOfDigits}')




