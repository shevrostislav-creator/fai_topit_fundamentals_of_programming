"""Задание 2. Циклы и базовые алгоритмические схемы."""
import random
import sys

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]



def single_pass(values: list[int]) -> dict:
    total = 0
    smallest = values[0]
    largest = values[0]
    even_count = 0
    for v in values:
        total += v
        if v < smallest:
            smallest = v
        if v > largest:
            largest = v
        if v % 2 == 0:
            even_count += 1
    return {"sum": total, "min": smallest, "max": largest, "even": even_count}



def count_above_mean(values: list[int], total: int) -> int:
    mean = total / len(values)
    count = 0
    for v in values:
        if v > mean:
            count += 1
    return count



def linear_search(values: list[int], target: int) -> tuple[int, int]:
    comparisons = 0
    for i, v in enumerate(values):
        comparisons += 1
        if v == target:
            return i, comparisons
    return -1, comparisons



def is_prime(n: int) -> tuple[bool, int]:
    if n < 2:
        return False, 0
    checked = 0
    d = 2
    while d * d <= n:
        checked += 1
        if n % d == 0:
            return False, checked
        d += 1
    return True, checked



def selection_sort(values: list[int]) -> tuple[list[int], int]:
    a = list(values)
    comparisons = 0
    for i in range(len(a) - 1):
        k = i
        for j in range(i + 1, len(a)):
            comparisons += 1
            if a[j] < a[k]:
                k = j
        a[i], a[k] = a[k], a[i]
    return a, comparisons


def binary_search(sorted_values: list[int], target: int) -> tuple[int, int]:
    lo, hi = 0, len(sorted_values) - 1
    comparisons = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if sorted_values[mid] == target:
            return mid, comparisons
        comparisons += 1
        if sorted_values[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comparisons


def comparison_table(sizes=(10, 100, 1000)) -> list[tuple]:
    rows = []
    for n in sizes:
        data = random.Random(2026).sample(range(1, 10 * n), n)
        ordered, _ = selection_sort(data)
        absent = 0                                   # такого числа в наборе нет
        lin_worst = linear_search(data, absent)[1]
        bin_worst = binary_search(ordered, absent)[1]
        lin_avg = sum_of(linear_search(data, x)[1] for x in data) / n
        bin_avg = sum_of(binary_search(ordered, x)[1] for x in data) / n
        rows.append((n, lin_worst, lin_avg, bin_worst, bin_avg))
    return rows


def sum_of(items) -> int:
    total = 0
    for x in items:
        total += x
    return total


def main() -> None:
    info = single_pass(measurements)
    print("Данные:", measurements)
    print("Сумма:", info["sum"], "| минимум:", info["min"], "| максимум:", info["max"])
    print("Четных значений:", info["even"])
    print("Больше среднего (", info["sum"] / len(measurements), "):",
          count_above_mean(measurements, info["sum"]))

    target = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    index, comps = linear_search(measurements, target)
    print(f"\nЛинейный поиск числа {target}: индекс {index}, сравнений {comps}")
    index, comps = linear_search(measurements, 100)
    print(f"Линейный поиск числа 100: индекс {index}, сравнений {comps}")

    print("\nПроверка простоты:")
    for n in (1, 2, 4, 17, 25, 97, 100, 7919, 1_000_003):
        prime, checked = is_prime(n)
        print(f"  {n:>9}: {'простое' if prime else 'составное':9} (проверено делителей: {checked})")

    print("\nСравнение поиска (число сравнений):")
    print(f"{'n':>6} {'лин. худш.':>11} {'лин. сред.':>11} {'бин. худш.':>11} {'бин. сред.':>11}")
    for n, lw, la, bw, ba in comparison_table():
        print(f"{n:>6} {lw:>11} {la:>11.1f} {bw:>11} {ba:>11.1f}")

    # самопроверки
    assert info == {"sum": 144, "min": 7, "max": 21, "even": 4}
    assert count_above_mean(measurements, info["sum"]) == 6
    assert linear_search(measurements, 18) == (3, 4) and linear_search(measurements, 100)[0] == -1
    assert [is_prime(n)[0] for n in (1, 2, 4, 17, 25, 97)] == [False, True, False, True, False, True]
    assert selection_sort([5, 2, 9, 1])[0] == [1, 2, 5, 9]
    assert binary_search([1, 3, 5, 7], 7)[0] == 3 and binary_search([1, 3, 5, 7], 4)[0] == -1


if __name__ == "__main__":
    main()