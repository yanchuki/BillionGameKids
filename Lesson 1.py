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

# Получение вложенных данных

# Вопрос
print(questions[0]['question'])
# Ответы
print(questions[0]['options'][0])
print(questions[0]['options'][1])
print(questions[0]['options'][2])
print(questions[0]['options'][3])
# Номер верного ответа
print(questions[0]['answer'])
balance += questions[0]['money']

print(balance)
