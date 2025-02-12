# data cost is in cost per barrel

import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv('myData.csv')
plot.figure(figsize = (30, 10)) #For some reason this line makes the graph blank
data.plot(x = "Year")
plot.savefig("graph.png")