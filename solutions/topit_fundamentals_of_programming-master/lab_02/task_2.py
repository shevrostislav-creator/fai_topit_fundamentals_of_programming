import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


def write(title):
    print("=" * 60)
    print(title)
    print("=" * 60)
    print("original:", original)
    print("alias:   ", alias)
    print("shallow: ", shallow)
    print("deep:    ", deep)

    print("id внешних списков:")
    print("  original:", id(original))
    print("  alias:   ", id(alias))
    print("  shallow: ", id(shallow))
    print("  deep:    ", id(deep))

    print("id первого вложенного списка:")
    print("  original:", id(original[0]))
    print("  alias:   ", id(alias[0]))
    print("  shallow: ", id(shallow[0]))
    print("  deep:    ", id(deep[0]))

    print("id объекта с первой оценкой (5):")
    print("  original:", id(original[0][1]))
    print("  alias:   ", id(alias[0][1]))
    print("  shallow: ", id(shallow[0][1]))
    print("  deep:    ", id(deep[0][1]))
    print()



write("До изменений")

original.append(["Databases", 5])
write("После original.append(['Databases', 5])")

original[0][1] = 3
write("После original[0][1] = 3")



# задание с матрицей
wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print("wrong_matrix:")
print(wrong_matrix)
print("  id строк:", [id(row) for row in wrong_matrix])
print()



correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1
print("correct_matrix:")
print(correct_matrix)
print("  id строк:", [id(row) for row in correct_matrix])


