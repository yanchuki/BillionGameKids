import random

def load_questions():
    """ Загружает вопросы из файла или создает в коде. """
    questions = [
        {
            "question": "Какой язык мы сейчас используем?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "answer": 2,
            "level": 1
        },
                {
            "question": "В каком году появился Python?",
            "options": ["1985", "1991", "2000", "2010"],
            "answer": 2,
            "level": 1
        },
        {
            "question": "Какой оператор используется для присваивания значения переменной?",
            "options": ["==", "=", "->", "<="],
            "answer": 1,
             "level": 2
        },
        {
             "question": "Что такое IDE?",
            "options": ["Интегрированная Домашняя Электрика", "Интегрированная Среда Разработки", "Интерактивный Динамический Элемент", "Идеальный Дисплей Электроники"],
            "answer": 1,
            "level": 2
        },
        {
            "question": "Какой тип данных используется для хранения текста?",
            "options": ["int", "float", "string", "bool"],
            "answer": 2,
            "level": 3
        },
        {
           "question": "Какой оператор используется для вывода данных на экран в Python?",
           "options": ["input()", "print()", "read()", "write()"],
            "answer": 1,
            "level": 3
        },
          {
            "question": "Какая функция используется для получения пользовательского ввода в Python?",
            "options": ["get()", "input()", "receive()", "scan()"],
            "answer": 1,
            "level": 4
        },
          {
            "question": "Что такое список (list) в Python?",
            "options": ["Упорядоченная изменяемая коллекция элементов", "Неупорядоченная неизменяемая коллекция элементов", "Упорядоченная неизменяемая коллекция элементов", "Набор строк"],
            "answer": 0,
             "level": 4
        },
         {
            "question": "Что такое цикл for?",
            "options": ["Цикл с предусловием", "Цикл с постусловием", "Цикл, выполняемый определенное количество раз", "Бесконечный цикл"],
            "answer": 2,
             "level": 5
        },
        {
            "question": "Что делает оператор `if`?",
            "options": ["Выполняет блок кода, если условие истинно", "Выполняет блок кода в любом случае", "Прерывает цикл", "Создает функцию"],
            "answer": 0,
            "level": 5
        },
    ]
    return questions


def show_question(question):
    """ Показывает вопрос и варианты ответов. """
    print(f"\nВопрос: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i + 1}. {option}")


def get_user_answer():
    """ Получает ответ пользователя. """
    while True:
        try:
            answer = int(input("Ваш ответ (номер варианта): "))
            if 1 <= answer <= 4:
                return answer - 1
            else:
                print("Введите корректный номер варианта.")
        except ValueError:
            print("Введите число!")


def check_answer(question, user_answer):
    """ Проверяет правильность ответа. """
    return user_answer == question['answer']


def game():
    """ Основная логика игры. """
    questions = load_questions()
    money = 0
    levels = {1: 100, 2: 500, 3: 1000, 4: 5000, 5: 20000}

    used_questions = []

    print("Добро пожаловать в игру 'Кто хочет стать миллионером'!")

    for level in range(1, 6):

        level_questions = [q for q in questions if q['level'] == level]
        question = random.choice(level_questions)
        while question in used_questions:
            question = random.choice(level_questions)
        used_questions.append(question)

        show_question(question)
        user_answer = get_user_answer()
        if check_answer(question, user_answer):
            money = levels[level]
            print(f"Правильно! Ваш выигрыш: {money} руб.")
            if level == 5:
                print(f"Поздравляю вы миллионер! Ваш выигрыш {money}")
                break
            input("Нажмите Enter для продолжения")
        else:
            print(f"Неправильно! Вы проиграли. Ваш выигрыш составил {money} руб.")
            break


if __name__ == "__main__":
    game()