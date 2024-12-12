import numpy as np
import json


def fuzzy_membership(value, points):
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]

        if x1 <= value <= x2:
            return y1 + (value - x1) * (y2 - y1) / (x2 - x1)

    return 0 if value < points[0][0] or value > points[-1][0] else 1


def apply_rules(temp_value, temp_memberships, heating_rules, heating_memberships):

    activation_levels = []
    for rule in heating_rules:
        temp_term = rule[0]
        heating_term = rule[1]

        temp_membership_value = fuzzy_membership(temp_value, temp_memberships[temp_term])
        heating_membership_value = temp_membership_value * fuzzy_membership(temp_value,
                                                                            heating_memberships[heating_term])

        activation_levels.append(heating_membership_value)

    numerator = 0
    denominator = 0
    for i, rule in enumerate(heating_rules):
        heating_term = rule[1]
        term_points = heating_memberships[heating_term]

        heating_center = sum([x * y for x, y in term_points]) / len(term_points)
        numerator += activation_levels[i] * heating_center
        denominator += activation_levels[i]

    return numerator / denominator if denominator != 0 else 0


def task(temperature_file, heating_file, rules_file, current_temperature):

    with open(temperature_file, 'r', encoding='utf-8') as f:
        temperature_data = json.load(f)

    with open(heating_file, 'r', encoding='utf-8') as f:
        heating_data = json.load(f)

    with open(rules_file, 'r', encoding='utf-8') as f:
        rules = json.load(f)

    temp_memberships = {term["id"]: term["points"] for term in temperature_data["температура"]}
    heating_memberships = {term["id"]: term["points"] for term in heating_data["температура"]}

    optimal_heating = apply_rules(current_temperature, temp_memberships, rules, heating_memberships)

    return optimal_heating


# Пример
temperature_file = 'temperature.json'
heating_file = 'heating.json'
rules_file = 'rules.json'

current_temperature = 20
optimal_heating = task(temperature_file, heating_file, rules_file, current_temperature)
print(f"Оптимальный уровень нагрева: {optimal_heating}")
