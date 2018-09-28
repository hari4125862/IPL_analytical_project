import matplotlib.pyplot as plt
import csv
from matplotlib import style
from collections import Counter
from matplotlib.ticker import FuncFormatter
row=[]
row1=[]
runs=[]
teams=[]
xruns=[]
matches=[]
result={}
with open('matches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        ele=0
        ele=int(i['id'])
        if int(i['season'])==2016:
            row.append(ele)

with open('deliveries.csv') as csvfile:
    reader1 = csv.DictReader(csvfile)
    for i in reader1:
        ele1=0
        ele1=int(i['match_id'])
        if ele1 in row:
           runs.append((i['bowling_team'],int(i['extra_runs'])))
    extraruns={}

    for i in runs:
        if i[0] in extraruns:
            extraruns[i[0]]+=int(i[1])
        else:
            extraruns[i[0]]=int(i[1])

x, y=zip(*extraruns.items())
print(x)
print(y)
plt.bar(x,y,color=['red','blue','green','yellow','black','gray'])
plt.subplots_adjust(bottom=0.35)
plt.xticks(x, rotation='vertical')
plt.xlabel('Team Name')
plt.ylabel('Extra runs')
plt.title('extra run conceeded in 2016')

plt.show()