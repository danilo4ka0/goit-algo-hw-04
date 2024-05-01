"""def total_salary(path):
    try:
        # Відкриваємо файл і читаємо дані
        with open(path, 'r', encoding='') as file:
            lines = file.readlines()
        
        # Ініціалізуємо змінні для обчислення загальної та середньої зарплати
        total_salary = 0
        num_developers = len(lines)

        # Обчислюємо загальну суму зарплат
        for line in lines:
            _, salary_str = line.split(',')
            total_salary += int(salary_str)

        # Обчислюємо середню зарплату
        average_salary = total_salary / num_developers

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")

# Приклад використання функції
total, average = total_salary(r"C:\\Users\\demo\\Desktop\\my_r\\file.txt.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")"""






def total_salary(path):
    try:
        # Відкриваємо файл і читаємо дані
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Ініціалізуємо змінні для обчислення загальної та середньої зарплати
        total_salary = 0
        num_developers = len(lines)

        # Обчислюємо загальну суму зарплат
        for line in lines:
            _, salary_str = line.split(',')
            total_salary += int(salary_str)

        # Обчислюємо середню зарплату
        average_salary = total_salary / num_developers

        return total_salary, average_salary

    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено.")
        return None, None
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
        return None, None

# Приклад використання функції
total, average = total_salary("file1.txt")

if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
