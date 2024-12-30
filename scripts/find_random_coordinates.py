import os
import numpy as np
import random 
import csv
from shapely.geometry import Polygon, Point

#http://apps.headwallphotonics.com/ to get polygon
#credits : https://aayush19.medium.com/a-quick-trick-to-create-random-lat-long-coordinates-in-python-within-a-defined-polygon-e8997f05123a

area = Polygon([
    #Polygon_1
    (43.629645497861794, -79.48378931864126),
    (43.712091581985526, -79.51949488504751),
    (43.7373986593588, -79.50095545633657),
    (43.77158964882741, -79.420166015625),
    (43.76368684270142, -79.37255274637563),
    (43.75773581238749, -79.33341395243032),
    (43.733429628720366, -79.33616053446157),
    (43.702660721748934, -79.31075465067251),
    (43.7041499035905, -79.2771090207897),
    (43.661942094195894, -79.30045496805532),
    (43.65312436249456, -79.3323839841686),
    (43.64104446159409, -79.37896728515625),
    (43.6361062062542, -79.4034517942272),
    (43.62765744785534, -79.41701304300649),
    (43.64306311546381, -79.45014368875844)
])

def generate_random_coordinates(area, n_points):
    min_x, min_y, max_x, max_y = area.bounds
    points = []
    
    while len(points) < n_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_point.within(area):
            points.append(random_point)
    
    return points

points = generate_random_coordinates(area, 1000)

def main():
    with open('datasets/coordinates.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for point in points:
            writer.writerow([point.x, point.y])

if __name__ == '__main__':
    main()