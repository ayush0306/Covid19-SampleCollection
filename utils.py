import pandas as pd
import math

def compute_sample_load(params,population_density,totalLoad):
	load = pd.DataFrame(population_density['Pop_Density'],index=population_density.index)
	# load['Total Load'] = load.apply(lambda row: float(row['Pop_Density'])*totalLoad,axis=1)
	load['Home Samples'] = load.apply(lambda row: round(float(row['Pop_Density'])*math.ceil(totalLoad*params['Samples@Home'])),axis=1)
	load['Patient Transport'] = load.apply(lambda row: round(float(row['Pop_Density'])*math.ceil(totalLoad*params['PatientsFromHome'])),axis=1)
	load['Lab Sample'] = load.apply(lambda row: round(float(row['Pop_Density'])*math.ceil(totalLoad*params['PatientsVisitingLab'])),axis=1)
	load = load.drop(['Pop_Density'],axis=1)
	return load

def lab_dist(row,labs,time_matrix):
	return sum(row[lb]*time_matrix[row.name][lb] for lb in labs)

def compute_transportTime(params,distance_matrix,circle_to_lab):
	distance_matrix = distance_matrix.mul(2)
	time_matrix = distance_matrix.div(params["SpeedOfAmbulance"]*1000.0/60.0)
	labs = list(circle_to_lab.columns)
	circle_to_lab['time_to_lab'] = circle_to_lab.apply(lambda row: lab_dist(row,labs,time_matrix),axis=1)
	to_ret = circle_to_lab['time_to_lab']
	return to_ret


def compute_time_per_lab(time_ward,circle_to_lab):
	df = circle_to_lab.transpose()
	wards = list(df.columns)
	df['time_home_sample'] = df.apply(lambda row: sum(row[w]*time_ward['time_home_sample'][w] for w in wards),axis = 1)
	df['time_pat_transport'] = df.apply(lambda row: sum(row[w]*time_ward['time_pat_transport'][w] for w in wards),axis = 1)
	df['time_lab_sample'] = df.apply(lambda row: sum(row[w]*time_ward['time_lab_sample'][w] for w in wards),axis = 1)
	return df[['time_home_sample','time_pat_transport','time_lab_sample']]

def compute_time_skill(time_lab):
	time_skill_level = time_lab.copy()
	time_skill_level['low_skill'] = time_skill_level['time_home_sample'] + time_skill_level['time_pat_transport']
	time_skill_level['high_skill'] = time_skill_level['time_home_sample'] + time_skill_level['time_lab_sample']
	return time_skill_level[['low_skill','high_skill']]
