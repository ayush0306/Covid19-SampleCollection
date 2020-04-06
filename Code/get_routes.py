import pandas as pd
import random
# import numpy as np

ward_input = "../Data/circle_coords.csv"
ambulances_input = ""
# df = pd.read_csv(ward_input)
# distance_matrix = pd.read_csv("../Data/circle_distance_matrix.csv")


class Planner:
	def __init__(self):
		self.n_doctors = 3
		self.wards = []
		self.ambulances = []

	def load_wards(self,ward_input):
		df = pd.read_csv(ward_input)
		self.n_wards = len(df)
		for row in df.iterrows():
			row = row[1]
			self.wards.append(Ward(row['ID'],row['Circle'],row['Longitude'],row['Latitude']))

	def load_ambulances(self,ambulances_input):
		df = pd.read_csv(ambulances_input)
		self.n_ambulances = len(df)
		for row in df.iterrows():
			row = row[1]
			self.ambulances.append(Ambulance(row[0]+1,row['Longitude'],row['Latitude']))

	def amb_to_ward(self):
		for amb in self.ambulances:
			amb.calc_dist(wards)

	def generate_demand(self,demand):
		for i in demand:
			rand = random.randint(0,n_wards-1)
			self.wards[rand].daily_cases += 1
			self.wards[rand].active_cases += 1
			self.wards[rand].total_cases += 1

	def increment_day(self):
		for i in range(n_wards):
			self.wards[i].daily_cases = 0

	# def allocate_wards(self):
	# 	for i in range(self.n_wards):






