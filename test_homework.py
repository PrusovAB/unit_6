import pytest
import Homework

numbers1 = [10, 20, 30, 40, 50]
numbers2 = [100, 20, 30, 40, 50]
numbers3 = []
numbers4 = 0
numbers5 = ["1", "2"]


def test_average_first_max():
    expected_str = "второй список имеет большее среднее значение"
    assert Homework.lists_average_compare(numbers1, numbers2) == expected_str

def test_average_second_max():
    expected_str = "первый список имеет большее среднее значение"
    assert Homework.lists_average_compare(numbers2, numbers1) == expected_str

def test_average_second_max():
    expected_str = "средние значения списков равны"
    assert Homework.lists_average_compare(numbers1, numbers1) == expected_str

def test_list_type_error():
    with pytest.raises(TypeError):
        Homework.lists_average_compare(numbers4, numbers1)

def test_list_type_error():
    with pytest.raises(TypeError):
        Homework.lists_average_compare(numbers1, numbers4)

def test_list_type_error():
    with pytest.raises(TypeError):
        Homework.lists_average_compare(numbers1, numbers5)

def test_list_type_error():
    with pytest.raises(TypeError):
        Homework.lists_average_compare(numbers5, numbers1)

def test_average_second_max():
    expected_str = "Первый список пуст"
    assert Homework.lists_average_compare(numbers3, numbers1) == expected_str

def test_average_second_max():
    expected_str = "Второй список пуст"
    assert Homework.lists_average_compare(numbers1, numbers3) == expected_str


