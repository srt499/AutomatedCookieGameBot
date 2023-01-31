from selenium import common
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "C:\python\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

five_min = time.time() + 5*60
time_out = time.time() + 5

while True:
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
    cookie.click()
    if time.time() > time_out:
        cursor = driver.find_element(By.ID, "buyCursor")
        cursor_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyCursor b').text.split('-')[1].replace(',', ''))

        grandma = driver.find_element(By.ID, "buyGrandma")
        grandma_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyGrandma b').text.split('-')[1].replace(',', ''))

        factory = driver.find_element(By.ID, "buyFactory")
        factory_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyFactory b').text.split('-')[1].replace(',', ''))

        mine = driver.find_element(By.ID, "buyMine")
        mine_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyMine b').text.split('-')[1].replace(',', ''))

        shipment = driver.find_element(By.ID, "buyShipment")
        shipment_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyShipment b').text.split('-')[1].replace(',', ''))

        alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
        alchemy_lab_cost = int(
            driver.find_element(By.CSS_SELECTOR, '#buyAlchemy\ lab > b').text.split('-')[1].replace(',', ''))

        portal = driver.find_element(By.ID, "buyPortal")
        portal_cost = int(driver.find_element(By.CSS_SELECTOR, '#buyPortal b').text.split('-')[1].replace(',', ''))

        time_machine = driver.find_element(By.ID, "buyTime machine")
        time_machine_cost = int(
            driver.find_element(By.CSS_SELECTOR, '#buyTime\ machine > b').text.split('-')[1].replace(',', ''))

        if money >= time_machine_cost:
            time_machine.click()
        elif money >= portal_cost:
            portal.click()
        elif money >= alchemy_lab_cost:
            alchemy_lab.click()
        elif money >= shipment_cost:
            shipment.click()
        elif money >= mine_cost:
            mine.click()
        elif money >= factory_cost:
            factory.click()
        elif money >= grandma_cost:
            grandma.click()
        elif money >= cursor_cost:
            cursor.click()

        time_out = time.time() + 5

        if time_out >= five_min:
            cookie_per_s = driver.find_element(By.ID, 'cps').text.split(":")
            print(cookie_per_s)
            break





