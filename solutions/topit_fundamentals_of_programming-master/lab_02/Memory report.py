import sys
import tracemalloc
from dataclasses import dataclass

N = 100_000


@dataclass
class Measurement:
    scenario: str
    items: int
    container_size: int
    current_kb: float
    peak_kb: float


def measure(scenario, factory, items):
    """Только измерение: возвращает данные, ничего не печатает."""
    tracemalloc.start()
    obj = factory()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return Measurement(scenario, items, sys.getsizeof(obj), current / 1024, peak / 1024)


def collect_measurements():
    return [
        measure("list(range(N))", lambda: list(range(N)), N),
        measure("tuple(range(N))", lambda: tuple(range(N)), N),
        measure("range(N)", lambda: range(N), N),
    ]


def format_report(results):
    """Только форматирование: строит текст отчёта из готовых данных."""
    lines = [f"{'Сценарий':18}{'Элементов':>11}{'Размер, Б':>12}"
             f"{'Текущая, КБ':>14}{'Пик, КБ':>12}"]
    for r in results:
        lines.append(f"{r.scenario:18}{r.items:>11}{r.container_size:>12}"
                     f"{r.current_kb:>14.2f}{r.peak_kb:>12.2f}")
    base, lazy = results[0], results[-1]
    ratio = base.peak_kb / lazy.peak_kb if lazy.peak_kb else float("inf")
    lines.append("")
    lines.append(f"Отношение пиков {base.scenario} / {lazy.scenario}: {ratio:.0f}x")
    return "\n".join(lines)


if __name__ == "__main__":
    print(format_report(collect_measurements()))
