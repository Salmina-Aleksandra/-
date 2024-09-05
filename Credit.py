from datetime import datetime
from array import *
import array
current_datetime = datetime.now()
today = current_datetime.year
print(" ")
print(" ")
print("Вы используете программу Сбербанка, которая помогает Вам с решением о выдаче кредита.")
print("")
print("Условия выдачи кредита:")
print("  1 - кредит выдается в рублях")
print("  2 - минимальная сумма кредита 15 000 (для Москвы 45 000)")
print("  3 - максимальная сумма кредита 1 500 000")
print("  4 - срок взятия кредита от 3 месяцев до 5 лет")
print(" ")
print("Требования к заёмщику:")
print("  1 - возраст не менее 21 года")
print("  2 - возраст на момент возврата не более 65 лет")
print("  3 - стаж работы не менее 6 месяцев на текущем месте работы и не менее 1 года общего стажа за последние 5 лет")
print("      (для клиентов Сбербанка не менее 3 месяцев на текущем месте работы)")
print(" ")
print("Проценты потребительского кредита:")
print(" ")
print("Кредит на срок от 3 до 24 месяцев:")
print("Для физических лиц, получающие зарплату или пенсию на счет, открытый в Сбербанке")
print("процентная ставка по потребительскому кредиту составит от 14.9% до 20.9%")
print("Для других категорий граждан процентная ставка по кредиту может составить от 16.9% до 21.9%")
print(" ")
print("Кредит на срок от 25 до 60 месяцев:")
print("Для физических лиц, получающие зарплату или пенсию на счет, открытый в Сбербанке")
print("процентная ставка по потребительскому кредиту составит от 15.9% до 21.9%")
print("Для других категорий граждан процентная ставка по кредиту может составить от 17.9% до 22.9%")
print(" ")

print("Введите вашу фамилию")
surname = input()
print("Введите ваше имя")
name = input()
print("Введите ваше отчество (если есть)")
patronymic = input()
print(" ")

print("Введите в числовом формате вашу дату рождения полностью")
print("Формат ввода: 29.03.1999")
print("День: ")
day = input()
print("Месяц: ")
month = input()
print("Год: ")
year = input()
age = int(today) - int(year)  # вычисление возраста пользователя

# переменные для счетчика
a = 0
b = 1
while a < b:
    a = 2
    if (age > 65) or (age < 21):  # проверка соответсвия возраста пользователя с условиями задачи
        print("Извините, но Ваш возраст не соответствует условиям (см. пункт 1 и/или 2 требований к заемщику)")
        a = 2
        import sys

        sys.exit("Мы не можем выдать вам кредит! Приносим свои извинения.")

print(" ")
print("Заполните данные о месте проживания/пребывания")
region = input("Введите регион: ")
city = input("Введите город: ")
street = input("Введите улицу: ")
address = input("Введите дом/квартиру: ")
print(" ")

print(name + " " + patronymic + ", у Вас есть открытый счет в Сбербанке?")
answer = input("Да/Нет: ")
print(" ")

# переменные для счетчика
a = 0
b = 1
while a < b:
    a = 2
    print("Введите Ваш стаж работы в месяцах на текущем месте работы (если не работаете введите 0)")
    WExperience = input()
    if (answer == "Да") or (answer == "да"):                    # проверка соответсвия опыта работы в зависимости от
        if (int(WExperience) == 0) or (int(WExperience) < 3):   # выбора есть ли счет у пользователя в Сбербанке или нет
            print("Извините, но мы не можем одобрить Вам кредит (см. пункт 3 требований к заемщику)")
            a = 0
            import sys

            sys.exit("Мы не можем выдать вам кредит! Приносим свои извинения.")
        else:
            a = 2
    else:
        if (int(WExperience) == 0) or (int(WExperience) < 6):
            print("Извините, но мы не можем одобрить Вам кредит (см. пункт 3 требований к заемщику)")
            a = 0
            import sys

            sys.exit("Мы не можем выдать вам кредит! Приносим свои извинения.")
        else:
            a = 2

print(" ")
print(name + " " + patronymic + ", Вы являетесь физическим лицом?")
face = input("Да/Нет: ")
print(" ")

print("Выберите вид платежа по кредиту: ")
print(" 1. Аннуитетный (фиксированная сумма выплат за каждый месяц)")
print(" 2. Дифференцированный (разная сумма выплат за каждый месяц в зависимости от остатка долга)")
t = input()
print(" ")

a = 0
b = 1
while a < b:
    print("Какую сумму хотите взять в кредит?")
    suma = input("Сумма кредита: ")
    a = 2

    if (city == "Москва") or (city == "москва"):  # проверка на соответсвие суммы кредита с условиями
        if (int(suma) < 45000) or (int(suma) > 1500000):
            print("Извините, но такую сумму нельзя взять в кредит (см. пункт 3 условий выдачи кредита)")
            a = 0
            import sys
            sys.exit("Мы не можем выдать вам кредит! Приносим свои извинения.")
    else:
        if (int(suma) < 15000) or (int(suma) > 1500000):
            print("Извините, но такую сумму нельзя взять в кредит (см. пункт 3 условий выдачи кредита)")
            a = 0
            import sys
            sys.exit("Мы не можем выдать вам кредит! Приносим свои извинения.")
print(" ")

print("Выберите примерные сроки кредита: ")
a = 0
b = 1
while a < b:
    print(" 1. От 3 до 24 месяцев.")
    print(" 2. От 25 до 60 месяцев.")
    choice = input()  # выбор срока кредита
    if int(choice) == 1:
        choice_1 = int(input("Введите конкретное число месяцев, на которое Вы хотите взять кредит (3-24): "))
        a = 2
    else:
        choice_1 = int(input("Введите конкретное число месяцев, на которое Вы хотите взять кредит (25-60): "))
        a = 2
    term = int(age) * 12 + int(month) + int(choice_1) # вычисление возраста пользователя на момент закрытия кредита
    if term > (65 * 12):
        print("Извините, но нельзя взять кредит на такой срок. На момент погашения кредита вам будет более 65 лет ")
        print(" (см. пункт 2 требований к заемщику")
        a = 0
        print(" ")
# рассчет процента в зависимости от информации о пользователе
if ((answer == "Да") or (answer == "да")) and ((face == "Да") or (face == "да")) and (int(choice) == 1):
    if (int(choice_1) >= 3) and (int(choice_1) <= 6.5):
        percent = 20.9
    else:
        if (int(choice_1) > 6.5) and (int(choice_1) <= 10):
            percent = 19.9
        else:
            if (int(choice_1) > 10) and (int(choice_1) <= 13.5):
                percent = 18.9
            else:
                if (int(choice_1) > 13.5) and (int(choice_1) <= 17):
                    percent = 17.9
                else:
                    if (int(choice_1) > 17) and (int(choice_1) <= 20.5):
                        percent = 16.9
                    else:
                        if (int(choice_1) > 20.5) and (int(choice_1) < 24):
                            percent = 15.9
                        else:
                            if int(choice_1) == 24:
                                percent = 14.9
else:
    if ((answer == "Да") or (answer == "да")) and ((face == "Нет") or (face == "нет")) and (int(choice) == 1):
        if (int(choice_1) >= 3) and (int(choice_1) <= 7.2):
            percent = 21.9
        else:
            if (int(choice_1) > 7.2) and (int(choice_1) <= 11.4):
                percent = 20.9
            else:
                if (int(choice_1) > 11.4) and (int(choice_1) <= 15.6):
                    percent = 19.9
                else:
                    if (int(choice_1) > 15.6) and (int(choice_1) <= 19.8):
                        percent = 18.9
                    else:
                        if (int(choice_1) > 19.8) and (int(choice_1) < 24):
                            percent = 17.9
                        else:
                            if int(choice_1) == 24:
                                percent = 16.9
    else:
        if ((answer == "Да") or (answer == "да")) and ((face == "Да") or (face == "да")) and (int(choice) == 2):
            if (int(choice_1) >= 25) and (int(choice_1) <= 30.8):
                percent = 21.9
            else:
                if (int(choice_1) > 30.8) and (int(choice_1) <= 36.6):
                    percent = 20.9
                else:
                    if (int(choice_1) > 36.6) and (int(choice_1) <= 42.4):
                        percent = 19.9
                    else:
                        if (int(choice_1) > 42.4) and (int(choice_1) <= 48.2):
                            percent = 18.9
                        else:
                            if (int(choice_1) > 48.2) and (int(choice_1) <= 54):
                                percent = 17.9
                            else:
                                if (int(choice_1) > 54) and (int(choice_1) <= 59.8):
                                    percent = 16.9
                                else:
                                    if (int(choice_1) > 59.8) and (int(choice_1) <= 60):
                                        percent = 15.9
        else:
            if ((answer == "Да") or (answer == "да")) and ((face == "Нет") or (face == "нет")) and (int(choice) == 2):
                if (int(choice_1) >= 25) and (int(choice_1) <= 32):
                    percent = 22.9
                else:
                    if (int(choice_1) > 32) and (int(choice_1) <= 39):
                        percent = 21.9
                    else:
                        if (int(choice_1) > 39) and (int(choice_1) <= 46):
                            percent = 20.9
                        else:
                            if (int(choice_1) > 46) and (int(choice_1) <= 53):
                                percent = 19.9
                            else:
                                if (int(choice_1) > 53) and (int(choice_1) < 60):
                                    percent = 18.9
                                else:
                                    if int(choice_1) == 60:
                                        percent = 17.9
            else:
                if ((answer == "Нет") or (answer == "нет")) and ((face == "Нет") or (face == "нет")) and (int(choice) == 1):
                    if (int(choice_1) >= 3) and (int(choice_1) <= 7.2):
                        percent = 21.9
                    else:
                        if (int(choice_1) > 7.2) and (int(choice_1) <= 11.4):
                            percent = 20.9
                        else:
                            if (int(choice_1) > 11.4) and(int(choice_1) <= 15.6):
                                percent = 19.9
                            else:
                                if (int(choice_1) > 15.6) and (int(choice_1) <= 19.8):
                                    percent = 18.9
                                else:
                                    if (int(choice_1) > 19.8) and (int(choice_1) < 24):
                                        percent = 17.9
                                    else:
                                        if int(choice_1) == 24:
                                            percent = 16.9
                else:
                    if ((answer == "Нет") or (answer == "нет")) and ((face == "Нет") or (face == "нет")) and (int(choice) == 2):
                        if (int(choice_1) >= 25) and (int(choice_1) <= 32):
                            percent = 22.9
                        else:
                            if (int(choice_1) > 32) and (int(choice_1) <= 39):
                                percent = 21.9
                            else:
                                if (int(choice_1) > 39) and (int(choice_1) <= 46):
                                    percent = 20.9
                                else:
                                    if (int(choice_1) > 46) and (int(choice_1) <= 53):
                                        percent = 19.9
                                    else:
                                        if (int(choice_1) > 53) and (int(choice_1) < 60):
                                            percent = 18.9
                                        else:
                                            if int(choice_1) == 60:
                                                percent = 17.9
                    else:
                        if ((answer == "Нет") or (answer == "нет")) and ((face == "Да") or (face == "да")) and (int(choice) == 1):
                            if (int(choice_1) >= 3) and (int(choice_1) <= 7.2):
                                percent = 21.9
                            else:
                                if (int(choice_1) > 7.2) and (int(choice_1) <= 11.4):
                                    percent = 20.9
                                else:
                                    if (int(choice_1) > 11.4) and (int(choice_1) <= 15.6):
                                        percent = 19.9
                                    else:
                                        if (int(choice_1) > 15.6) and (int(choice_1) <= 19.8):
                                            percent = 18.9
                                        else:
                                            if (int(choice_1) > 19.8) and (int(choice_1) < 24):
                                                percent = 17.9
                                            else:
                                                if int(choice_1) == 24:
                                                    percent = 16.9
                        else:
                            if ((answer == "Нет") or (answer == "нет")) and ((face == "Да") or (face == "да")) and (int(choice) == 2):
                                if (int(choice_1) >= 25) and (int(choice_1) <= 32):
                                    percent = 22.9
                                else:
                                    if (int(choice_1) > 32) and (int(choice_1) <= 39):
                                        percent = 21.9
                                    else:
                                        if (int(choice_1) > 39) and (int(choice_1) <= 46):
                                            percent = 20.9
                                        else:
                                            if (int(choice_1) > 46) and (int(choice_1) <= 53):
                                                percent = 19.9
                                            else:
                                                if (int(choice_1) > 53) and (int(choice_1) < 60):
                                                    percent = 18.9
                                                else:
                                                    if int(choice_1) == 60:
                                                        percent = 17.9
print(" ")

print(name + " " + patronymic + ", желаете ли Вы увидеть примерный график платежей по Вашему кредиту?")
answer_1 = input("Да/Нет: ")

print(" ")
print(" ")
print("---------------------------------------------------------------------------------------------------------------")
print("Поздравляем Вас! Вам одобрен кредит!")
print("Клиент: " + surname + " " + name + " " + patronymic)
print("Дата рождения: " + day + " " + month + " " + year)
print("Текущий возраст: " + str(age))
print("Место проживания/пребывания: " + region + " " + city + " " + street + " " + address)
if answer == "Да" or answer == "да":
    print("Имеет открытый счет в Сбербанке")
else:
    print("Не имеет открытый счет в Сбербанке")
if face == "Да" or face == "да":
    print("Является физическим лицом")
else:
    print("Относится к иной категории граждан")
print("Стаж работы в месяцах на текущем месте: " + WExperience)
print("Сумма кредита: " + str(suma) + " руб.")
print("Срок погашения кредита: " + str(choice_1) + " мес.")
print("Процентная ставка по кредиту: " + str(percent))
print("---------------------------------------------------------------------------------------------------------------")

# вычисление графика выплат
if answer_1 == "Да" or answer_1 == "да":
    print(" ")
    print("График выплат:")
    print(" ")
    print("-----------------------------------------------------------------------------------------------------------")
    print(" ")
    print("Месяц     " + "Сумма платежа    " + "Платеж по осн. долгу    " + "Платеж по процентам          " + "Остаток долга    ")
    p = percent  # рассчитанный процент выше
    s = float(suma)  # сумма кредита для рассчетов, чтобы не изменить ее
    m = choice_1  # срок кредита, для счетчика
    mon = 1  # переменная для вывода кол-ва месяца для таблицы
    perep = 0  # переменная для счета выплат
    if int(t) == 1:
        i = p/100/12  # вычисление ежемесячного процента
        P = round(s * (i + i/(((1.0 + i) ** choice_1) - 1.0)), 4)  # вычисление платежа в счет основного долга
        while m != 0:
            In = round(s * i, 4)  # вычисление платежа в счет процентов
            sn = round(P - In, 4)  # вычисление общей суммы выплат в месяц
            s = round(s - sn, 4)  # вычисление остатка долга
            if s < 0.5:  # условие создано, тк в последнем месяце остаток долга не равен в некоторых случаях нулю, а равен
                s = 0   # 0,00003 и тп, это происходит из-за погрешности при округлении чисел
            print("  " + str(mon) + "          " + str(P) + "        " + str(sn) + "               " + str(In) + "                 " + str(s))
            print(" ")
            m = m - 1  # счетчик месяцев в обратном порядке для выхода из цикла
            mon = mon + 1  # счетчик месяцев от 1 до нужно, сделано для красивого вывода в конечной таблице
            perep = round(perep + P, 4)  # вычисление общих выплат
        print("Сумма кредита" + " " + str(suma) + " руб." + " " + "Переплата составила" + " " + str(round(perep - int(suma), 4)) + " руб. " + " " + "Общая сумма выплат" + " " + str(perep) + " руб.  ")
        print(" ")

    else:
        if int(t) == 2:
            sn = round(s/m, 4)  # вычисление платежа в счет основного долга
            while m != 0:
                In = round((s * (p/100) * 30)/365, 4)  # вычисление платежа в счет процентов
                P = round(sn + In, 4)  # вычисление общей суммы выплат в месяц
                s = round(s - sn, 4)  # вычисление остатка долга
                if s < 0:  # условие создано, тк в последнем месяце остаток долга не равен в некоторых случаях нулю, а
                    s = 0  # равен 0,00004 и тп, это происходит из-за погрешности при округлении чисел
                print("  " + str(mon) + "          " + str(P) + "        " + str(sn) + "               " + str(In) + "                 " + str(s))
                print(" ")
                m = m - 1  # счетчик месяцев в обратном порядке для выхода из цикла
                mon = mon + 1  # счетчик месяцев от 1 до нужного, сделано для красивого вывода в конечной таблице
                perep = round(perep + P, 4)  # вычмсление общих выплат
        print(" ")
        print("-------------------------------------------------------------------------------------------------------")
        print(" ")
        print("Сумма кредита" + " " + str(suma) + " руб." + " " + "Переплата составила" + " " + str(round(perep - int(suma), 4)) + " руб. " + " " + "Общая сумма выплат" + " " + str(perep) + " руб.  ")
        print(" ")