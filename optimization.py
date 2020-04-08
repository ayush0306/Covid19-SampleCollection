import math

def compute_resources(time_skill_level,params):
	tot_mins = time_skill_level.sum(axis=0)
	n_resources = {}
	n_resources['low_skill'] = math.ceil(tot_mins['low_skill']/(60.0*params['WorkingHours_LowSkilled']))
	n_resources['high_skill'] = math.ceil(tot_mins['high_skill']/(60.0*params['WorkingHours_HighSkilled']))
	return n_resources
