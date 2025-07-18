from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot,dot2)
        dists.append([sum_dist,dot])
    return min(dists)[1]

with open('27A_19747.txt') as file:
    data = [list(map(float, i.split())) for i in file]

clusters = []
eps =0.26
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot,dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 7:
        clusters.append(cluster)


centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers)/ len(centers)
p_y = sum(center[1] for center in centers)/ len(centers)
print(abs(int(p_x *100_000)),abs(int(p_y*100_000)))