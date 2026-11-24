"""Задание 5. Анализатор учебных результатов."""

students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ("отлично", "хорошо", "удовлетворительно", "недостаточно")
NO_DATA = "нет данных"


def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("пустой список")
    total = 0
    for v in values:
        total += v
    return total / len(values)


def minimum(values: list[float]) -> float:
    if not values:
        raise ValueError("пустой список")
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result


def maximum(values: list[float]) -> float:
    if not values:
        raise ValueError("пустой список")
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result


def classify(score: float) -> str:
    if score >= 90:
        return CATEGORIES[0]
    elif score >= 75:
        return CATEGORIES[1]
    elif score >= 60:
        return CATEGORIES[2]
    else:
        return CATEGORIES[3]


def student_summary(name: str, results: list[int]) -> dict:
    if not results:
        return {"name": name, "count": 0, "mean": None, "min": None, "max": None, "category": NO_DATA}
    avg = mean(results)
    return {"name": name, "count": len(results), "mean": avg, "min": minimum(results),
            "max": maximum(results), "category": classify(avg)}


def find_top_students(summaries: list[dict]) -> list[str]:
    best = None
    for s in summaries:
        if s["mean"] is not None and (best is None or s["mean"] > best):
            best = s["mean"]
    if best is None:
        return []
    return [s["name"] for s in summaries if s["mean"] == best]


def rank_students(summaries: list[dict]) -> list[dict]:
    ranked = [s for s in summaries if s["mean"] is not None]
    for i in range(1, len(ranked)):
        item = ranked[i]
        j = i - 1
        while j >= 0 and (ranked[j]["mean"], _inv(ranked[j]["name"])) < (item["mean"], _inv(item["name"])):
            ranked[j + 1] = ranked[j]
            j -= 1
        ranked[j + 1] = item
    return ranked


def _inv(name: str) -> tuple:
    return tuple(-ord(c) for c in name)


def group_summary(data: dict[str, list[int]]) -> dict:
    summaries = [student_summary(name, results) for name, results in data.items()]
    all_results_total = 0
    all_results_count = 0
    categories = {c: 0 for c in CATEGORIES}
    with_results = 0
    for name, results in data.items():
        for r in results:
            all_results_total += r
            all_results_count += 1
    for s in summaries:
        if s["mean"] is not None:
            with_results += 1
            categories[s["category"]] += 1
    return {
        "students": len(data),
        "with_results": with_results,
        "overall_mean": all_results_total / all_results_count if all_results_count else None,
        "categories": categories,
        "top": find_top_students(summaries),
        "summaries": summaries,
    }


def format_report(student_data: list[dict], group_data: dict) -> str:
    lines = ["== Результаты студентов =="]
    for s in student_data:
        if s["mean"] is None:
            lines.append(f"{s['name']}: нет результатов")
        else:
            lines.append(f"{s['name']}: среднее {s['mean']:.2f}, мин. {s['min']}, макс. {s['max']}, {s['category']}")
    lines.append("\n== Рейтинг ==")
    for place, s in enumerate(rank_students(student_data), 1):
        lines.append(f"{place}. {s['name']} - {s['mean']:.2f}")
    lines.append("\n== Группа ==")
    lines.append(f"Студентов: {group_data['students']} (с результатами: {group_data['with_results']})")
    overall = group_data["overall_mean"]
    lines.append("Общий средний результат: " + ("нет данных" if overall is None else f"{overall:.2f}"))
    lines.append("Лидеры: " + (", ".join(group_data["top"]) if group_data["top"] else "нет"))
    for c, n in group_data["categories"].items():
        lines.append(f"{c}: {n}")
    return "\n".join(lines)


def analyze(data: dict[str, list[int]]) -> str:
    group = group_summary(data)
    return format_report(group["summaries"], group)



def run_scenarios() -> None:
    rows = []

    g = group_summary(students)
    assert g["top"] == ["Дарья"] and g["students"] == 4
    assert g["categories"] == {"отлично": 1, "хорошо": 1, "удовлетворительно": 1, "недостаточно": 1}
    rows.append(("обычный набор", "лидер Дарья, по одному студенту в каждой категории"))

    g = group_summary({"Мария": [80, 90]})
    assert g["top"] == ["Мария"] and g["overall_mean"] == 85
    rows.append(("один студент", "лидер Мария, общий средний 85"))

    g = group_summary({"А": [90, 80], "Б": [85, 85], "В": [70]})
    assert g["top"] == ["А", "Б"]
    rows.append(("несколько лидеров", "лидеры А и Б (среднее 85)"))

    g = group_summary({})
    assert g["students"] == 0 and g["overall_mean"] is None and g["top"] == []
    rows.append(("пустая группа", "общий средний - нет данных, лидеров нет"))

    g = group_summary({"Ян": [], "Ева": [70]})
    assert g["with_results"] == 1 and g["top"] == ["Ева"] and g["summaries"][0]["category"] == NO_DATA
    rows.append(("студент без результатов", "Ян - 'нет данных', в статистику не входит"))

    bounds = [(90, "отлично"), (89.99, "хорошо"), (75, "хорошо"), (74.99, "удовлетворительно"),
              (60, "удовлетворительно"), (59.99, "недостаточно"), (0, "недостаточно")]
    for score, expected in bounds:
        assert classify(score) == expected, score
    rows.append(("границы категорий", "90, 89.99, 75, 74.99, 60, 59.99, 0 классифицированы верно"))

    before = {k: list(v) for k, v in students.items()}
    group_summary(students)
    assert students == before
    rows.append(("исходные данные", "словарь students не изменен"))

    assert minimum([4, 2, 9]) == 2 and maximum([4, 2, 9]) == 9 and mean([1, 2]) == 1.5
    for func in (mean, minimum, maximum):
        try:
            func([])
            raise AssertionError("ожидался ValueError")
        except ValueError:
            pass
    rows.append(("пустой список в mean/min/max", "ValueError"))

    print("== Сценарии проверки ==")
    for number, (name, result) in enumerate(rows, 1):
        print(f"{number}. {name:30} {result}  [OK]")


def main() -> None:
    print(analyze(students))
    print()
    run_scenarios()


if __name__ == "__main__":
    main()