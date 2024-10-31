import numpy as np
from collections import Counter
from math import log2
import csv

def calculate_entropy(probabilities):
    return -sum(p * log2(p) for p in probabilities if p > 0)

def task():
    filename = 'test.csv'
    categories = []
    probabilities = []

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for row in reader:
            category_data = list(map(int, row[1:]))
            total = sum(category_data)
            category_probabilities = [x / total for x in category_data]
            probabilities.append(category_probabilities)
            categories.append(row[0])

    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    sums = [x + y for x, y in outcomes]
    products = [x * y for x, y in outcomes]

    sum_counts = Counter(sums)
    total_outcomes = len(outcomes)
    P_A = {k: v / total_outcomes for k, v in sum_counts.items()}

    product_counts = Counter(products)
    P_B = {k: v / total_outcomes for k, v in product_counts.items()}

    joint_counts = Counter((x + y, x * y) for x, y in outcomes)
    P_AB = {k: v / total_outcomes for k, v in joint_counts.items()}

    H_A = calculate_entropy(P_A.values())
    H_B = calculate_entropy(P_B.values())
    H_AB = calculate_entropy(P_AB.values())

    H_B_given_A = H_AB - H_A

    I_A_B = H_B - H_B_given_A

    results = [round(H_AB, 2), round(H_A, 2), round(H_B, 2), round(H_B_given_A, 2), round(I_A_B, 2)]

    print("Результаты:")
    print(f"H(AB): {results[0]}")
    print(f"H(A): {results[1]}")
    print(f"H(B): {results[2]}")
    print(f"H(B|A): {results[3]}")
    print(f"I(A,B): {results[4]}")

    return results

# Тестирование
task()
