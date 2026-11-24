#Эксперимент A. Неизменяемый объект
a = 10
b = a

print("=== Эксперимент A. Неизменяемый объект ===")
print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))


#Экперимаент B. Изменяемый объект
print("\n=== Эксперимент B. Изменяемый объект ===")
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

print("\n--- Переназначение second на новый список ---")
second = list(first)
print("first == second:", first == second)
print("first is second:", first is second)
second.append(40)
print("first =", first)
print("second =", second)


import copy
#Практическая задача
config_1 = {
    "name_of_project": "Учебный проект CS-2",
    "list_of_members": ["Donk", "Simple", "Monesy", "ZywOo", "Rostislav"],
    "game_parametrs": [["--Chosen map", "Mirage"], ["--Players", "5"], ["--Bad players", "4"]]
}
print("-"*50)
print("без deepcopy")
print("-"*50)
config_2 = config_1
print("до изменения:")
print("config_1:", config_1)
print("config_2:", config_2)

config_1["list_of_members"] = ["Flame", "Ropz", "Buster", "Exile", "Evelon"]
config_1["game_parametrs"][2][1] = "5"


print("После изменений через config_1:")
print("config_1:", config_1)
print("config_2:", config_2)
print("config_1 is config_2:", config_1 is config_2)
print("-"*50)
print("после dyeepcopy")
print("-"*50)
config_1 = {
    "name_of_project": "Учебный проект CS-2",
    "list_of_members": ["Donk", "Simple", "Monesy", "ZywOo", "Rostislav"],
    "game_parametrs": [["--Chosen map", "Mirage"], ["--Players", "5"], ["--Bad players", "4"]]
}

config_2 = copy.deepcopy(config_1)
print("до изменения:")
print("config_1:", config_1)
print("config_2:", config_2)

config_1["list_of_members"] = ["Flame", "Ropz", "Buster", "Exile", "Evelon"]
config_1["game_parametrs"][2][1] = "5"


print("После изменений через config_1:")
print("config_1:", config_1)
print("config_2:", config_2)
print("config_1 is config_2:", config_1 is config_2)

assert config_1 is not config_2
assert config_1["list_of_members"] is not config_2["list_of_members"]
assert config_1["game_parametrs"] is not config_2["game_parametrs"]
assert config_1["game_parametrs"][0] is not config_2["game_parametrs"][0]


print("\nИтог:")
print("  Присваивание: config_2 — это тот же объект; название, участники и параметры общие.")
print("  deepcopy: словарь, список участников и все вложенные списки параметров независимы.")

