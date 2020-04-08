import matplotlib.pyplot as plt

def myPlot(df,title,filename):
	df.plot()
	plt.title(title)
	plt.xlabel("Demand")
	plt.ylabel("Required Capacity")
	plt.savefig("Plots/"+filename+".png")
	plt.close()
