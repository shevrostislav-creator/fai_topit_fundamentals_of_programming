import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


print("")

import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())


#практическая задача
class Record:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Record({self.name!r})"

print("\n=== Реестр на WeakValueDictionary ===")
registry = weakref.WeakValueDictionary()

first = Record("first")
second = Record("second")
third = Record("third")

registry["first"] = first
registry["second"] = second
registry["third"] = third

print("Сразу после регистрации:", sorted(registry.keys()))

del third
print("После удаления временной ссылки на third:", sorted(registry.keys()))

del second
print("После удаления сильной ссылки на second:", sorted(registry.keys()))

print("first всё ещё жив:", registry.get("first"))
print("second в реестре:", "second" in registry)
print("third в реестре:", "third" in registry)