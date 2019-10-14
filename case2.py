#  Anufrieva A.
# Zhuravleva A. (50%)
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

d_1 = 0                              # determine the value of the coefficient
d_2 = 9075
d_3 = 36900
d_4 = 89350
d_5 = 186350
d_6 = 405100
d_7 = 406750

d_22 = 18150
d_23 = 73800
d_24 = 148150
d_25 = 226850
d_26 = 405100
d_27 = 457600

d_32 = 12950
d_33 = 49400
d_34 = 127550
d_35 = 206600
d_36 = 405100
d_37 = 432200


if status == lc.TXT_STATUS_1:        # calculate the tax for the first status
    if 0 <= annual_income <= 9075:
        print(0.1 * (annual_income - d_1))
    elif 9076 <= annual_income <= 36900:
        print(0.1 * (d_2 - d_1) + 0.15 * (annual_income - d_2))
    elif 36901 <= annual_income <= 89350:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (annual_income - d_3))
    elif 89351 <= annual_income <= 186350:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (annual_income - d_4))
    elif 186351 <= annual_income <= 405100:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 *
              (annual_income - d_5))
    elif 405101 <= annual_income <= 406750:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 *
              (d_6 - d_5) + 0.35 * (annual_income - d_6))
    elif 406751 <= annual_income:
        print(0.1 * (d_2 - d_1) + 0.15 * (d_3 - d_2) + 0.25 * (d_4 - d_3) + 0.28 * (d_5 - d_4) + 0.33 *
              (d_6 - d_5) + 0.35 * (d_7 - d_6) + 0.396 * (annual_income - d_7))

elif status == lc.TXT_STATUS_2:      # calculate the tax for the second status
    if 0 <= annual_income <= 18150:
        print(0.1 * (annual_income - d_1))
    elif 18151 <= annual_income <= 73800:
        print(0.1 * (d_22 - d_1) + 0.15 * (annual_income - d_22))
    elif 73801 <= annual_income <= 148850:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (annual_income - d_23))
    elif 148851 <= annual_income <= 226850:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (annual_income - d_24))
    elif 226851 <= annual_income <= 405100:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 *
              (annual_income - d_25))
    elif 405101 <= annual_income <= 457600:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 *
              (d_26 - d_25) + 0.35 * (annual_income - d_26))
    elif 457601 <= annual_income:
        print(0.1 * (d_22 - d_1) + 0.15 * (d_23 - d_22) + 0.25 * (d_24 - d_23) + 0.28 * (d_25 - d_24) + 0.33 *
              ((d_26 - d_25) + 0.35 * (d_27 - d_26) + 0.396 * (annual_income - d_27)))


elif status == lc.TXT_STATUS_3:      # calculate the tax for the third status
    if 0 <= annual_income <= 12950:
        print(0.1 * (annual_income - d_1))
    elif 12951 <= annual_income <= 49400:
        print(0.1 * (d_2 - d_1) + 0.15 * (annual_income - d_32))
    elif 49401 <= annual_income <= 127550:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (annual_income - d_33))
    elif 127551 <= annual_income <= 206600:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (annual_income - d_34))
    elif 206601 <= annual_income <= 405100:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 *
              (annual_income - d_35))
    elif 405101 <= annual_income <= 432200:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 *
              (d_36 - d_35) + 0.35 * (annual_income - d_36))
    elif 432201 <= annual_income:
        print(0.1 * (d_32 - d_1) + 0.15 * (d_33 - d_32) + 0.25 * (d_34 - d_33) + 0.28 * (d_35 - d_34) + 0.33 *
              (d_36 - d_35) + 0.35 * (d_37 - d_36) + 0.396 * (annual_income - d_37))

