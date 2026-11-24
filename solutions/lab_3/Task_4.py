"""Задание 4. Функции, параметры и области видимости."""


def arithmetic_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("список не должен быть пустым")
    total = 0.0
    for v in values:
        total += v
    return total / len(values)


def normalize_name(name: str) -> str:
    parts = name.split()
    if not parts:
        return ""
    fixed = []
    for part in parts:
        pieces = [p[:1].upper() + p[1:].lower() for p in part.split("-")]
        fixed.append("-".join(pieces))
    return " ".join(fixed)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    name = normalize_name(student)
    if not results:
        return f"{name}: нет результатов"
    mean = arithmetic_mean(results)
    return f"{name}: {prefix.lower()} {mean:.{precision}f} (работ: {len(results)})"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    if not tags:
        return ()
    seen = set()
    result = []
    for tag in tags:
        clean = tag.strip()
        if lowercase:
            clean = clean.lower()
        if clean and clean not in seen:
            seen.add(clean)
            result.append(clean)
    return tuple(result)



def run_asserts() -> None:
    assert arithmetic_mean([1, 2, 3]) == 2
    assert arithmetic_mean([2.5]) == 2.5
    assert arithmetic_mean([0, 10]) == 5
    try:
        arithmetic_mean([])
        raise AssertionError("ожидался ValueError")
    except ValueError:
        pass

    assert normalize_name("  иВАНОВ   иван ") == "Иванов Иван"
    assert normalize_name("анна-мария   петрова") == "Анна-Мария Петрова"
    assert normalize_name("   ") == ""

    assert build_report("анна", [80, 90]) == "Анна: результат 85.00 (работ: 2)"
    assert build_report("борис", [70, 71], precision=0, prefix="Среднее") == "Борис: среднее 70 (работ: 2)"
    assert build_report("илья", []) == "Илья: нет результатов"

    assert collect_tags(" Python ", "python", "", "Код") == ("python", "код")
    assert collect_tags("A", "a", lowercase=False) == ("A", "a")
    assert collect_tags() == ()



course = "Основы программирования"


def outer() -> None:
    counter = 0

    def inner() -> None:
        nonlocal counter
        local_note = "вызов"
        counter += 1
        print(f"  {local_note} {counter}: курс = {course!r}, длина названия = {len(course)}")


    inner()
    inner()
    print("  итоговое значение counter во внешней функции:", counter)



def add_result_bad(value, results=[]):
    results.append(value)
    return results


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results



def apply_to_results(operation, values):
    return [operation(v) for v in values]


def to_percent(x):
    return x * 100 // 5


def make_threshold_checker(threshold):
    def check(result):
        return result >= threshold
    return check


def main() -> None:
    run_asserts()
    print("Все assert пройдены.\n")

    print("Позиционные и именованные аргументы:")
    print(" ", build_report("анна", [80, 90, 100]))
    print(" ", build_report("борис иванов", [60, 75], precision=1, prefix="Среднее"))
    print(" ", collect_tags(" Python ", "python", "", "Код", lowercase=False))

    print("\nРаспаковка * и **:")
    args = ["дарья", [95, 93, 97]]
    kwargs = {"precision": 3, "prefix": "Итог"}
    print(" ", build_report(*args, **kwargs))
    print(" ", collect_tags(*[" a", "A ", "b"]))

    print("\nLEGB:")
    print(" глобальное course до вызова:", repr(course))
    outer()
    print(" глобальное course после вызова:", repr(course))

    print("\nИзменяемое значение по умолчанию:")
    print("  ошибочная версия:", add_result_bad(1), add_result_bad(2), add_result_bad(3))
    print("  исправленная версия:", add_result(1), add_result(2), add_result(3))
    print("  значение по умолчанию:", add_result_bad.__defaults__)

    print("\nФункции как аргументы:")
    results = [3, 4, 5]
    print("  именованная функция:", apply_to_results(to_percent, results))
    print("  lambda:", apply_to_results(lambda x: x + 0.5, results))
    print("  исходные данные:", results)

    easy = make_threshold_checker(3)
    strict = make_threshold_checker(5)
    print("  порог 3:", [easy(x) for x in results])
    print("  порог 5:", [strict(x) for x in results])
    print("  в замыканиях хранятся:", easy.__closure__[0].cell_contents, strict.__closure__[0].cell_contents)


if __name__ == "__main__":
    main()