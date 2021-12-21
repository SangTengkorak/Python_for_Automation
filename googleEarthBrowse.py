from selenium import webdriver as wd
from selenium.webdriver.common.by import By as by
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec

url = 'https://www.google.co.id/intl/id/earth/'
driver = wd.Chrome('./chromedriver')
driver.get(url)
wait = wdw(driver, 10)

launchEarthButton = wait.until(ec.element_to_be_clickable(
    (by.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/div/a/span/span')))
launchEarthButton.click()
