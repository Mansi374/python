import csv
import math

points=[]
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)


with open("coordinates.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        points.append([float(cord) for cord in row])
    print(points)
min=float('inf')
for i in range(len(points)):
    for j in range(i+1,len(points)):
        dist=distance(points[i],points[j])
        if dist<min:
            min=dist
            closest_pair=(points[i],points[j])
print(dist)
