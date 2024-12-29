# import required modules
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
 
 
# assign url in the webdriver object
driver = webdriver.Chrome()
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)
 
 
# search locations
def searchplace():
    Place = driver.find_element(By.CLASS_NAME, "tactile-searchbox-input")
    Place.send_keys("Tiruchirappalli")
    Submit = driver.find_element(
        By.XPATH, "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()
 
 
searchplace()
 
 
# get directions
def directions():
    sleep(10)
    directions = driver.find_element(
        By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button")
    directions.click()
 
 
directions()
 
 
# find place
def find():
    sleep(6)
    find = driver.find_element(
        By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
    find.send_keys("Tirunelveli")
    sleep(2)
    search = driver.find_element(
        By.XPATH,"/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
 
 
find()
 
 
# get transportation details
def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element(
        By.XPATH,"/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)
    Bus = driver.find_element(
        By.XPATH, "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
    print("Bus Travel:", Bus.text)
    sleep(7)
    Train = driver.find_element(
        By.XPATH, "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div")
    print("Train Travel:", Train.text)
    sleep(7)
 
 
kilometers()