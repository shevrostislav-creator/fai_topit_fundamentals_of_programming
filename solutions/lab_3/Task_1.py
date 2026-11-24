"""Задание 1. Условия и классификация данных."""
import sys

LEVELS = ("недостаточный", "удовлетворительный", "хороший", "отличный")


def check_ranges(score: int, absences: int) -> str:
    if score < 0 or score > 100:
        return "результат вне 0-100"
    elif absences < 0 or absences > 5:
        return "пропуски вне 0-5"
    else:
        return ""


def base_level_index(score: int) -> int:
    if score >= 90:
        return 3
    elif score >= 75:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0


def evaluate(score: int, absences: int) -> str:
    error = check_ranges(score, absences)
    if error:
        return "ошибка: " + error
    index = base_level_index(score)
    if absences > 3 and index > 0:
        index -= 1
    return LEVELS[index]


def describe_work(work_type: str) -> str:
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def format_record(score: int, work_type: str, absences: int) -> str:
    return (f"{describe_work(work_type)}, результат {score}, пропусков {absences}: "
            f"{evaluate(score, absences)}")



SCENARIOS = [
    (0, "exam", 0, "недостаточный"),
    (59, "project", 0, "недостаточный"),
    (60, "practice", 0, "удовлетворительный"),
    (74, "exam", 3, "удовлетворительный"),
    (75, "exam", 3, "хороший"),
    (75, "exam", 4, "удовлетворительный"),
    (89, "project", 5, "удовлетворительный"),
    (90, "exam", 0, "отличный"),
    (100, "practice", 4, "хороший"),
    (50, "exam", 5, "недостаточный"),
    (101, "exam", 0, "ошибка: результат вне 0-100"),
    (70, "project", 6, "ошибка: пропуски вне 0-5"),
]

RECORDS = [
    (95, "exam", 0), (88, "project", 1), (76, "practice", 4), (59, "exam", 2),
    (60, "project", 0), (100, "practice", 5), (45, "exam", 4), (82, "exam", 3),
    (74, "project", 1), (91, "practice", 2), (67, "exam", 5), (0, "practice", 0),
]


def run_scenarios() -> None:
    print(f"{'результат':>9} {'тип':9} {'проп.':>5}  {'ожидается':30} {'фактически':30} итог")
    for score, work_type, absences, expected in SCENARIOS:
        actual = evaluate(score, absences)
        status = "OK" if actual == expected else "ОШИБКА"
        print(f"{score:>9} {work_type:9} {absences:>5}  {expected:30} {actual:30} {status}")
        assert actual == expected, (score, work_type, absences, actual)


def summarize(records: list[tuple[int, str, int]]) -> dict[str, int]:
    counts = {level: 0 for level in LEVELS}
    for score, _work_type, absences in records:
        level = evaluate(score, absences)
        if level in counts:
            counts[level] += 1
    return counts


def main() -> None:
    if len(sys.argv) == 4:
        print(format_record(int(sys.argv[1]), sys.argv[2], int(sys.argv[3])))
        return
    print("== Тестовые сценарии ==")
    run_scenarios()
    print("\n== Обработка списка записей ==")
    for number, record in enumerate(RECORDS, 1):
        print(f"{number:>2}. {format_record(*record)}")
    print("\n== Сводка по уровням ==")
    for level, count in summarize(RECORDS).items():
        print(f"{level}: {count}")


if __name__ == "__main__":
    main()