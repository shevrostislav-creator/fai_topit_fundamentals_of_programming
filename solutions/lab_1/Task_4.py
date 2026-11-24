student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print(student[0], student[3])

print(student[:4])
print(student[5:])

print(student.upper())
print(student.lower())

print(student[0] + "." + student[5] + ".")

print(course[::-1])

print("%s — %s: %d/%d (70.0%%) " % (student, course, completed, total))
print("{} — {}: {}/{} (70.0%) " .format(student, course, completed, total))
print(f"{student} — {course}: {completed}/{total} (70.0%)")

symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(ord(symbol)))
print(symbol.encode("utf-8"))
print(len(symbol))
print(len(symbol.encode("utf-8")))

#symbol[0] = "А"