import numpy as np
import random 
import csv
from shapely.geometry import Polygon, Point

area = Polygon([
    (43.733941130636175, -79.60069161996111),
    (43.771382419750616, -79.5022462810324),
    (43.817972347333644, -79.42328204763396),
    (43.84224418360483, -79.34637775075896),
    (43.82193577031832, -79.2605470622824),
    (43.791212360523204, -79.23102130544646),
    (43.808062638807556, -79.17402972829802),
    (43.75650564795305, -79.18501605642302),
    (43.728725775715375, -79.21385516775115),
    (43.70280358334807, -79.24454827580176),
    (43.6686606637348, -79.29729090454012),
    (43.65226793474262, -79.33745966674715),
    (43.6332622672584, -79.42661360231627),
    (43.65748548015629, -79.46907564335413),
    (43.64469159081562, -79.47073057619322),
    (43.61449796009941, -79.48680506469637),
    (43.598960655940594, -79.4995080065909),
    (43.598665369197256, -79.50148516392164),
    (43.59481405781939, -79.50531005859375),
    (43.597173569547934, -79.5155613968318),
    (43.60447120506334, -79.52380114292555)
])

import random
import csv
from shapely.geometry import Point, Polygon


def generate_random_coordinates(area, n_points):
    min_x, min_y, max_x, max_y = area.bounds
    points = []
    
    while len(points) < n_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_point.within(area):
            points.append(random_point)
    
    return points

points = generate_random_coordinates(area, 250)

with open('datasets/coordinates.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for point in points:
        writer.writerow([point.x, point.y])