
def lists_average_compare(numbers_n, numbers_m):
    if not isinstance(numbers_n, list):
        raise TypeError("Input should be a list.")
    elif not isinstance(numbers_m, list):
        raise TypeError("Input should be a list.")

    for item in numbers_n:
        if not isinstance(item, int):
            raise TypeError("В списке должны быть только числа")
    for item in numbers_m:
        if not isinstance(item, int):
            raise TypeError("В списке должны быть только числа")

    if not numbers_n:
        return "Первый список пуст"
    if not numbers_m:
        return "Второй список пуст"

    avg1 = (sum(numbers_n) / len(numbers_n))
    avg2 = (sum(numbers_m) / len(numbers_m))

    if (avg1 > avg2):
        str = 'первый список имеет большее среднее значение'
        print(str)
        return str

    elif (avg1 < avg2):
        str = 'второй список имеет большее среднее значение'
        print(str)
        return str

    elif (avg1 == avg2):
        str = 'средние значения списков равны'
        print(str)
        return str
