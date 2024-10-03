import csv
import math

def read_csv(file_path):
    nodes = []
    relation_matrix = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            nodes.append(row[0])
            relation_matrix.append([int(x) for x in row[1:]])

    return nodes, relation_matrix

def compute_probabilities_and_entropy(nodes, relation_matrix):
    n = len(nodes)
    h = 0

    for i, row in enumerate(relation_matrix):
        Hi = 0
        for j, lij in enumerate(row):
            if lij > 0:
                Pij = lij / (n - 1)
                Hi -= Pij * math.log2(Pij)
        h += Hi

    return h

def main(csv_file_path):
    nodes, relation_matrix = read_csv(csv_file_path)

    total_entropy = compute_probabilities_and_entropy(nodes, relation_matrix)

    print(f"Общая энтропия h: {total_entropy:.4f}")
    return total_entropy

if __name__ == "__main__":
    csv_file_path = "relation_matrix.csv"
    main(csv_file_path)
