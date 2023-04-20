
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products=[]
prices=[]
des=[]

driver.get("https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_6f7e5ed3-df0a-4263-8915-bac4643afb61_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y")

content = driver.page_source
soup= BeautifulSoup(content,"html.parser")

for p in soup.findAll('a',href=True,attrs={'class':'_1fQZEK'}):
    name=p.find('div',attrs={'class':'_4rR01T'})
    price=p.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    dd=p.find('div',attrs={'class':'fMghEO'})
    products.append(name.text)
    prices.append(price.text)
    des.append(dd.text)
    
    
    df=pd.DataFrame({'Product Name':products,'Prices':prices,'Descraption':des})
    df.to_csv('products.csv',index=False,encoding='utf-8')
                   