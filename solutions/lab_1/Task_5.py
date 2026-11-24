"""
Программа «Информационная карточка вычислительного эксперимента».

Запрашивает у пользователя данные об эксперименте,
затем выводит информационную карточку и диагностическую строку
с типами введённых значений.
"""


name = input("Имя исследователя: ")
experiment = input("Название эксперимента: ")
runs = int(input("Количество выполненных запусков: "))
duration = float(input("Длительность одного запуска, с: "))
real = float(input("Действительная часть коэффициента: "))
imag = float(input("Мнимая часть коэффициента: "))


total_seconds = runs * duration
total_minutes = total_seconds / 60
coefficient = complex(real, imag)
modul = real ** 2 + imag ** 2
has_runs = bool(runs)


print("=" * 40)
print(f"ЭКСПЕРИМЕНТ: {experiment}")
print(f"Исследователь: {name}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_seconds:.2f} с ({total_minutes:.2f} мин)")
print(f"Коэффициент: {coefficient}")
print(f"Квадрат модуля: {modul:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("=" * 40)


print("Типы введённых значений:")
print(f"  name = {type(name)}")
print(f"  experiment = {type(experiment)}")
print(f"  runs       = {type(runs)}")
print(f"  duration   = {type(duration)}")
print(f"  real       = {type(real)}")
print(f"  imag       = {type(imag)}")
print("=" * 40)