# app that calculates your monthly salary and your savings after taking off by-law expenses: Pension savings,
# "Keren hishtalmut", Health insurance, income tax, social insurance.

PENSION_RATE = 0.07; # 7% off bruto, must be at least 6%
HEALTH_INS = [0.031, 0.05];
HISHTALMUT_RATE = 0.025; # 2.5% off bruto
EMPLOYER_HISHTALMUT = 0.075;
EMPLOYER_PENSION = 0.1483; # 6% by law, and 8.33% severance fees
SOCIAL_INS = [0.04, 0.07];
AVG_INCOME = 9907;
SIXTYPERC_AVG_INCOME = int(0.6 * AVG_INCOME); # social and health insurance fee blocks depend on 60% avg national income
INCOMETAX_THRESH = 4837;
TAX_BRACKET = [INCOMETAX_THRESH, 6240, 8950, 14360, 19960, 41530, 53490];
TAX_RATES =[1, 0.9, 0.86, 0.8, 0.69, 0.65, 0.53, 0.5];


def income_tax_deduction(bruto):
    arr = TAX_BRACKET + [bruto];
    arr.sort();
    j = arr.index(bruto);
    if j == 0:
        return bruto;
    sum = INCOMETAX_THRESH;
    for i in range(1, j):
        sum += (TAX_BRACKET[i] - TAX_BRACKET[i-1]) * TAX_RATES[i];
    sum += TAX_RATES[j]*(bruto - TAX_BRACKET[j-1]);
    return sum;


# calculates fee for health or social insurance, flag true for health ins., flag false for social ins.
def calc_ins_fee(bruto, flag):
    if bruto < SIXTYPERC_AVG_INCOME:
        return HEALTH_INS[0]*bruto if flag else SOCIAL_INS[0]*bruto;
    sum = HEALTH_INS[0] if flag else SOCIAL_INS[0];
    sum *= SIXTYPERC_AVG_INCOME;
    sum += HEALTH_INS[1]*(bruto-SIXTYPERC_AVG_INCOME) if flag else SOCIAL_INS[1]*(bruto-SIXTYPERC_AVG_INCOME);
    return sum;


brutoIncome = float(input("enter (bruto) salary "));
healthInsFee = calc_ins_fee(brutoIncome, True);
socialInsFee = calc_ins_fee(brutoIncome, False);
brutoAfterExpenses = brutoIncome - brutoIncome*(PENSION_RATE + HISHTALMUT_RATE) - healthInsFee - socialInsFee;
netIncome = income_tax_deduction(brutoAfterExpenses);
savings = brutoIncome*(PENSION_RATE + HISHTALMUT_RATE + EMPLOYER_HISHTALMUT + EMPLOYER_PENSION);
print("net income is: " + str(int(netIncome)) + "\nsavings are " + str(int(savings)));






