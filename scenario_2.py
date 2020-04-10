import pandas as pd
import math

scenario_name = "pooled"

def collect_home_sample(load_val,time_val,params):
	transport_time = time_val*min(load_val,1)
	collection_time = load_val*params['Time_SampleCollection']
	within_time = load_val*params['Time_withinWard']
	return math.ceil(transport_time+collection_time+within_time)

def transport_patient(load_val,time_val,params):
	transport_time = time_val*load_val
	collection_time = 0
	# within_time = load_val*params['Time_withinWard']
	within_time = 0
	return math.ceil(transport_time+collection_time+within_time)

def collect_lab_sample(load1_val,load2_val,time_val,params):
	transport_time = 0
	collection_time = (load1_val+load2_val)*params['Time_SampleCollection']
	within_time = 0
	return math.ceil(transport_time+collection_time+within_time)

def compute_time_per_ward(params,load,time_to_lab_2way):
	load['time_home_sample'] = load.apply(lambda row: 
			collect_home_sample(row['Home Samples'],time_to_lab_2way[row.name],params),axis=1)
	load['time_pat_transport'] = load.apply(lambda row: 
			transport_patient(row['Patient Transport'],time_to_lab_2way[row.name],params),axis=1)
	load['time_lab_sample'] = load.apply(lambda row: 
			collect_lab_sample(row['Patient Transport'],row['Lab Sample'],time_to_lab_2way[row.name],params),axis=1)
	return load[['time_home_sample','time_pat_transport','time_lab_sample']]