import json
import folium
import numpy as np
from folium.plugins import HeatMap
from PIL import Image
from io import BytesIO
import csv
# Step 1: Read the GeoJSON data from a file
def read_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Step 2: Extract coordinates from the features
def extract_coordinates(data):
    coordinates = []
    for feature in data['features']:
        coords = feature['geometry']['coordinates'][0]  # Extract first coordinate pair
        coordinates.append([coords[1], coords[0]])  # Folium expects [lat, lon] format
    return coordinates

# Step 3: Generate the heatmap centered on a specific point
def generate_heatmap(coordinates, lat, lng, zoom, output_file="heatmap.png"):
    # Create a map centered at the given latitude and longitude with "CartoDB Positron No Labels" tiles
    m = folium.Map(location=[lat, lng], zoom_start=zoom, tiles='CartoDB Positron', control_scale=False)
    
    # Add HeatMap layer
    HeatMap(coordinates, blur=15, radius=20).add_to(m)
    
    # Save as HTML first
    map_html = 'heatmap.html'
    m.save(map_html)

    # Convert to image if needed (via browser or use an external service)
    img_data = m._to_png(5)  # Export the map as PNG with scale factor
    img = Image.open(BytesIO(img_data))
    img = img.resize((1920, 1080))  # Resize to match requested size
    img.save(output_file)

# Step 4: Main logic to center the heatmap on a specific point
def main(file_path, lat, lng, zoom, output_file):
    data = read_data(file_path)
    coordinates = extract_coordinates(data)
    generate_heatmap(coordinates, lat, lng, zoom, output_file)

# Optional: Crop the image if needed
from PIL import Image

def crop(image):
    img = Image.open(image)
    width, height = img.size

    # Calculate the left, top, right, and bottom positions to crop
    left = (width - 900) / 2
    top = (height - 900) / 2
    right = (width + 900) / 2
    bottom = (height + 900) / 2

    # Crop the image to the new box
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(image)
    print(f"Image cropped successfully to 900x900 centered!")



# Example usage
if __name__ == "__main__":
    z = 0
    file_path = 'datasets/json.txt'  # Path to your file containing the data
    

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
            'center': (lat, lng),  # Example: lat, lng for Scarborough
            'zoom': 17,  # Close zoom level
            'size': '1920x1080',  # Size in pixels (handled via resize)
        }
    
        # Generate heatmap
        lat, lng = params['center']
        zoom = params['zoom']
        main(file_path, lat, lng, zoom, output_file)
        crop(output_file)
        z += 1