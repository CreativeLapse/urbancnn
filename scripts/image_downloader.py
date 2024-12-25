from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def download_google_maps_image(top_left_lat, top_left_lng, bottom_right_lat, bottom_right_lng):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size

    # Set up the Chrome driver
    chrome_driver_path = r'C:\Users\Gurshaan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
   
    if not os.path.isfile(chrome_driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at: {chrome_driver_path}")
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open Google Maps
        driver.get("https://www.google.com/maps")

        # Wait for the map to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        print("Map page loaded successfully.")

        # Search for the top-left location
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(f"{top_left_lat},{top_left_lng}")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Additional wait time to ensure the map loads
        print("Location searched successfully.")

        # Click the layers button to open the layers menu
        layers_button_xpath = "/html/body/div[1]/div[3]/div[8]/div[23]/div[5]/div/div[2]/button"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, layers_button_xpath))
        )
        layers_button = driver.find_element(By.XPATH, layers_button_xpath)
        layers_button.click()
        time.sleep(2)  # Wait for the layers menu to appear
        print("Layers button clicked.")

        # Take a screenshot of the map
        driver.save_screenshot("map.png")
        print("Map image downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# Example usage
top_left_lat = 37.7749
top_left_lng = -122.4194
bottom_right_lat = 37.7397
bottom_right_lng = -122.3552

download_google_maps_image(top_left_lat, top_left_lng, bottom_right_lat, bottom_right_lng)