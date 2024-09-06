from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
from webdriver_manager.microsoft import EdgeChromiumDriverManager #自动更新驱动
#from selenium.webdriver.edge.options import Options
#from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import EdgeOptions#设置edge的无界面模式
from msedge.selenium_tools import Edge
import time

global driver
edge_options = EdgeOptions()
#edge_options.use_chromium = True
#edge_options.add_argument("--headless")
#edge_options.add_argument("--disable-gpu")
driver = Edge(EdgeChromiumDriverManager().install(),options=edge_options)
driver.get(r"https://tools.1001genomes.org/pseudogenomes/#select_strains")
wait1 = WebDriverWait(driver, 20)
time.sleep(2)
all_choice_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div/table/thead/tr/th[1]/input")))    #变量
driver.execute_script("arguments[0].click();", all_choice_element)

next_element = driver.find_element_by_xpath( "/html/body/div/div[1]/div/div/div/p/button")   #变量
next_element.click()

input_element  = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/input")))  
input_element.clear()
input_element.send_keys("Chr1:10000..10300")

first_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-selectable]")))
first_option.click()

element = driver.find_element_by_xpath( "/html/body/div/div[2]/div/div/div/p/button[2]")   #变量 Create sequence
element.click()

link_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[3]/div/div/div/div[3]/div[2]/span/pre")))  
element_text = link_element.text
print(element_text)

#第二个循环

back_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[3]/div/div/div/div[4]/form/p/button")))  
back_element.click()

back_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/div/div/p/button[1]")))  
back_element.click()
driver.refresh()

time.sleep(2)
all_choice_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div/table/thead/tr/th[1]/input")))    #变量
driver.execute_script("arguments[0].click();", all_choice_element)

next_element = driver.find_element_by_xpath( "/html/body/div/div[1]/div/div/div/p/button")   #变量
next_element.click()

input_element  = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/input")))  
input_element.clear()
input_element.send_keys("Chr1:10000..10300")

first_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-selectable]")))
first_option.click()

element = driver.find_element_by_xpath( "/html/body/div/div[2]/div/div/div/p/button[2]")   #变量 Create sequence
element.click()

