class Ward:
	def __init__(self,index,name,lon,lat):
		self.index = index
		# self.zone = zone
		self.name = name
		self.coord = (lon,lat)
		self.total_cases = 0
		self.daily_cases = 0
		self.active_cases = 0