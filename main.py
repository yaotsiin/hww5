import colorama
import inspect

print("Атрибути бібліотеки Colorama:")
print(dir(colorama))

print("\nІнформація про бібліотеку:")
print(inspect.getdoc(colorama))

print("\nФункції бібліотеки:")
for name, obj in inspect.getmembers(colorama, inspect.isfunction):
    print(name, inspect.signature(obj))

print("\nКласи бібліотеки:")
for name, obj in inspect.getmembers(colorama, inspect.isclass):
    print(name)
