import json
import os


def parse_tree(json_data):
    nodes = json_data["nodes"]
    return nodes

def adjacency_matrix(nodes):
    node_list = sorted(nodes.keys(), key=int)
    size = len(node_list)
    matrix = [[0] * size for _ in range(size)]
    for i, node in enumerate(node_list):
        for neighbor in nodes[node]:
            j = node_list.index(neighbor)
            matrix[i][j] = 1
            matrix[j][i] = 1
    return matrix


def edges_list(nodes):
    edges = []

    for node, neighbors in nodes.items():
        for neighbor in neighbors:
            edges.append((node, neighbor))
    return edges


def main(json_file_path):

    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Файл {json_file_path} не найден.")

    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    nodes = parse_tree(json_data)

    adj_matrix = adjacency_matrix(nodes)
    print("Матрица смежности:")
    for row in adj_matrix:
        print(row)

    edge_list = edges_list(nodes)
    print("\nСписок рёбер:")
    for edge in edge_list:
        print(edge)

    return nodes


if __name__ == "__main__":
    json_file = "tree.json"
    main(json_file)
