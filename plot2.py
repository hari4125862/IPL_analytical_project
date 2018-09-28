import matplotlib.pyplot as plt
import csv
from collections import Counter
from matplotlib.ticker import FuncFormatter
x=[]
s={}
season=[]
match=[]
element=0
count=0
tempElement=0
with open('matches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(row['winner'])
    sd=(Counter(x))
    temp=set(x)
#print(temp)
print(sd)
for i in sd:
    season.append(i)
    match.append(sd[i])
print(season)
print(match)
plt.bar(season,match, label='Loaded from file!')
plt.xlabel('Teams')
plt.xticks(x, rotation='vertical')
plt.subplots_adjust(bottom=0.35)
plt.ylabel('matches won')
plt.title('matches won of all teams')
plt.show()


