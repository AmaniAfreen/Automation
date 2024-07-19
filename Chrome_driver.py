import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\\Users\\amani\\Documents\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
#(Not able to execute using this code)driver = webdriver.Chrome(executable_path="C:\\Users\\amani\\Documents\\Drivers\\chromedriver.exe")
driver.get("https://www.amazon.in")
driver.maximize_window()

driver.get_screenshot_as_file("homepage.png")
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone14", Keys.ENTER)

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight):")
#driver.find_element(By.CLASS_NAME, "a-size-medium a-color-base a-text-normal").click()
time.sleep(10)
print(driver.title)
print(driver.current_url)
