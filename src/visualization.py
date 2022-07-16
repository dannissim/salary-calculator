import csv

import matplotlib.pyplot as plt
import numpy as np

from src.salary_calculator import calculate_net_income, calculate_savings


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
    plt.savefig("graph.png")
    plt.show()


def create_table():
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # for salary in
        # writer.writerow(['Spam'] * 5 + ['Baked Beans'])
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


if __name__ == '__main__':
    create_graph()
