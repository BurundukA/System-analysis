import json


def parse_tree(json_data):
    nodes = json_data["nodes"]
    return nodes


def compute_relation_matrix(nodes):
    node_list = list(nodes.keys())
    n = len(node_list)

    relation_matrix = [[0] * 5 for _ in range(n)]

    predecessors = {node: [] for node in node_list}
    for parent, children in nodes.items():
        for child in children:
            predecessors[child].append(parent)

    for i, node in enumerate(node_list):
        r1 = len(nodes[node])
        r2 = len(predecessors[node])
        descendants = get_descendants(nodes, node)
        r3 = len(descendants) - r1
        ancestors = get_ancestors(predecessors, node)
        r4 = len(ancestors) - r2
        r5 = 0
        for pred in predecessors[node]:
            siblings = set(nodes[pred]) - {node}
            r5 += len(siblings)

        relation_matrix[i] = [r1, r2, r3, r4, r5]

    return relation_matrix


def get_descendants(nodes, node):
    descendants = set(nodes[node])
    for child in nodes[node]:
        descendants.update(get_descendants(nodes, child))
    return descendants

def get_ancestors(predecessors, node):
    ancestors = set(predecessors[node])
    for parent in predecessors[node]:
        ancestors.update(get_ancestors(predecessors, parent))
    return ancestors


def main(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    nodes = parse_tree(json_data)

    relation_matrix = compute_relation_matrix(nodes)

    print("Матрица отношений (r1, r2, r3, r4, r5):")
    for row in relation_matrix:
        print(row)

    return relation_matrix


if __name__ == "__main__":
    # Укажите путь к файлу JSON
    json_file_path = "tree.json"
    main(json_file_path)
