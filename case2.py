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

d_22 = 18150
d_23 = 73800
d_24 = 148850
d_25 = 226850
d_26 = 405100
d_27 = 457600
d_28 = 457601

if status == "одиночка":
    if 0 <= annual_income <= 9075:
        result = 0.1 * (annual_income - d_1)
        print(result)
    if 9076 <= annual_income <= 36900:
        print(0.1 * (annual_income - d_1))
    if 36901 <= annual_income <= 89350:
        print(0.1 * (annual_income - d_1))
    if 89351 <= annual_income <= 186350:
        print(0.1 * (annual_income - d_1))
    if 186351 <= annual_income <= 405100:
        print(0.1 * (annual_income - d_1))
    if 405101 <= annual_income <= 406750:
        print(0.1 * (annual_income - d_1))
    if 406751 <= annual_income:
        print(0.1 * (annual_income - d_1))

elif status == "супружеская пара":
    if 0 <= annual_income <= d_22:
        result = 0.1 * (annual_income - d_1)
    elif 18151 <= annual_income <= d_23:
        result =