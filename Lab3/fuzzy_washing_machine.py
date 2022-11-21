#!/usr/bin/env python3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import sys
from typing import List
from frules.rules import Rule as FuzzySet
from frules.expressions import Expression as MemFunction
from frules.expressions import ltrapezoid, trapezoid, rtrapezoid


# membership functions and corresponding fuzzy sets for how dirty (in tablespoons)
almost_clean_fn = MemFunction(ltrapezoid(0.25, 1.00), "almost_clean")
almost_clean_set = FuzzySet(value=almost_clean_fn)

dirty_fn = MemFunction(rtrapezoid(0.50, 1.0), "dirty")
dirty_set = FuzzySet(value=dirty_fn)

# membership functions and corresponding fuzzy sets for how delicate (in fabric weight)
very_delicate_fn = MemFunction(ltrapezoid(2.00, 4.00), "very_delicate")
very_delicate_set = FuzzySet(value=very_delicate_fn)

delicate_fn = MemFunction(trapezoid(3.00, 4.00, 6.00, 7.00), "delicate")
delicate_set = FuzzySet(value=delicate_fn)

not_delicate_fn = MemFunction(rtrapezoid(6.00, 7.00), "not_delicate")
not_delicate_set = FuzzySet(value=not_delicate_fn)

# dictionary with the output level for each of the rules; the key pertains to the rule number
rule_weights_dict = {1:10, 2:40, 3:60, 4:100}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TASK 1: 2 marks
# Implement the function that computes the degree to which a crisp input belongs to a fuzzy set
def fuzzify(fuzzy_set: FuzzySet, val: float) -> float:
	return fuzzy_set.eval(value = val)


# TASK 2a: 2 marks
# Implement the function for computing the conjunction of a rule's antecedents
def get_conjunction(fuzzified_dirt: float, fuzzified_fabric_weight: float) -> float:
	return min(fuzzified_dirt,fuzzified_fabric_weight)

# TASK 2b: 2 marks
# Implement the function for computing the disjunction of a rule's antecedents
def get_disjunction(fuzzified_dirt: float, fuzzified_fabric_weight: float) -> float:
	return max(fuzzified_dirt,fuzzified_fabric_weight)


# TASK 3: 3 marks
# Implement the function for computing the combined value of a rule antecedent
def get_rule_antecedent_value(ant1: FuzzySet, val1: float, ant2: FuzzySet, val2: float, operator: str) -> float:
	if operator == "OR":
		return get_disjunction(fuzzify(ant1,val1),fuzzify(ant2,val2))
	elif operator == "AND":
		return get_conjunction(fuzzify(ant1,val1),fuzzify(ant2,val2))
	elif operator == "":
		if(ant1 == None):
			return fuzzify(ant2,val2)
		elif(ant2 == None):
			return fuzzify(ant1,val1)
	else:
		return "Error Input!"


# TASK 4: 2 marks
# Implement function that returns the weighted output level of a rule
def get_rule_output_value(rule_number: int, rule_antecedent_value: float) -> float:
	return rule_weights_dict[rule_number] * rule_antecedent_value


# TASK 5: 3 marks
# dirt_amount can range from 0 to 2.5 inclusive
# fabric_weight range from 1.0 to 11.00 inclusive
# level = [[0,2.5],[1.0,11.00]]
def configure_washing_machine(dirt_amount: float, fabric_weight: float) -> tuple:
	all_antecedents = [0.0,1.0,2.0,3.0] # this should be set to a List containing the antecedent values for all rules
	all_outputs = [] # this should be set to a List containing the output values for all rules

	all_antecedents[0] = get_rule_antecedent_value(None,dirt_amount,very_delicate_set,fabric_weight,"") 
	all_antecedents[1] = get_rule_antecedent_value(almost_clean_set,dirt_amount,delicate_set,fabric_weight,"OR")
	all_antecedents[2] = get_rule_antecedent_value(dirty_set,dirt_amount,delicate_set,fabric_weight,"AND")
	all_antecedents[3] = get_rule_antecedent_value(dirty_set,dirt_amount,not_delicate_set,fabric_weight,"AND")

	n = 1
	for value in all_antecedents:
		all_outputs.append(get_rule_output_value(n,value))
		n += 1

	return (all_antecedents, all_outputs)


# TASK 6: 3 marks
# Implement function that computes the weighted average over all rules
def get_weighted_average(all_antecedents: List, all_outputs: List) -> float:
	weighted_average = 0
	antecedents = 0
	outputs = 0

	for i in all_antecedents:
		antecedents += i

	for i in all_outputs:
		outputs += i

	weighted_average = outputs / antecedents
	return weighted_average 


# TASK 7: 3 marks
# Implement function for computing the actual temperature the machine should be set to
temperature_range = [10, 90]
def get_temperature(all_antecedents: List, all_outputs: List) -> float:
    percentage = (temperature_range[1] - temperature_range[0]) * get_weighted_average(all_antecedents,all_outputs) / 100
    percentage = percentage + temperature_range[0]
    return percentage

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Debug
if __name__ == '__main__':
	if len(sys.argv) > 2:
		cmd = "{}({})".format(sys.argv[1], ",".join(sys.argv[2:]))
		print("debug run:", cmd)
		ret = eval(cmd)
		print("ret value:", ret)
	else:
		sys.stderr.write("Usage: fuzzy_washing_machine.py FUNCTION ARG...")
		sys.exit(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set noet ts=4 sw=4:
