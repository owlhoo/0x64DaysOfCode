from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:8000/polls/')
link = driver.find_elements_by_tag_name('a')
link[0].click()
driver.save_screenshot('./kek.png')

driver.get('https://www.youtube.com')
input_field_container = driver.find_element_by_id('search-form')
input_field = input_field_container.find_element_by_id('search')
# input_field.click()
input_field.send_keys('This is hello world from selenium py app :)')

button = driver.find_element_by_id('search-icon-legacy')
sleep(2)
button.click()

sleep(2)
driver.close()
driver.quit()
