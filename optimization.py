import math
from pulp import *

# def compute_resources(time_skill_level,params):
# 	tot_mins = time_skill_level.sum(axis=0)
# 	n_resources = {}
# 	n_resources['low_skill'] = math.ceil(tot_mins['low_skill']/(60.0*params['WorkingHours_LowSkilled']))
# 	n_resources['high_skill'] = math.ceil(tot_mins['high_skill']/(60.0*params['WorkingHours_HighSkilled']))
# 	return n_resources

def compute_resources(time_skill_level,params):
	tot_mins = time_skill_level.sum(axis=0).to_dict()
	n_resources = {}
	prob = LpProblem("Capacity Calculation",LpMinimize)
	x1 = LpVariable("x1", 0)
	x2 = LpVariable("x2", 0)
	prob += x1 + x2
	prob += x1*params['WorkingHours_LowSkilled']*60 >= tot_mins['low_skill']
	prob += x2*params['WorkingHours_HighSkilled']*60 >= tot_mins['high_skill']
	prob.solve()
	n_resources['low_skill'] = math.ceil(value(x1))
	n_resources['high_skill'] = math.ceil(value(x2))
	return n_resources