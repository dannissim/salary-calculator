import csv

import matplotlib.pyplot as plt
import numpy as np

from src.salary_calculator import (EMPLOYEE_EDUCATION_FUND_RATE, EMPLOYEE_PENSION_RATE,
                                   EMPLOYER_EDUCATION_FUND_RATE, EMPLOYER_PENSION_RATE,
                                   EMPLOYER_SEVERANCE_RATE, HEALTH_INSURANCE_BRACKETS,
                                   MAX_SALARY_TO_CALCULATE_INSURANCE_FEE, SOCIAL_INSURANCE_BRACKETS,
                                   calculate_income_tax, calculate_net_income, calculate_savings,
                                   calculate_sum_of_brackets, calculate_taxable_income)


def create_graph():
    x = np.arange(0.0, 50000.0, 500.0)
    y = [calculate_savings(i) for i in x]
    z = [calculate_net_income(i) for i in x]
    l = [int(y[i] + z[i]) for i in range(len(y))]
    plt.plot(x, y, label='Savings')
    plt.plot(x, z, label='Net Income')
    plt.plot(x, l, label='Total: Savings + Net')
    plt.legend(loc='upper left')
    plt.xlabel('Gross Salary')
    plt.ylabel('₪')
    plt.savefig('../static/graph.png')
    plt.show()


def create_table():
    with open('../static/results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        titles = ('Gross Salary', 'Overall Income', 'Net Income', 'Overall Savings',
                  'Taxable Income', 'Income Tax', 'Health Insurance', 'Social Insurance',
                  'Employee Pension', 'Employer Pension', 'Employee Education Fund',
                  'Employer Education Fund', 'Employer Severance')
        writer.writerow(titles)
        rewrite_titles_counter = 1
        for gross_salary in np.arange(1000, 51000, 1000):
            writer.writerow(_get_salary_details(gross_salary))
            if rewrite_titles_counter % 10 == 0 and gross_salary != 50000:
                writer.writerow(titles)
            rewrite_titles_counter += 1


def _get_salary_details(gross_salary: int) -> tuple:
    taxable_income = calculate_taxable_income(gross_salary)
    income_tax = calculate_income_tax(taxable_income)
    salary_to_calculate_insurance_fee = min(taxable_income, MAX_SALARY_TO_CALCULATE_INSURANCE_FEE)
    health_insurance_fee = calculate_sum_of_brackets(salary_to_calculate_insurance_fee,
                                                     HEALTH_INSURANCE_BRACKETS)
    social_insurance_fee = calculate_sum_of_brackets(salary_to_calculate_insurance_fee,
                                                     SOCIAL_INSURANCE_BRACKETS)
    employee_pension = EMPLOYEE_PENSION_RATE * gross_salary
    employer_pension = EMPLOYER_PENSION_RATE * gross_salary
    employee_education_fund = EMPLOYEE_EDUCATION_FUND_RATE * gross_salary
    employer_education_fund = EMPLOYER_EDUCATION_FUND_RATE * gross_salary
    employer_severance = EMPLOYER_SEVERANCE_RATE * gross_salary
    overall_savings = calculate_savings(gross_salary)
    net_income = calculate_net_income(gross_salary)
    overall_income = overall_savings + net_income
    results = (gross_salary, overall_income, net_income, overall_savings, taxable_income,
               income_tax, health_insurance_fee, social_insurance_fee, employee_pension,
               employer_pension, employee_education_fund, employer_education_fund,
               employer_severance)
    return tuple(int(value) for value in results)


if __name__ == '__main__':
    create_graph()
    create_table()
