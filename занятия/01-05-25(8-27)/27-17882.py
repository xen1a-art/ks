#a
from math import dist

def centroid(cluster):
    dists = []# все дистанции
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

with open('27_A_17882.txt') as file:
    cluster_a1 = []
    cluster_a2 = []
    for line in file:
        x,y = map(float,line.split())
        if y < 3:
            cluster_a1.append([x,y])
        else:
            cluster_a2.append([x,y])

center_a1 = centroid(cluster_a1)
center_a2 = centroid(cluster_a2)

ans_x = (center_a1[0] + center_a2[0])/2
ans_y = (center_a1[1] + center_a2[1])/2
print(int(ans_x*10_000),int(ans_y*10_000))

#b
with open('27_B_17882.txt') as file:
    cluster_b1 = []
    cluster_b2 = []
    cluster_b3 = []
    for line in file:
        x,y = map(float, line.split())
        if x<3 and y < 4:
            cluster_b1.append([x,y])
        elif x < 5:
            cluster_b2.append([x,y])
        else:
            cluster_b3.append([x,y])

center_b1 = centroid(cluster_b1)
center_b2 = centroid(cluster_b2)
center_b3 = centroid(cluster_b3)

ans_x = (center_b1[0] + center_b2[0] + center_b3[0])/3
ans_y = (center_b1[1] + center_b2[1] + center_b3[1])/3

print(int(ans_x * 10_000), int(ans_y* 10_000))