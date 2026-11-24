#Эксперимент А
x = 17
y = 5
print("x + y = ", x + y,  type(x + y))
print("x - y = ", x - y,  type(x - y))
print("x * y = ", x*y,  type(x*y))
print("x / y = ", x/y,  type(x / y))
print("x // y = ", x // y,  type(x // y))
print("x % y = ", x % y,  type(x % y))
print("x ** y = ", x ** y, type(x ** y))

#Эксперимент B
print(2**1000)

#Эксперимент C
import math

result = 0.1 + 0.2
print("result = 0.1 + 0.2")
print("result =", result)
print("result = 0.3 :", result == 0.3)
print("result - 0.3 =" , result - 0.3)
print("math.isclose(result, 0.3) = ", math.isclose(result,0.3))

#Эксперимент D
print("int('42')      = ", int("42"), "  ", type(int("42")))
print("float('3.14')  = ", float("3.14"), "  ", type(float("3.14")))
print("str(2026)      = ", str(2026), "  ", type(str(2026)))
print("")
print("bool(0)        = ", bool(0), "  ", type(bool(0)))
print("bool(-1)       = ", bool(-1), "  ", type(bool(-1)))
print("bool("")         = ", bool(""), "  ", type(bool("")))
print("bool('False')  = ", bool("False"), "  ", type(bool("False")))
print("")
print("complex(2, -3) = ", complex(2, -3), "  ", type(complex(2, -3)))
print("Действительная часть:",  complex(2, -3).real)
print("мнимая часть:",  complex(2, -3).imag)