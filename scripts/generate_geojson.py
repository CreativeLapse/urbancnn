import json
import folium
import numpy as np
from folium.plugins import HeatMap
from PIL import Image
from io import BytesIO
import csv
from PIL import Image

def read_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def extract_coordinates(data):
    coordinates = []
    for feature in data['features']:
        coords = feature['geometry']['coordinates'][0] 
        coordinates.append([coords[1], coords[0]])  
    return coordinates

def generate_heatmap(coordinates, lat, lng, zoom, output_file="heatmap.png"):
    #create folium map
    m = folium.Map(location=[lat, lng], zoom_start=zoom, tiles='CartoDB Positron', control_scale=False)
    
    #save heat map
    HeatMap(coordinates, blur=15, radius=20).add_to(m)
    
    map_html = 'heatmap.html'
    m.save(map_html)

    img_data = m._to_png(5)  
    img = Image.open(BytesIO(img_data))
    img = img.resize((1920, 1080))  
    img.save(output_file)

def main(file_path, lat, lng, zoom, output_file):
    data = read_data(file_path)
    coordinates = extract_coordinates(data)
    generate_heatmap(coordinates, lat, lng, zoom, output_file)


def crop(image):
    img = Image.open(image)
    width, height = img.size

    left = (width - 900) / 2
    top = (height - 900) / 2
    right = (width + 900) / 2
    bottom = (height + 900) / 2

    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(image)
    print(f"Image cropped successfully to 900x900 centered!")



if __name__ == "__main__":
    z = 0
    file_path = 'datasets/json.txt' 
    

    def read_coordinates_file(file_path):
        coordinates = []
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    lat, lng = map(float, row[:2])
                    coordinates.append((lat, lng))
        return coordinates
    coordinates = read_coordinates_file("datasets/coordinates.csv")
   
    for index, (lat, lng) in enumerate(coordinates, start=1):
        output_file = f'maps/geojson/GM_map{z+1}.png'
        params = {
            'center': (lat, lng), 
            'zoom': 17,  
            'size': '1920x1080',  
        }
    
        lat, lng = params['center']
        zoom = params['zoom']
        main(file_path, lat, lng, zoom, output_file)
        crop(output_file)
        z += 1