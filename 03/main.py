import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_directory_structure(path: Path, level: int = 0):
    # Перевірка чи існує шлях і чи це директорія
    if not path.exists():
        print(Fore.RED + f"Помилка: Шлях {path} не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Помилка: {path} не є директорією.")
        return

    # Отримання всіх файлів та папок у поточній директорії
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + '  ' * level + f"📂 {item.name}")
            # Рекурсивний виклик для відображення вмісту підкаталогів
            print_directory_structure(item, level + 1)
        elif item.is_file():
            print(Fore.GREEN + '  ' * level + f"📜 {item.name}")

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії як аргумент.")
        sys.exit(1)

    # Отримання шляху до директорії з аргументів командного рядка
    dir_path = sys.argv[1]
    print_directory_structure(Path(dir_path))

if __name__ == "__main__":
    main()