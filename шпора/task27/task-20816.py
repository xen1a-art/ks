from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

with open('27_B_20816.txt') as file:
    cluster_1 = []
    cluster_2 = []
    cluster_3 = []
    for i in file:
        x,y = map(float, i.split())
        if x < -5:
            cluster_1.append([x,y])
        elif y < -5:
            cluster_2.append([x,y])
        else:
            cluster_3.append([x,y])

clusters = [cluster_1,cluster_2,cluster_3]
centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/len(centers)
p_y = sum(center[1] for center in centers)/len(centers)
print(int(p_x*10_000),int(p_y*10_000))
# a 10592 6300
# b 15981 37287