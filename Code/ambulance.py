class Ambulance:
	def __init__(self,index,lon,lat,wards):
		self.index = index
		self.coord = (lon,lat)

	def calc_dist(wards):
		self.ward_distance = distance_matrix(self.coord,wards)

	def visit_wards(self, to_visit):
