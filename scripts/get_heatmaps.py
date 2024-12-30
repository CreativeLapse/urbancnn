import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import helper_functions as hf

from PIL import Image


heat_maps = [
    {
        "name": "median_income",
        "mapID": "3348#17",
        "file_path": "maps/heat_maps/median_income/MI_map{index}.png"
    },

    {
        "name": "ethnic_diversity",
        "mapID": "3601#17",
        "file_path": "maps/heat_maps/ethnic_diversity/ED_map{index}.png"

    },
]


def read_coordinates_file(file_path):
    coordinates = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                lat, lng = map(float, row[:2])
                coordinates.append((round(lat, 6), round(lng, 6)))
    return coordinates

read_coordinates = read_coordinates_file("datasets/coordinates.csv")


# print(read_coordinates[0][1])


def crop(image):
    img = Image.open(image)
    width, height = img.size
    cropped_img = img.crop((360, 150, width-915, height-150))
    cropped_img.save(image)
    print(f"Image cropped successfully!")

def download_heatmap(latitude, longitude, type, index):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080") 

    chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)

    mapId = hf.get_map_id(heat_maps, type)
    file_path = hf.get_map_filepath(heat_maps, type, index)
    driver.get(f"https://censusmapper.ca/maps/{mapId}/{latitude}/{longitude}")
    time.sleep(5)

    driver.save_screenshot(file_path)
    print(f"Map image downloaded successfully!")
    crop(file_path)
    time.sleep(3)




def main():
    for i in range(250,1000):
     download_heatmap(read_coordinates[i][0], read_coordinates[i][1], "ethnic_diversity",i+1)
     download_heatmap(read_coordinates[i][0], read_coordinates[i][1], "median_income", i+1)

if __name__ == "__main__":
    main()