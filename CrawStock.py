import requests
from bs4 import BeautifulStoneSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparnet_encoding
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL + stock
        html=getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict={}
            soup=BeautifulSoup(html,"html.parser")
            stockInfo=soup.find('')
    return ""

def main():
    #获得股票链接
    stock_list_url = 'https://app.finance.ifeng.com/list/stock.php?t=ha'
    #获得个股信息
    stock_info_url = 'https://www.laohu8.com/search/all?word='

    output_file = "D://StockInfo.txt"
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

main()
