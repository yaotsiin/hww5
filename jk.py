from colorama import init, Fore, Back, Style

init(autoreset=True)

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Fore.BLUE + "Синій текст")

print(Back.YELLOW + "Текст на жовтому фоні")

print(Style.BRIGHT + "Яскравий текст")
print(Style.DIM + "Приглушений текст")

print(Fore.CYAN + Back.BLACK + Style.BRIGHT +
      "Кольоровий текст із фоном")

print("Програма завершена!")