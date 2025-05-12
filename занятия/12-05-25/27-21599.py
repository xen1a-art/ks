from math import dist

with open('27_A_21599.txt') as file:
    cluster_a1 =[]
    cluster_a2 =[]
    cluster_a3 =[]
    for i in file:
        x,y = map(float, i.split())
        if y < -7:
            cluster_a1.append([x,y])
        elif y > x - 10:
            cluster_a2.append([x,y])
        else:
            cluster_a3.append([x,y])

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

clusters = [cluster_a1,cluster_a2,cluster_a3]
centers = [centroid(cluster) for cluster in clusters]
p_x= sum(center[0] for center in centers)/ len(centers)
p_y= sum(center[1] for center in centers)/ len(centers)
print(abs(int(p_x * 10_000)),abs(int(p_y *10_000)))