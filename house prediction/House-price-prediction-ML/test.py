from selenium import webdriver

driver1=webdriver.Chrome(executable_path='/usr/bin/chromedriver')
driver1.get("http://127.0.0.1:8000/")

driver1.find_element_by_id('loginm').click()

driver1.find_element_by_id('username').send_keys('sit')
driver1.find_element_by_id('loginpass').send_keys('sit')
driver1.find_element_by_id('lsubmit').click()



