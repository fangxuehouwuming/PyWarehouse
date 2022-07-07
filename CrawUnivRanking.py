import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        #如果tr标签不是bs库定义的Tag类型，则过滤掉
        if isinstance(tr,bs4.element.Tag):
            trContents = tr.contents

            #print(tr.prettify())
            #print("\n\n\n\n\n\n")
            #for child in tr:
            #    print(child.name)
            #print(trContents[0].div.string.strip())
            #print(trContents[1].a.string.strip())
            #print(trContents[4].string.strip())

            ulist.append([trContents[0].div.string.strip(), trContents[1].a.string.strip(), trContents[4].string.strip()])

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    unifo = []
    url = "https://www.shanghairanking.cn/rankings/bcur/201611"
    html = getHTMLText(url)
    fillUnivList(unifo,html)
    printUnivList(unifo,len(unifo))

main()