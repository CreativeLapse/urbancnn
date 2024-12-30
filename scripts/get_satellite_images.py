import os
import requests
import csv

# Retrieve the Google Maps API key from environment variables
API_KEY = "AIzaSyBR9R06eZuZHKXCoP6sDamTtUjpBKMauWY"
# or in the terminal $env:GOOGLE_MAPS_API_KEY= "enter your api key"

def read_coordinates_file(file_path):
    coordinates = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                lat, lng = map(float, row[:2])
                coordinates.append((lat, lng))
    return coordinates

def download_static_map(lat, lng, index, save_dir='maps\satellite'):
    os.makedirs(save_dir, exist_ok=True)
    params = {
        'center': f'{lat},{lng}',
        'zoom': 17,
        'size': '1920x1080',
        'maptype': 'satellite',
        'key': API_KEY
    }

    url = "https://maps.googleapis.com/maps/api/staticmap"
    response = requests.get(url, params=params)

    if response.status_code == 200: #sucess 
        image_path = os.path.join(save_dir, f'SM_map{index}.png')
        with open(image_path, 'wb') as img_file:
            img_file.write(response.content)
        print(f"Map image downloaded successfully: {image_path}")

def main():
    coordinates = read_coordinates_file("datasets/coordinates.csv")
    print(f"Coordinates to process: {coordinates}")
    #iteraete over all coordinates 
    
    for index, (lat, lng) in enumerate(coordinates, start=1):
        download_static_map(lat, lng, index)

if __name__ == "__main__":
    main()