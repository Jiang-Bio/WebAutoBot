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
import pandas as pd
import sys
sys.path.append(r"C:/Users/JIANGDK/Desktop/")
df = pd.read_excel(r"C:/Users/JIANGDK/Desktop/region.xlsx",sheet_name="Sheet1")
regions = df.iloc[0].to_list()

global driver
edge_options = EdgeOptions()
#edge_options.use_chromium = True
#edge_options.add_argument("--headless")
#edge_options.add_argument("--disable-gpu")
driver = Edge(EdgeChromiumDriverManager().install(),options=edge_options)
driver.get(r"https://tools.1001genomes.org/vcfsubset/#select_strains")
wait1 = WebDriverWait(driver, 20)
time.sleep(2)
all_choice_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/div/table/thead/tr/th[1]/input")))    #变量
driver.execute_script("arguments[0].click();", all_choice_element)

next_element = driver.find_element_by_xpath( "/html/body/div/div[1]/div/div/div/p/button")   #变量
next_element.click()
for region in regions:

    input_element  = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/input")))  
    input_element.send_keys(region)
    first_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-selectable]")))
    first_option.click()

    element = driver.find_element_by_xpath( "/html/body/div/div[2]/div/div/div/p/button[2]")   #变量
    element.click()

    element = driver.find_element_by_xpath( "/html/body/div/div[3]/div/div/div/form/p/button[2]")   #变量
    element.click()

    link_element = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[4]/div/div/div/form/p/button[2]")))  
    link_element.click()
    time.sleep(2)
    element = driver.find_element_by_xpath( "/html/body/div/div[4]/div/div/div/form/p/button[1]")   #变量
    element.click()

    element = driver.find_element_by_xpath( "/html/body/div/div[3]/div/div/div/form/p/button[1]")   #变量
    element.click()

    element = driver.find_element_by_xpath( "/html/body/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div/a")   #变量
    element.click()

time.sleep(120)
print("##########################")
driver.quit()
