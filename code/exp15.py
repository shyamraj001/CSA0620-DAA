import math

def closest_pair(points):
    min_dist = float('inf')
    pair = ()

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 +
                             (points[i][1] - points[j][1]) ** 2)

            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])

    return pair, min_dist

points = [(1, 2), (4, 5), (7, 8), (3, 1)]

pair, distance = closest_pair(points)

print("Closest Pair:", pair)
print("Distance:", distance)
