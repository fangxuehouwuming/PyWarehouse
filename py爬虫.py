import requests
import os

def pic_paqv():
    url = input("请输入要爬取的网址\n")
    root = "D://pics//"
    path = root + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb')as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")
    return


from bs4 import BeautifulSoup
import requests
url1="https://python123.io/ws/demo.html"
url2="https://www.shanghairanking.cn/rankings/bcur/201611"

r = requests.get(url2)
r.raise_for_status()
r.encoding=r.apparent_encoding
demo = r.text
#print(demo)
soup = BeautifulSoup(demo,"html.parser")
print(soup.title)
tag = soup.a
print(tag)
print(tag.name)
print(tag.parent.name)
tag.parent.parent.name
tag.attrs
tag.attrs['href']
type(tag)
type(tag.attrs)
print(type(tag.string))
soup.body.contents[0]

for child in soup.body.children:
    print(child)
for child in soup.body.descendants:
    print(child)

print(soup.a.prettify())

for link in soup.find_all('a'):
    print(link.get('href'))

soup.find_all(['a','b'])

soup.find_all('p','course')

soup.find_all(string='Basic Python')

content=soup.prettify()
import os
root="D://try//"
path=root+"html.txt"
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path,'wb')as f:
            f.write(content.encode('utf-8'))
            f.close()
            print("文件保存成功")
except:
    print("出错")