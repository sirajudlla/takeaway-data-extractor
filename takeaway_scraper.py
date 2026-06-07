# Download_json file from takeaway

#import necessary modules

from undetected_chromedriver import Chrome
import time
import csv
from bs4 import BeautifulSoup
import json
import warnings

# Suppress Windows internal resource error warnings in the terminal

warnings.filterwarnings("ignore", category=ResourceWarning)

driver=Chrome()
driver.get('https://www.takeaway.com/be-en/delivery/food/bruxelles-1000')
time.sleep(100) 

soup=BeautifulSoup(driver.page_source,'html.parser')

#note.js main tag surch 
next_data_script=soup.find('script',id='__NEXT_DATA__')

if next_data_script:
    page_json_data = json.loads(next_data_script.string)
    with open('takeaway_raw_data.json','w',encoding='utf-8') as json_file:
        json.dump(page_json_data,json_file,ensure_ascii=False,indent=4)
    print('success all json file download')
else:
    print("no found json tag")

# Safe cleanup to avoid OSError or WinError6 on browser close
try:
    driver.close()
    time.sleep(20)
    driver.quit()
except Exception:
    pass
