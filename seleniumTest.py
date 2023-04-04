from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
driver = webdriver.Chrome(chrome_options=option, executable_path="C:\Python\chromedriver.exe")

model = "text-davinci-002"
driver.get("https://chat.openai.com/")
driver.implicitly_wait(60)
search_box = driver.find_element(By.CLASS_NAME,'m-0')
search_box.send_keys("Selenium with Python")
search_box.submit()

driver.quit()