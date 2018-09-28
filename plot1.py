import matplotlib.pyplot as plt
import csv
from collections import Counter
x = []
y = []
s={}
season=[]
match=[]
final=[]
next1=[]
element=0
count=0
tempElement=0
with open('matches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x.append(row['season'])
    s=(Counter(x))
    print(s)
    for i in s:
        season.append(s[i])
        match.append(i)
    print(season)
    print(match)
plt.bar(match,season, label='Loaded from file!',color=['red','blue','green','yellow','black','gray'])
plt.xlabel('year')
plt.ylabel('no of matches')
plt.title('NUmber of matches played')
plt.legend()
plt.show()