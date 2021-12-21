from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

driver = wd.Chrome("./chromedriver")
driver.get("https://www.google.com")

print(driver.title)

searchField = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchField.send_keys('roti sobek')

searchField.submit()
