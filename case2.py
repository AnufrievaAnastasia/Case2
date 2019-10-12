# string constants
import local as lc
JAN = lc.TXT_JAN                     # define the values of the variables
FEB = lc.TXT_FEB
MAR = lc.TXT_MAR
APR = lc.TXT_APR
MAY = lc.TXT_MAY
JUN = lc.TXT_JUN
JUL = lc.TXT_JUL
AUG = lc.TXT_AUG
SEP = lc.TXT_SEP
OCT = lc.TXT_OCT
NOV = lc.TXT_NOV
DEC = lc.TXT_DEC

name_month = [JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

annual_income = 0
for month in range(12):
    print('{} {}:'.format(lc.TXT_WAGES, name_month[month], end=''))
    income = float(input())
    annual_income += income

status = input(lc.TXT_STATUS)

d_1 = 0
d_2 = 9075
d_3 = 36900
d_4 = 89350
d_5 = 186350
d_6 = 405100
d_7 = 406750
d_32 = 12950
d_33 = 49400
d_34 = 127550
d_35 = 206600
d_36 = 405100
d_37 = 432200


if status == lc.TXT_STATUS_1:
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



if status == lc.TXT_STATUS_3:
    if 0 <= annual_income <= 12950:
        print(0.1 * (annual_income - d_1))
    if 12951 <= annual_income <= 49400:
        print(0.1 * (d_2 - d_1) + 0.15 * (annual_income - d_32))
    if 49401 <= annual_income <= 127550:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (annual_income - d_33))
    if 127551 <= annual_income <= 206600:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (annual_income - d_34))
    if 206601 <= annual_income <= 405100:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 * (annual_income - d_35))
    if 405101 <= annual_income <= 432200:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 * (d_36 - d_35) + 0.35 * (annual_income - d_36))
    if 432201 <= annual_income:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 * (d_36 - d_35) + 0.35 * (d_37 - d_36) + 0.396 * (annual_income - d_37))

