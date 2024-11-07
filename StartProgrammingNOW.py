from typing import Tuple

print("Erste Stunde in Python")

# Control + Shift + F10 -> Shortcut um die aktuelle, geöffnete Datei auszuführen
a: int = "Ich bin ein String"
b = 5
print(b)

print("Der Wert von a ist: " + str(a))
print(f"Der Wert von a ist: {a}")

c = [1, 2, "Hallo", 2.6]
print(c)
dictionary = {"Summe": 3, "key": "value", str: {5: 7}, print: [a, b]}
print(dictionary)
print(print())


def x_squared(x: float) -> float:
    result = x * x
    return result


print(x_squared(2.5))


def multiply(z: float, y: float) -> float:
    return z * y


x = 3


# "->" return type hints
def multiply_and_divide(x: float, y: float) -> tuple[float, float]:
    return multiply(x, y), x / y


mul, div = multiply_and_divide(25, 7)
print(mul)
print(div)
func = multiply_and_divide
func(25, 7)
print(multiply_and_divide(10, 5))


def multiply_or_divide(x: float, y: float, multiplication: bool = True) -> float:
    if multiplication:
        return x * y
    return x / y


print(multiply_or_divide(4.2, 6.8))
print(multiply_or_divide(4.2, 6.8, multiplication=True))
print(multiply_or_divide(4.2, 6.8, multiplication=False))

print("git")




