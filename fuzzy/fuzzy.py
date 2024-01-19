import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import json
from enum import Enum
from functools import reduce

quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

quality.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# quality['average'].view()
# service.view()
# tip.view()
class Operator(Enum):
    OR = "or"
    AND = "and"
    NOT = "not"
    NONE = "none"

def build_terms(operator: str, terms: list) -> any:
    term_list = [ globals()[term["term_name"]][term["fuzzy_set"]] for term in terms]
    match Operator(operator):
        case Operator.OR:
            return reduce(lambda x, y: x | y, term_list)
        case Operator.AND:
            return reduce(lambda x, y: x & y, term_list)
        case Operator.NONE:
            return term_list[0]

rules_list = []
# if os.path.exists(config_route):
with open('data.json', 'r', encoding="utf8") as config_file:
    data = json.load(config_file)
for rule in data["rules"]:
    for antecedent in rule["antecedent"]:
        rule_ant = build_terms(operator=antecedent["operator"], terms=antecedent["terms"])
    
    for consequent in rule["consequent"]:
        rule_cons = build_terms(operator=consequent["operator"], terms=consequent["terms"])
    
    globals()[rule["rule"]] = ctrl.Rule(rule_ant, rule_cons)
    rules_list.append(globals()[rule["rule"]])


# rule1_ant = quality['poor'] | service['poor']
# rule2_ant = service['average']
# rule3_ant = service['good'] | quality['good']

# rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
# rule2 = ctrl.Rule(service['average'], tip['medium'])
# rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# rule1 = ctrl.Rule(rule1_ant, tip['low'])
# rule2 = ctrl.Rule(rule2_ant, tip['medium'])
# rule3 = ctrl.Rule(rule3_ant, tip['high'])

# rule1.view()
# rules_list.append(rule2)
# rules_list.append(rule3)

print(rules_list)

# tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_ctrl = ctrl.ControlSystem(rules_list)
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['quality'] = 6.5
tipping.input['service'] = 9.8

tipping.compute()

print(tipping.output['tip'])
# tip.view(sim=tipping)
# plt.show()