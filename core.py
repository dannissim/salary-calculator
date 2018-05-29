# app that calculates your monthly salary and your savings after taking off law ordered expenses: Pension savings,
# "Keren hishtalmut", Health insurance, income tax, social insurance.

PENSION_RATE = 0.05; #5% off bruto
HEALTH_INS = 0.05;
HISHTALMUT_RATE = 0.025; #2.5% off bruto
EMPLOYER_HISHTALMUT = 0.075;
EMPLOYER_PENSION = 0.05;
SOCIAL_INS = 0.05;
INCOMETAX_THRESH = 4837;
TAX_BRACKET = [INCOMETAX_THRESH, 6240, 8950, 14360, 19960, 41530, 53490];
TAX_RATES =[1, 0.9, 0.86, 0.8, 0.69, 0.65, 0.53, 0.5];

def incomeTaxDeduction(bruto):
    arr = TAX_BRACKET + [bruto];
    arr.sort();
    j = arr.index(bruto);
    if j==0:
        return bruto;
    sum = INCOMETAX_THRESH;
    for i in range(1, j):
        sum += (TAX_BRACKET[i] - TAX_BRACKET[i-1]) * TAX_RATES[i];
    sum += TAX_RATES[j]*(bruto - TAX_BRACKET[j-1]);
    return sum;

brutoIncome = (float)(input("enter (bruto) salary "));
brutoAfterExpenses = brutoIncome - brutoIncome*(PENSION_RATE + HEALTH_INS + SOCIAL_INS + HISHTALMUT_RATE);
netIncome = incomeTaxDeduction(brutoAfterExpenses);
savings = brutoIncome*(PENSION_RATE + HISHTALMUT_RATE + EMPLOYER_HISHTALMUT +EMPLOYER_PENSION);
print("net income is: " + str(netIncome) + "\nsavings are " + str(savings));






