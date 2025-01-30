balance = 0

questions = [
        {
            "question": "Какой язык мы сейчас используем?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "answer": 2,
            "money": 500
        },
        {
            "question": "В каком году появился Python?",
            "options": ["1985", "1991", "2000", "2010"],
            "answer": 2,
            "money": 1000
        },
        {
            "question": "Какой оператор используется для присваивания значения переменной?",
            "options": ["==", "=", "->", "<="],
            "answer": 2,
            "money": 2500
        },
    ]


# Перебор всех вопросов с нумерацией
for index_inf, info in enumerate(questions):
    print(info['question'])
    # Перебор верных ответов
    for index_q, question in enumerate(info['options']):
        print(index_q + 1, question)

    your_answer = int(input('Введите правильный ответ: '))
    # Валидация ответа пользователя и окончание игры
    if info['answer'] == your_answer:
        balance = info['money']
        print('Всё правильно! Вы выиграли уже: ', balance, '$!')
    else:
        print('Ответ неверный :(. Вы выиграли:', balance, '$')
        break

print('Конец игры!')