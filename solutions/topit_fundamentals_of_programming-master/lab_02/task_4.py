import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("\nАвтоматический сборщик включён:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений:")
for i, stat in enumerate(gc.get_stats()):
    print(f"  поколение {i}: {stat}")

id_first, id_second = id(first), id(second)
print("\nid до удаления:", id_first, id_second)

del first, second
collected = gc.collect()
print("gc.collect() вернул:", collected)



print("\n=== Эксперимент с отключённым сборщиком ===")
gc.collect()
gc.disable()
try:
    print("Сборщик включён:", gc.isenabled())
    for _ in range(5):
        a, b = [], []
        a.append(b)
        b.append(a)
    del a, b
    print("Циклов создано: 5 (внешние ссылки удалены, объекты ещё в памяти)")
    print("gc.collect() вернул:", gc.collect())
finally:
    gc.enable()
print("Сборщик восстановлен:", gc.isenabled())

print("\n=== Практическая задача: граф ===")
gc.collect()
before = gc.collect()
print("Собрано до создания графа:", before)

node_a = {"name": "A", "links": []}
node_b = {"name": "B", "links": []}
node_c = {"name": "C", "links": []}
node_d = {"name": "D", "links": []}

node_a["links"].append(node_b)
node_b["links"].append(node_c)
node_c["links"].append(node_a)

for node in (node_a, node_b, node_c, node_d):
    print(f"  {node['name']} -> {[n['name'] for n in node['links']]}")

del node_a, node_b, node_c
after = gc.collect()
print("Собрано после удаления графа:", after)

assert node_d["name"] == "D" and node_d["links"] == []
print("Независимый узел D остался доступен:", node_d)