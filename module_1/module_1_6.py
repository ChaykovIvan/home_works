my_dict = {
    "Алексей": 1990,
    "Мария": 1985,
    "Иван": 2000
}
removed_value = my_dict.pop("Иван", "Ключ не найден")
print("Удалено значение:", removed_value )
print("Обновленный словарь my_dict:", my_dict)
my_set = {1, 3.14, "Python", 1, 42, "Python"}
print("Множество my_set:", my_set)
my_set.add("Программирование")
my_set.add(2024)
my_set.remove(42)
print("Измененное множество my_set:", my_set)