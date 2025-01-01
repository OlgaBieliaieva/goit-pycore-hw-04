def total_salary(path):
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        total = 0
        count = 0

        for line in lines:
            
            try:
                _, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            except ValueError:
                print(f"Пропускаємо неправильний формат рядка: {line.strip()}")

        if count == 0:
            raise ValueError("Файл не містить валідних даних про зарплати.")

        average = round(total / count, 2)

        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return None, None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None, None


total, average = total_salary("./salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
