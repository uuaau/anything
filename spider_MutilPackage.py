from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import os

# 隐藏浏览器界面

# options=EdgeOptions()
# options.use_chromium = True
# options.add_argument("headless")

# # 防止检测
# option = EdgeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])


driver= Edge(executable_path='../edgedriver/msedgedriver.exe')
driver.get('https://www.guoguo-app.com/')

btn_srarch = driver.find_element(By.CSS_SELECTOR, '#display')
btn_srarch.click()
value = input('请输入快递单号:')
search_input = driver.find_element(By.CSS_SELECTOR, '#J_SearchInput')
search_input.send_keys(value)

btn_srarch = driver.find_element(By.CSS_SELECTOR, '#J_SearchBtn')
btn_srarch.click()

page_text = driver.page_source
tree = etree.HTML(page_text)

time.sleep(5)

content = driver.find_element(By.XPATH,"//*[@id='J_PackageDetail']").text
print(content)
if not os.path.exists('../Kuai'):  # 判断所在目录下是否有该文件名的文件夹
    os.mkdir('../Kuai')
file = '../Kuai/'+value+'.txt'
with open(file,'w',encoding='utf-8') as fp:
    fp.write(content)
print('-'*100)

driver.quit()


