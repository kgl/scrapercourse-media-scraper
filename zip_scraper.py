from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests
import os
import time
import zipfile


# 1. 操作網頁的查詢功能
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(
    'https://www.twse.com.tw/zh/statistics/statisticsList?type=05&subType=225')

select = Select(driver.find_element(By.ID, 'd1').find_element(
    By.CSS_SELECTOR, "select[name='yy']"))
select.select_by_value('2021')

button = driver.find_element(By.CSS_SELECTOR, "a[class='button search']")
button.click()

# 2. 爬取zip檔案連結
soup = BeautifulSoup(driver.page_source, 'lxml')

links = soup.find('table', {'class': 'grid links'}).find_all('a')

# 3. 下載zip檔案、解壓縮
for index, link in enumerate(links):
    zip_response = requests.get('https://www.twse.com.tw/' + link.get('href'))

    if not os.path.exists('zip'):
        os.mkdir('zip')

    with open(f'zip\\{index+1}.zip', 'wb') as file:
        file.write(zip_response.content)

    zipfile.ZipFile(f'zip\\{index+1}.zip').extractall('zip\\.')
