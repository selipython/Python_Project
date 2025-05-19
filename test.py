import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options)
# driver.get("https://www.facebook.com/")
driver.get("https://www.w3schools.com/html/html_iframe.asp")
time.sleep(20)
driver.maximize_window()
# wait=WebDriverWait(driver,10)
# ele=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@name='submit']")))
# ele.click()

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("hello")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("hello")
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("hhhhhh")
# driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]").send_keys("hari1234@gmail.com")
# parent=driver.current_window_handle
# # print(driver.current_window_handle)
# driver.switch_to.new_window('window1')
# driver.get("https://www.amezon.com/")
# win=driver.window_handles
# for wins in win:
#     if wins!=parent:
#         driver.switch_to.window(wins)
#
# driver.find_element(By.CSS_SELECTOR,"input#captchacharacters").send_keys("ddffdf")
# driver.switch_to.window(parent)
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("hello")
# driver.close()
# driver.quit()

# ele=driver.find_element(By.XPATH,"//*[@id='main']/div[3]/iframe")
# driver.switch_to.frame(ele)
# driver.find_element(By.CLASS_NAME,"w3-right w3-btn").click()


#
#
# driver.implicitly_wait(10)
# try:
#     expect=driver.find_element(By.XPATH,"//h3[text()='Results12']").is_displayed()
#     if expect:
#         print("Yes")
#     # else:
#     #     print("No")
# except NoSuchElementException:
#     print("NoNoSuchElementException")
#
# # assert "Results" in expect
# # driver.forward()
# v=driver.current_url
# print(v)
# l=[]
# l=driver.find_elements(By.XPATH,"//iframe | //frame")
# driver.find_element(By.TAG_NAME)
#
# print(len(l))
# driver.close()
# # a=driver.switch_to.alert
# # a.accept()
# # a.dismiss()
# #
# # act=ActionChains(driver)
# # act.context_click(on_element=ele)
# # act.perform()
# #
# # driver.execute_script("w")
# # driver.close()
#
# # print(driver.title)
# # driver.close()
# # driver.quit()
# # v=driver.current_url
#
#
# print(driver.current_window_handle)
# driver.page_source
# driver.current_url
# driver.title
# driver.maximize_window()
# driver.switch_to.