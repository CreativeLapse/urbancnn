# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# def download_google_maps_image(top_left_lat, top_left_lng, bottom_right_lat, bottom_right_lng):
#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--window-size=1920x1080") 

#     # Set up the Chrome driver
#     chrome_driver_path = r'C:\Users\Gurshaan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
   
#     if not os.path.isfile(chrome_driver_path):
#         raise FileNotFoundError(f"ChromeDriver not found at: {chrome_driver_path}")
    
#     service = Service(chrome_driver_path)
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     try:
#         driver.get("https://www.google.com/maps")

#         # Wait for the map to load
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.NAME, "q"))
#         )
#         print("Map page loaded successfully.")

#         search_box = driver.find_element(By.NAME, "q")
#         search_box.clear()
#         search_box.send_keys(f"{top_left_lat},{top_left_lng}")
#         search_box.send_keys(Keys.RETURN)
#         time.sleep(3)  
#         print("Location searched successfully.")

#         # Click the layers button to open the layers menu
#         layers_button_xpath = "/html/body/div[1]/div[3]/div[8]/div[23]/div[5]/div/div[2]/button"
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, layers_button_xpath))
#         )
#         layers_button = driver.find_element(By.XPATH, layers_button_xpath)
#         layers_button.click()
#         time.sleep(2) 
#         print("Layers button clicked.")

#         driver.save_screenshot("map.png")
#         print("Map image downloaded successfully!")

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         driver.quit()

# # Example usage
# top_left_lat = 37.7749
# top_left_lng = -122.4194
# bottom_right_lat = 37.7397
# bottom_right_lng = -122.3552

# download_google_maps_image(top_left_lat, top_left_lng, bottom_right_lat, bottom_right_lng)

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
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080") 

    # Set up the Chrome driver
    chrome_driver_path = r'C:\Users\Gurshaan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
   
    if not os.path.isfile(chrome_driver_path):
        raise FileNotFoundError(f"ChromeDriver not found at: {chrome_driver_path}")
    
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.google.com/maps")

        # Wait for the map to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        print("Map page loaded successfully.")

        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(f"{top_left_lat},{top_left_lng}")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # Adjust sleep time as needed
        print("Location searched successfully.")

        # Click the layers button to open the layers menu
        layers_button_xpath = "/html/body/div[1]/div[3]/div[8]/div[23]/div[5]/div/div[2]/button"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, layers_button_xpath))
        )
        layers_button = driver.find_element(By.XPATH, layers_button_xpath)
        layers_button.click()
        time.sleep(2)  # Adjust sleep time as needed
        print("Layers button clicked.")

        # Click on the specific element within the layers menu
        specific_element_xpath_1 = "/html/body/div[1]/div[3]/div[8]/div[23]/div[7]/div/div/div/ul/li[5]/button"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, specific_element_xpath_1))
        )
        specific_element_1 = driver.find_element(By.XPATH, specific_element_xpath_1)
        specific_element_1.click()
        time.sleep(2)  # Adjust sleep time as needed
        print("First specific element clicked.")

        # Click on the second specific element within the layers menu
        specific_element_xpath_2 = "/html/body/div[1]/div[3]/div[8]/div[24]/div/div/div/div[4]/ul/li[2]/button"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, specific_element_xpath_2))
        )
        specific_element_2 = driver.find_element(By.XPATH, specific_element_xpath_2)
        specific_element_2.click()
        time.sleep(2)  # Adjust sleep time as needed
        print("Second specific element clicked.")

        driver.save_screenshot("map.png")
        print("Map image downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()

# Example usage ,
top_left_lat = 43.7476484
top_left_lng = -79.7426587
bottom_right_lat = 37.7397
bottom_right_lng = -122.3552

download_google_maps_image(top_left_lat, top_left_lng, bottom_right_lat, bottom_right_lng)