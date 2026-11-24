"""Задание 3. Коллекции и выбор структуры данных."""

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]


def empty_structures() -> dict:
    return {
        "students": set(),
        "labs": set(),
        "attempts": {},
        "best": {},
        "count": {},
    }


def add_submission(data: dict, record: tuple[str, str, int]) -> None:
    student, lab, score = record
    key = (student, lab)
    data["students"].add(student)
    data["labs"].add(lab)
    data["attempts"].setdefault(student, []).append((lab, score))
    if key not in data["best"] or score > data["best"][key]:
        data["best"][key] = score
    data["count"][key] = data["count"].get(key, 0) + 1


def build_structures(records: list[tuple[str, str, int]]) -> dict:
    data = empty_structures()
    for record in records:
        add_submission(data, record)
    return data


def students_with_all_labs(data: dict) -> set[str]:
    by_lab = {lab: set() for lab in data["labs"]}
    for (student, lab) in data["best"]:
        by_lab[lab].add(student)
    result = set(data["students"])
    for students in by_lab.values():
        result &= students
    return result


def run_query(data: dict, line: str) -> str:
    parts = line.split()
    if not parts:
        return "пустая команда"
    match parts:
        case ["student", name]:
            if name not in data["attempts"]:
                return f"студент {name} не найден"
            return f"попытки {name}: {data['attempts'][name]}"
        case ["best", name, lab]:
            if (name, lab) not in data["best"]:
                return f"нет данных для пары ({name}, {lab})"
            return f"лучший результат {name} по {lab}: {data['best'][(name, lab)]}"
        case ["attempts", name, lab]:
            if (name, lab) not in data["count"]:
                return f"нет данных для пары ({name}, {lab})"
            return f"попыток {name} по {lab}: {data['count'][(name, lab)]}"
        case ["completed", lab]:
            who = sorted(s for (s, l) in data["best"] if l == lab)
            return f"{lab} сдали: {who}" if who else f"работа {lab} никем не сдана"
        case _:
            return f"неизвестная команда или неверное число аргументов: {line!r}"


def main() -> None:
    data = build_structures(submissions)
    print("Студенты:", sorted(data["students"]))
    print("Работы:", sorted(data["labs"]))
    print("Попытки:", data["attempts"])
    print("Лучшие результаты:", data["best"])
    print("Число попыток:", data["count"])
    print("Сдали все работы:", sorted(students_with_all_labs(data)))

    print("\nДобавляем запись ('daria', 'lab_02', 4) и ('anna', 'lab_02', 3)")
    add_submission(data, ("daria", "lab_02", 4))
    add_submission(data, ("anna", "lab_02", 3))
    print("Сдали все работы:", sorted(students_with_all_labs(data)))
    print("Лучший результат anna/lab_02:", data["best"][("anna", "lab_02")],
          "| попыток:", data["count"][("anna", "lab_02")])

    print("\nЗапросы:")
    for q in ["student anna", "best anna lab_01", "attempts boris lab_02", "completed lab_01",
              "best anna lab_09", "student petr", "remove anna", "best anna", ""]:
        print(f"  > {q!r:26} {run_query(data, q)}")

    assert data["best"][("anna", "lab_01")] == 5 and data["count"][("anna", "lab_01")] == 2
    assert build_structures(submissions + [("daria", "lab_02", 4), ("anna", "lab_02", 3)])["best"] == data["best"]


if __name__ == "__main__":
    main()