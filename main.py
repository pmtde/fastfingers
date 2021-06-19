from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/aziziskandar/chrome-driver")

driver.get('https://10fastfingers.com/typing-test/english')
time.sleep(3)
driver.find_element_by_link_text('Allow all cookies').click()
time.sleep(2)

timer = driver.find_element_by_id('timer').text
while timer != '0:00':
    word = driver.find_element_by_xpath('//span[@class="highlight"]').text
    input_field = driver.find_element_by_id('inputfield')
    input_field.send_keys(word + ' ')
    time.sleep(0.05)

time.sleep(3)
driver.quit()