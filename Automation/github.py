import sys
from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://github.com/login')
driver.maximize_window()

email = input('Enter your email:')
password = input('Enter your password:')

driver.find_element_by_xpath("//*[@id='login_field']").send_keys(email)
driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

driver.find_element_by_xpath("//*[@id='login']/form/div[4]/input[9]").click()

driver.get('https://github.com/new')

driver.find_element_by_xpath("//*[@id='repository_name']").send_keys('test-repo')
driver.find_element_by_xpath("//*[@id='repository_description']").send_keys('Automation Test')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button").click()
