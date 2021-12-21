from selenium import webdriver as wd
from selenium.webdriver.common.action_chains import ActionChains as ac
driver = wd.Chrome('./chromedriver')
driver.maximize_window()

driver.get(
    'http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element_by_xpath('//*[@id="box3"]')
dest = driver.find_element_by_xpath('//*[@id="box103"]')
actions = ac(driver)
actions.drag_and_drop(source, dest).perform()
