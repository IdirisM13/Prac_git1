tasks = []

while True:
    print("\n===== МЕНЕДЖЕР ЗАДАЧ =====")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("Выбери действие: ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)
        print("Задача добавлена!")

    elif choice == "2":
        if len(tasks) == 0:
            print("Список пуст!")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("Нет задач для удаления!")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")

            number = int(input("Номер задачи: "))

            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                print("Задача удалена!")
            else:
                print("Неверный номер!")

    elif choice == "4":
        print("До свидания!")
        break

    else:
        print("Неверный выбор!")
