def exp(x):
    return x ** 2


def isOdd(x):
    return x % 2


inputData = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
print('Исходный список: ', inputData)
result = map(exp, inputData)
result1 = list(result)
print('Квадраты элементов исходного списка: ', result1)
result2 = filter(isOdd, result1)

print('Нечетные квадраты: ', list(result2))
