from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

with open('27_A_21425.txt') as file:
    cluster_a1 = []
    cluster_a2 = []
    for line in file:
        x,y = map(float, line.split())
        if y < 15:
            cluster_a1.append([x,y])
        else:
            cluster_a2.append([x,y])

center_a1 = centroid(cluster_a1)
center_a2 = centroid(cluster_a2)
ans_x = (center_a1[0] + center_a2[0])/2
ans_y = (center_a1[1] + center_a2[1])/2
print(int(ans_x * 10_000),int(ans_y*10_000))