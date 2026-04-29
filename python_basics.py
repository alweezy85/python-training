# ============================================================
# Python Basics: Syntax and Data Types
# ============================================================


# ── 1. Comments ──────────────────────────────────────────────
# This is a single-line comment

"""
This is a multi-line comment (docstring).
Use it to describe functions, classes, or modules.
"""


# ── 2. Variables and Assignment ───────────────────────────────
name = "Alice"          # str
age = 30                # int
height = 5.7            # float
is_student = True       # bool
nothing = None          # NoneType

print("=== Variables ===")
print(name, age, height, is_student, nothing)


# ── 3. Strings ────────────────────────────────────────────────
print("\n=== Strings ===")

greeting = "Hello, World!"
multiline = """Line 1
Line 2
Line 3"""

# Common string operations
print(greeting.upper())             # HELLO, WORLD!
print(greeting.lower())             # hello, world!
print(greeting.replace("World", "Python"))
print(len(greeting))                # 13
print(greeting[0])                  # H  (indexing)
print(greeting[0:5])                # Hello  (slicing)
print(f"My name is {name} and I am {age} years old.")  # f-string


# ── 4. Numbers ────────────────────────────────────────────────
print("\n=== Numbers ===")

x = 10
y = 3

print(x + y)    # Addition        → 13
print(x - y)    # Subtraction     → 7
print(x * y)    # Multiplication  → 30
print(x / y)    # Division        → 3.333...
print(x // y)   # Floor division  → 3
print(x % y)    # Modulus         → 1
print(x ** y)   # Exponentiation  → 1000

pi = 3.14159
print(round(pi, 2))     # 3.14
print(abs(-42))         # 42
print(type(x))          # <class 'int'>
print(type(pi))         # <class 'float'>


# ── 5. Booleans ───────────────────────────────────────────────
print("\n=== Booleans ===")

print(True and False)   # False
print(True or False)    # True
print(not True)         # False
print(5 > 3)            # True
print(5 == 5)           # True
print(5 != 3)           # True


# ── 6. Lists ──────────────────────────────────────────────────
print("\n=== Lists ===")

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]   # lists can hold any type

print(fruits[0])            # apple
print(fruits[-1])           # cherry (last item)
print(fruits[0:2])          # ['apple', 'banana']

fruits.append("mango")      # add to end
fruits.insert(1, "blueberry")  # insert at index
fruits.remove("banana")     # remove by value
popped = fruits.pop()       # remove and return last item

print(fruits)
print(len(fruits))          # length
print("apple" in fruits)    # membership check  → True

numbers.sort()
numbers.reverse()
print(numbers)


# ── 7. Tuples ─────────────────────────────────────────────────
print("\n=== Tuples ===")

coordinates = (10.0, 20.0)      # immutable — cannot be changed
rgb = (255, 128, 0)

print(coordinates[0])           # 10.0
print(len(rgb))                 # 3

x_coord, y_coord = coordinates  # unpacking
print(f"x={x_coord}, y={y_coord}")


# ── 8. Dictionaries ───────────────────────────────────────────
print("\n=== Dictionaries ===")

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])               # Alice
print(person.get("country", "N/A")) # safe get with default → N/A

person["email"] = "alice@example.com"   # add key
person["age"] = 31                      # update value
del person["city"]                      # delete key

print(person)
print(person.keys())
print(person.values())
print(person.items())

print("name" in person)     # True


# ── 9. Sets ───────────────────────────────────────────────────
print("\n=== Sets ===")

colors = {"red", "green", "blue"}
more_colors = {"blue", "yellow", "red"}

print(colors)
colors.add("purple")
colors.discard("green")

print(colors | more_colors)     # union
print(colors & more_colors)     # intersection
print(colors - more_colors)     # difference


# ── 10. Type Conversion ───────────────────────────────────────
print("\n=== Type Conversion ===")

print(int("42"))            # str → int
print(float("3.14"))        # str → float
print(str(100))             # int → str
print(bool(0))              # 0 → False
print(bool(1))              # 1 → True
print(list((1, 2, 3)))      # tuple → list
print(tuple([4, 5, 6]))     # list → tuple


# ── 11. Type Checking ─────────────────────────────────────────
print("\n=== Type Checking ===")

values = [42, 3.14, "hello", True, None, [1, 2], {"a": 1}, (1,), {1, 2}]
for v in values:
    print(f"{str(v):<15} → {type(v).__name__}")
