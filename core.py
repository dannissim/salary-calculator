# app that calculates your monthly salary and your savings after taking off by-law expenses: Pension savings,
# "Keren hishtalmut", Health insurance, income tax, social insurance.
# Need to fix: max hishtalmut and pension deposit from bruto
# should update tax bracket
PENSION_RATE = 0.06  # 7% off bruto, must be at least 6%
HEALTH_INS = [0.031, 0.05]
HISHTALMUT_RATE = 0.025  # 2.5% off bruto
EMPLOYER_HISHTALMUT = 0.075
EMPLOYER_PENSION = 0.065
EMPLOYER_SEVER = 0.0833
DISCOUNT_POINTS = 2.25
POINT_WORTH = 218
DISCOUNT = DISCOUNT_POINTS * POINT_WORTH
#   if employer deposits more than this amnt, the difference will be added to the income and tax will be paid
MAX_EMPLOYER_SEVER = 2833
#   you get 35% of your pension deposit as tax deduction, up to max pension deposit
MAX_PENSION =  616  
PENSION_TAX_DEDUCTION = 0.35
#   employer pension does not count as income for tax to be paid up to max employer pension, above this, the
#   difference will be added to the salary for which income tax will be calculated
MAX_EMPLOYER_PENSION = 148
SOCIAL_INS = [0.004, 0.07]
AVG_INCOME = 10273
SIXTYPERC_AVG_INCOME = int(0.6 * AVG_INCOME)  # social and health insurance fee blocks depend on 60% avg national income
# INCOMETAX_THRESH = 4837
TAX_BRACKET = [6310, 9050, 14530, 20200, 42030, 54130]
TAX_RATES = [0.1, 0.14, 0.2, 0.31, 0.35, 0.47, 0.5]
MAX_HISHTALMUT = 15712  # this is the max salary in which the there isn't income tax on employer deposit
# this is the amount which the no income tax is paid on employer deposit in keren hishtalmut
MAX_EMPLOYER_HISHTALMUT= EMPLOYER_HISHTALMUT * MAX_HISHTALMUT   


def income_tax(bruto):
    # calculate bruto_tobe_taxed
    bruto_tobe_taxed = bruto
    employer_pens = EMPLOYER_PENSION * bruto
    if employer_pens > MAX_EMPLOYER_PENSION:
        bruto_tobe_taxed += employer_pens - MAX_EMPLOYER_PENSION
    severence = EMPLOYER_SEVER * bruto
    if severence > MAX_EMPLOYER_SEVER:
        bruto_tobe_taxed += severence - MAX_EMPLOYER_HISHTALMUT
    employer_hisht = bruto * EMPLOYER_HISHTALMUT
    if employer_hisht > MAX_EMPLOYER_HISHTALMUT:
        bruto_tobe_taxed += employer_hisht - MAX_EMPLOYER_HISHTALMUT

    # calculate income tax without deductions
    arr = TAX_BRACKET + [bruto_tobe_taxed]
    arr.sort()
    j = arr.index(bruto_tobe_taxed)
    if j == 0:
        res = bruto_tobe_taxed * TAX_RATES[0]
    else:
        res = TAX_BRACKET[0] * TAX_RATES[0]
        for i in range(1, j+1):
            res += (arr[i] - arr[i - 1]) * TAX_RATES[i]

    # calculate deductions
    pension = bruto * PENSION_RATE
    res -= (PENSION_TAX_DEDUCTION * min(MAX_PENSION, pension) + DISCOUNT)
    return max(int(res), 0)
     

# calculates fee for health or social insurance, flag true for health ins., flag false for social ins.
def calc_ins_fee(bruto, flag):
    if bruto < SIXTYPERC_AVG_INCOME:
        return HEALTH_INS[0] * bruto if flag else SOCIAL_INS[0] * bruto
    res = (HEALTH_INS[0] if flag else SOCIAL_INS[0]) * SIXTYPERC_AVG_INCOME
    res += (HEALTH_INS[1] if flag else SOCIAL_INS[1]) * (bruto - SIXTYPERC_AVG_INCOME)
    return int(res)


def net_income(bruto):
    health_ins_fee = calc_ins_fee(bruto, True)
    social_ins_fee = calc_ins_fee(bruto, False)
    inc_tax = income_tax(bruto)
    print(inc_tax, health_ins_fee, social_ins_fee, bruto*(PENSION_RATE + HISHTALMUT_RATE))
    return int(bruto - inc_tax - health_ins_fee - social_ins_fee - bruto * (PENSION_RATE + HISHTALMUT_RATE))


def savings(bruto):
    return int(bruto * (PENSION_RATE + HISHTALMUT_RATE + EMPLOYER_HISHTALMUT + EMPLOYER_PENSION))
