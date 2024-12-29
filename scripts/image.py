import os
import requests
import csv

# Retrieve the Google Maps API key from environment variables
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
if not API_KEY:
    raise ValueError("Please set the GOOGLE_MAPS_API_KEY environment variable.")

def read_coordinates_file(file_path):
    coordinates = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                try:
                    lat, lng = map(float, row[:2])
                    coordinates.append((lat, lng))
                except ValueError:
                    print(f"Invalid coordinates: {row}")
    return coordinates

def download_static_map(lat, lng, index, save_dir='maps'):
    os.makedirs(save_dir, exist_ok=True)
    params = {
        'center': f'{lat},{lng}',
        'zoom': 18,
        'size': '1920x1080',
        'maptype': 'satellite',
        'key': API_KEY
    }
    url = "https://maps.googleapis.com/maps/api/staticmap"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        image_path = os.path.join(save_dir, f'map_{index}_{lat}_{lng}.png')
        with open(image_path, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Map image downloaded successfully: {image_path}")
    else:
        print(f"Failed to download image for ({lat}, {lng}): {response.status_code} - {response.text}")

def main():
    csv_file_path = os.path.join('datasets', 'coordinates.csv')  # Ensure this path is correct
    coordinates = read_coordinates_file(csv_file_path)
    print(f"Coordinates to process: {coordinates}")
    
    for index, (lat, lng) in enumerate(coordinates, start=1):
        print(f"Processing coordinates {index}: {lat}, {lng}")
        download_static_map(lat, lng, index)

if __name__ == "__main__":
    main()