import numpy as np
import pandas as pd
from utils import *
from scenario_2 import *
from optimization import *
from plots import *

input_file = "Data/parameters.xlsx"

params = pd.read_excel(input_file,sheet_name="parameters")
distance_matrix = pd.read_excel(input_file,sheet_name="distance_matrix")
circle_to_lab = pd.read_excel(input_file,sheet_name="circle_activations")
population_density = pd.read_excel(input_file,sheet_name="pop_density")
params = dict(zip(params.Parameter, params.Value))
totalLoad = 450

#-------------------------------------------------#

n_fte = []
for totalLoad in range(200,5200,200):
	load = compute_sample_load(params,population_density,totalLoad)
	time_to_lab_2way = compute_transportTime(params,distance_matrix,circle_to_lab)
	circle_to_lab = circle_to_lab.drop(['time_to_lab'],axis=1)
	time_ward = compute_time_per_ward(params,load,time_to_lab_2way)
	time_lab = compute_time_per_lab(time_ward,circle_to_lab)
	time_skill_level = compute_time_skill(time_lab)
	n_resources = compute_resources(time_skill_level,params)
	n_fte.append([totalLoad,n_resources['low_skill'],n_resources['high_skill']])

index = [i for i in range(200,5200,200)]
columns = ['Demand','Low_Skill_FTE','High_Skill_FTE']
req_resources = pd.DataFrame(n_fte,index=index,columns=columns)
req_resources['Total_Skill_FTE'] = req_resources['Low_Skill_FTE']+req_resources['High_Skill_FTE']

myPlot(req_resources[['Low_Skill_FTE','High_Skill_FTE']],'Skill-Wise Resource Requirement',scenario_name+'.png')
req_resources.to_excel("Output_Sheets/"+scenario_name+".xlsx")

print(load)
print(time_to_lab_2way)
print(time_ward)
print(time_lab)
print(time_skill_level)
print(n_resources)
print(req_resources)