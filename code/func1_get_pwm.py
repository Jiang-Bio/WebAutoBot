from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
from webdriver_manager.microsoft import EdgeChromiumDriverManager 
#from selenium.webdriver.edge.options import Options
#from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge


def func(wells,webpath,patterns,directory):
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    global driver  
    driver = Edge(EdgeChromiumDriverManager().install(),options=edge_options)
    driver.get(webpath)# 

    for well in wells: 
            element = driver.find_element_by_id(well)   #变量
            element.click()

            wait = WebDriverWait(driver, 30)
            print(well)    
            if "Nana2_9__WRKY_WG" in webpath:
                  text_content=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/table/tbody/tr[3]/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td/a[1]")))  
            else :
                  text_content=wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/table/tbody/tr[2]/td[2]/table/tbody/tr/td/table[1]/tbody/tr/td/a[1]"))) 
            
            a=text_content.text
            print(a)
            tfName = "TF_"+well+".pwm"    
            tfName=os.path.join(directory,tfName)
            print(tfName)
            wait = WebDriverWait(driver, 30)
            if "Nana2_9__WRKY_WG" in webpath:
                  modal_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/table/tbody/tr[3]/td[1]/input[2]')))   
            else:
                  modal_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/table/tbody/tr[2]/td[1]/input[2]')))   
            modal_button.click()
            iframe_element = driver.find_element_by_css_selector('iframe[width="1100"][height="850"]')
            driver.switch_to_frame(iframe_element) #
            driver.execute_script("document.body.style.zoom='80%'")
            for pattern in patterns:
                    wait1 = WebDriverWait(driver, 30)
                    input_element  = wait1.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/table[1]/tbody/tr[2]/td[5]/input")))  
                    input_element.clear()
                    input_element.send_keys(pattern)

                    wait2 = WebDriverWait(driver, 30)
                    modal_button2 = wait2.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/table[7]/tbody/tr/td/input[3]")))  #calculate
                    driver.execute_script("$(arguments[0]).click()",modal_button2)
            
                    wait2 = WebDriverWait(driver, 100)
                    logo=wait2.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/table[4]/tbody/tr[3]/td[1]/a/img")))  
                    title_content = logo.get_attribute('title')#

                    with open(tfName,'a') as file:
                        file.write(f">{pattern}\n{title_content}")

            wait3 = WebDriverWait(driver, 30)
            modal_button3 = wait3.until(EC.element_to_be_clickable((By.XPATH,"/html/body/form/table[7]/tbody/tr/td/input[1]")))
            driver.execute_script("$(arguments[0]).click()",modal_button3)
            driver.switch_to.default_content()#
            element = driver.find_element_by_id(well)
            element.click()# 
    driver.quit()#退出浏览器

    
if __name__=='__main__':
    #list_A = [f"A{i}" for i in range(1, 13)]
    #list_B = [f"B{i}" for i in range(1, 13)]

    wells = ['B4','A10'] 
    webpath = 'http:/selex/zhu_welldisp.php?base=WG_50ul_2ul_SELEX_20230717'
    patterns = [
                'NNTTGACTTGACNNN',
                'NNTTGACNTTGACNNN',
                'NNTTGACNNTTGACNNN']
    directory="E:\test_python"
    func(wells,webpath,patterns,directory)
    print("###########################Calculation completed###########################")


