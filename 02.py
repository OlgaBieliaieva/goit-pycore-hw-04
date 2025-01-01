def get_cats_info(path):
    try:
        
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        cats_info = []

        for line in lines:
            try:
                cat_id, name, age = line.strip().split(',')
                cats_info.append({"id": cat_id, "name": name, "age": age})
            except ValueError:
                print(f"Пропускаємо неправильний формат рядка: {line.strip()}")

        return cats_info

    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

cats_info = get_cats_info("./cats_file.txt")
if cats_info:
    print(cats_info)
