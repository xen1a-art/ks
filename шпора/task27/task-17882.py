#а
from math import dist
def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist+= dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

with open('27_A_17882 (3).txt') as file:
    cluster_1= []
    cluster_2=[]
    for i in file:
        x,y = map(float,i.split())
        if y < 3:
            cluster_1.append([x,y])
        else:
            cluster_2.append([x,y])
clusters= [cluster_1,cluster_2]
centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/len(centers)
p_y = sum(center[1] for center in centers)/len(centers)

print(int(p_x*10_000),int(p_y*10_000))
#=================================================================================================
#б
from math import dist


def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_B_17882 (1).txt') as file:
    cluster_B1 = []
    cluster_B2 = []
    cluster_B3 = []
    for i in file:
        x, y = map(float, i.split())
        if x > 5:
            cluster_B1.append([x, y])
        elif y > 4:
            cluster_B2.append([x, y])
        else:
            cluster_B3.append([x, y])

clusters = [cluster_B1, cluster_B2, cluster_B3]

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10_000), int(p_y * 10_000))