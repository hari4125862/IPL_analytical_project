import matplotlib.pyplot as plt
import csv
from matplotlib import style
from collections import Counter
from matplotlib.ticker import FuncFormatter
results=[]
runs=[]
with open('matches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['season']=='2015':
            results.append((row['id']))
with open('deliveries.csv') as csvfile:
    read = csv.DictReader(csvfile)
    for row in read:
        if row['match_id'] in results:
            runs.append((row['bowler'],row['total_runs']))

totalruns={}
for i in runs:
    if i[0] in totalruns:
        totalruns[i[0]] = [totalruns[i[0]][0]+int(i[1]),totalruns[i[0]][1]+1]
    else:
        totalruns[i[0]] = [int(i[1]), 1]
print(totalruns)
for i,j in totalruns.items():
    totalruns[i] = j[0]/(j[1]/6)
min=sorted(totalruns.items(), key=lambda kv:kv[1])[:5]
x,y = zip(*min)
plt.bar(x,y, width=0.4,color=['red','blue','green','yellow','black','gray'])
plt.xlabel('Bowler Name')
plt.ylabel('Economy rate')
plt.title('Economy of Bowlers in 2015')
plt.show()