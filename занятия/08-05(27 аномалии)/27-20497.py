from math import dist
import turtle as t


def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return max(dists)[1]

with open('27.19.B_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps = 5
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot,dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

#t.tracer(0)
#m = 50

#colors = ['red', 'green', 'blue']
#for cluster, color in zip(clusters,colors):
#    for dot in cluster:
#        t.goto(dot[0] * m, dot[1] * m)
#        t.dot(3,color)

#t.update()
#t.done()

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/len(centers)
p_y = sum(center[1] for center in centers)/len(centers)
print(int(p_x*10_000),int(p_y*10_000))




