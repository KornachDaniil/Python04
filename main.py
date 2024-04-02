def sum_digits(number):
    number_str = str(number)
    digit_sum = 0
    for i in number_str:
        digit_sum += int(i)
    return digit_sum


number = int(input("Введите число: "))
result = sum_digits(number)
print(f"Сумма цифр числа {number} равна {result}")
