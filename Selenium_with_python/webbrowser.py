from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\rasis\AppData\chromedriver')
driver.get("https://Admin:PC135@cianlogic.com/")
print(driver.title)
driver.maximize_window()
driver.find_element_by_name("loginUsername").send_keys("byun@moon")
driver.find_element_by_name("loginPassword").send_keys("A12345")
driver.find_element_by_id("submit").click()


#
# driver.maximize_window()
#
#
# print(driver.current_url)
# driver.sleep()
#
# driver.close()
# driver.quit()