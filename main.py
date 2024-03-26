print("приветствую вас в викторине по MSM")

questions = ["можно ли вывести Сахагитора на острове растений?",
             "поёт ли Стоарб на острове земли *put you're hands up*?",
             "можно ли разместить редкого Kоробаса на острове вублинов?",
             "можно ли кормить монстров больше 20 уровня?",
             "есть ли Парсалона на острове земли?",
             "можно ли установить иконку Шажара любого цвета?",
             "если соединить Исболалиста и Тирокса получится ли Вужас?"]
answers = ["нет", "да", "нет", "нет", "нет", "нет", "да"]
score = 0

print("первый вопрос: ", questions[0])
user_answer = input("ваш ответ: ")
correct = answers[0] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("второй вопрос: ", questions[1])
user_answer = input("ваш ответ: ")
correct = answers[1] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("третий вопрос: ", questions[2])
user_answer = input("ваш ответ: ")
correct = answers[2] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("четвёртый вопрос: ", questions[3])
user_answer = input("ваш ответ: ")
correct = answers[3] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("пятый вопрос: ", questions[4])
user_answer = input("ваш ответ: ")
correct = answers[4] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("шестой вопрос: ", questions[5])
user_answer = input("ваш ответ: ")
correct = answers[5] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

print("седьмой вопрос: ", questions[6])
user_answer = input("ваш ответ: ")
correct = answers[6] == user_answer.lower()
if correct:
    print("правильно!")
    score += 1
else:
    print("неправильно!")

if score <= 2:
    print("плохо ;(")
elif score <= 5:
    print("хорошо :)")
elif score <= 7:
    print("красавчик ;D")
