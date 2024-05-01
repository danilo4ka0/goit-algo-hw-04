def get_cats_info(path):
    try:
        # Відкриваємо файл і читаємо дані
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Ініціалізуємо список для зберігання інформації про котів
        cats_info = []

        # Обробляємо кожен рядок в файлі
        for line in lines:
            # Розділяємо рядок за комами
            cat_data = line.strip().split(',')

            # Перевіряємо, чи отримано правильні дані
            if len(cat_data) == 3:
                # Створюємо словник для кожного кота і додаємо його до списку
                cat_info = {"id": cat_data[0], "cat name": cat_data[1], "age": cat_data[2]}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None

# Приклад використання функції
cats_info = get_cats_info("file2.txt")

if cats_info is not None:
    for cat in cats_info:
        print(cat)
