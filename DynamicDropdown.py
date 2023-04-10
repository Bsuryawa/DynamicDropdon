import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service (r"C:\Users\BHAGYASHRI\Downloads\chromedriver_win32 (1)\chromedriver")
driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)
countires = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countires))
for country in countires:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"