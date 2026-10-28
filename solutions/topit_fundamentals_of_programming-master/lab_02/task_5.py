import sys
import tracemalloc

print("=== Часть 1. Размеры отдельных объектов ===")
ten = list(range(10))
samples = [
    ("пустой список", []),
    ("список из 10 int", ten),
    ("кортеж из 10 int", tuple(ten)),
    ("строка из 10 символов", "abcdefghij"),
    ("целое число 10", 10),
    ("None", None),
]
for title, obj in samples:
    print(f"{title:24}: {sys.getsizeof(obj)} байт")

print("\n=== Часть 2. Рост списка ===")
lst = []
last = sys.getsizeof(lst)
print(f"len={len(lst):3}  size={last}")
for i in range(100):
    lst.append(i)
    size = sys.getsizeof(lst)
    if size != last:
        print(f"len={len(lst):3}  size={size}")
        last = size

print("\n=== Часть 3. tracemalloc ===")


def measure(factory):
    tracemalloc.start()
    numbers = factory()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del numbers
    return current, peak


for title, factory in (("list(range(100_000))", lambda: list(range(100_000))),
                       ("range(100_000)", lambda: range(100_000))):
    cur, peak = measure(factory)
    print(f"{title:22}: текущий {cur / 1024:10.2f} КБ, пик {peak / 1024:10.2f} КБ")