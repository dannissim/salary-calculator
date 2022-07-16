import typing

import pydantic


class Bracket(pydantic.BaseModel):
    threshold: int
    rate: float


# These are values that are constant for everyone and are updated by the government yearly

INCOME_TAX_BRACKETS = [
    Bracket(threshold=0, rate=0.1),
    Bracket(threshold=6450, rate=0.14),
    Bracket(threshold=9240, rate=0.2),
    Bracket(threshold=14840, rate=0.31),
    Bracket(threshold=20620, rate=0.35),
    Bracket(threshold=42910, rate=0.47),
    Bracket(threshold=55270, rate=0.5)
]
SIXTY_PERCENT_OF_AVG_INCOME = 6331
HEALTH_INSURANCE_BRACKETS = [
    Bracket(threshold=0, rate=0.031),
    Bracket(threshold=SIXTY_PERCENT_OF_AVG_INCOME, rate=0.05)
]
SOCIAL_INSURANCE_BRACKETS = [
    Bracket(threshold=0, rate=0.004),
    Bracket(threshold=SIXTY_PERCENT_OF_AVG_INCOME, rate=0.07)
]
DISCOUNT_POINT_WORTH = 223
MAX_SALARY_TO_CALCULATE_INSURANCE_FEE = 45075
MAX_NONTAXABLE_EMPLOYER_SEVERANCE = 2908
MAX_NONTAXABLE_EMPLOYER_PENSION = 1978
MAX_SALARY_WITHOUT_TAX_ON_EMPLOYER_EDUCATION_FUND = 15712
MAX_PENSION_DEPOSIT_TO_RECEIVE_TAX_DEDUCTION = 623.0

# These values may change from person to person

EMPLOYEE_PENSION_RATE = 0.07
EMPLOYER_PENSION_RATE = 0.07
DISCOUNT_POINTS = 2.25

# These values are constant for most people and aren't updated yearly

TAX_DEDUCTION_RATE_FROM_PENSION_DEPOSIT = 0.35
EMPLOYEE_EDUCATION_FUND_RATE = 0.025
EMPLOYER_EDUCATION_FUND_RATE = 0.075
EMPLOYER_SEVERANCE_RATE = 0.0833
DISCOUNT = DISCOUNT_POINTS * DISCOUNT_POINT_WORTH
MAX_NONTAXABLE_EMPLOYER_EDUCATION_FUND = EMPLOYER_EDUCATION_FUND_RATE * MAX_SALARY_WITHOUT_TAX_ON_EMPLOYER_EDUCATION_FUND


def main(gross_salary: int):
    net_income = calculate_net_income(gross_salary)
    savings = calculate_savings(gross_salary)
    return net_income, savings, net_income + savings


def calculate_net_income(gross_salary: int) -> int:
    gross_salary_with_additions = _calculate_gross_salary_with_additions(gross_salary)
    income_tax = _calculate_income_tax(gross_salary_with_additions)
    salary_to_calculate_insurance_fee = min(gross_salary_with_additions,
                                            MAX_SALARY_TO_CALCULATE_INSURANCE_FEE)
    health_insurance_fee = _calculate_sum_of_brackets(salary_to_calculate_insurance_fee,
                                                      HEALTH_INSURANCE_BRACKETS)
    social_insurance_fee = _calculate_sum_of_brackets(salary_to_calculate_insurance_fee,
                                                      SOCIAL_INSURANCE_BRACKETS)
    employee_deductions = gross_salary * (EMPLOYEE_PENSION_RATE + EMPLOYEE_EDUCATION_FUND_RATE)
    return int(gross_salary - income_tax - health_insurance_fee - social_insurance_fee -
               employee_deductions)


def calculate_savings(gross_salary: int) -> int:
    return int(gross_salary *
               (EMPLOYEE_PENSION_RATE + EMPLOYEE_EDUCATION_FUND_RATE +
                EMPLOYER_EDUCATION_FUND_RATE + EMPLOYER_PENSION_RATE + EMPLOYER_SEVERANCE_RATE))


def _calculate_income_tax(gross_salary_with_additions: float) -> float:
    income_tax_without_deductions = _calculate_sum_of_brackets(gross_salary_with_additions,
                                                               INCOME_TAX_BRACKETS)
    tax_deduction_from_pension_deposit = TAX_DEDUCTION_RATE_FROM_PENSION_DEPOSIT * min(
        MAX_PENSION_DEPOSIT_TO_RECEIVE_TAX_DEDUCTION,
        gross_salary_with_additions * EMPLOYEE_PENSION_RATE)
    income_tax = income_tax_without_deductions - tax_deduction_from_pension_deposit - DISCOUNT
    return max(income_tax, 0)


def _calculate_gross_salary_with_additions(gross_salary: float) -> float:
    employer_pension_to_be_taxed = max(
        0.0, gross_salary * EMPLOYEE_PENSION_RATE - MAX_NONTAXABLE_EMPLOYER_PENSION)
    severance_to_be_taxed = max(
        0.0, gross_salary * EMPLOYER_SEVERANCE_RATE - MAX_NONTAXABLE_EMPLOYER_SEVERANCE)
    employer_education_fund_to_be_taxed = max(
        0.0, gross_salary * EMPLOYER_EDUCATION_FUND_RATE - MAX_NONTAXABLE_EMPLOYER_EDUCATION_FUND)
    return gross_salary + employer_pension_to_be_taxed + severance_to_be_taxed + employer_education_fund_to_be_taxed


def _calculate_sum_of_brackets(number: float, brackets: typing.Iterable[Bracket]) -> float:
    relevant_brackets = [bracket for bracket in brackets if bracket.threshold < number]
    relevant_brackets.append(Bracket(threshold=number, rate=0))  # this rate isn't used
    result = 0
    for index, bracket in enumerate(relevant_brackets[:-1]):
        result += (relevant_brackets[index + 1].threshold - bracket.threshold) * bracket.rate
    return result


if __name__ == '__main__':
    gross_salary_from_user = int(input("enter gross salary \n"))
    print(main(gross_salary_from_user))
