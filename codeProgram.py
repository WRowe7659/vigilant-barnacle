# data cost is in cost per barrel

import pandas as pd
import matplotlib.pyplot as plot

data = pd.read_csv('myData.csv')
plot.figure(figsize = (30, 10)) #For some reason this line makes the graph blank
data.plot(x = "Year")
plot.savefig("graph.png")
#plot.pie(data)
#plot.savefig("graph2.png")

monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
data2 = [1816.74, 1849.61, 1900.14, 1941.87, 1953.37, 1982.09, 2003.45, 1984.25, 1980.59, 1974.14, 1851.12, 1790.98]
data3 = []
for x in data2:
    z = x / 51
    data3.append(z)
print(data3)
df = pd.DataFrame({'Month': monthList, 'Cost':data3})
ax = df.plot.bar(x='Month', y='Cost', rot=0, color= 'green')
plot.savefig("barGraph.png")