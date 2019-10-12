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
d_24 = 148150
d_25 = 226850
d_26 = 405100
d_27 = 457600

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

elif status == "супружеская пара":
    if 0 <= annual_income <= 18150:
        print(0.1 * (annual_income - d_1))
    if 18151 <= annual_income <= 73800:
        print(0.1 * (d_22 - d_1) + 0.15 * (annual_income - d_22))
    if 73801 <= annual_income <= 148850:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (annual_income - d_23))
    if 148851 <= annual_income <= 226850:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (annual_income - d_24))
    if 226851 <= annual_income <= 405100:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 * (annual_income - d_25))
    if 405101 <= annual_income <= 457600:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 * (d_26 - d_25) + 0.35 * (annual_income - d_26))
    if 457601 <= annual_income:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 * (d_26 - d_25) + 0.35 * (d_27 - d_26) + 0.396 * (annual_income - d_27))




elif status == "родитель - одиночка":
