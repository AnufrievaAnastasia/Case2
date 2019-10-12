# string constants
JAN = "январь"
FEB = "февраль"
MAR = "март"
APR = "апрель"
MAY = "май"
JUN = "июнь"
JUL = "июль"
AUG = "август"
SEP = "сентябрь"
OCT = "октябрь"
NOV = "ноябрь"
DEC = "декабрь"

name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format("Сколько Вы заработали за", name_month[month], end=''))
    income = float(input())
    annual_income += income

status = input("Напишите Ваше положение: одиночка, супружеская пара, родитель - одиночка ")

d_1 = 0
d_2 = 9075
d_3 = 36900
d_4 = 89350
d_5 = 186350
d_6 = 405100
d_7 = 406750
d_8 = 406751

if status == "одиночка":
    if 0 <= annual_income <= 9075:
        print(0.1 * (annual_income - d_1))
    if 9076 <= annual_income <= 36900:
        print(0.1 * (d_2 - d_1) + 0.15 * (annual_income - d_2))
    if 36901 <= annual_income <= 89350:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (annual_income - d_3))
    if 89351 <= annual_income <= 186350:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (annual_income - d_4))
    if 186351 <= annual_income <= 405100:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 * (annual_income - d_5))
    if 405101 <= annual_income <= 406750:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 * (d_6 - d_5) + 0.35 * (annual_income - d_6))
    if 406751 <= annual_income:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 * (d_6 - d_5) + 0.35 * (d_7 - d_6) + 0.396 * (annual_income - d_7))

if status == "родитель - одиночка":
