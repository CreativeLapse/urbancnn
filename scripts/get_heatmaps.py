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
from PIL import Image
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") 

chrome_driver_path = r'D:\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

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
print(read_coordinates[0][1] )
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.set_window_size(1920, 1080)


def crop(image):
    img = Image.open(image)
    width, height = img.size
    cropped_img = img.crop((360, 150, width-900, height-150))
    cropped_img.save(image)
    print(f"Image cropped successfully!")

def download_heatmap(latitude, longitude):
    driver.get(f"https://censusmapper.ca/maps/3348#17/{latitude}/{longitude}")
    driver.save_screenshot(f"map{latitude}_{longitude}.png")
    print(f"Map image  downloaded successfully!")
    driver.quit

def main():
    download_heatmap(read_coordinates[1][0], read_coordinates[1][1])
    
    crop(f"map{read_coordinates[1][0]}_{read_coordinates[1][1]}.png")
if __name__ == "__main__":
    main()