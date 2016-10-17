import re
import urllib.request
import os
from bs4 import BeautifulSoup

def fileName(path):
    localPath = 'C:\\doubanPic'
    if not os.path.isdir(localPath):
        os.mkdir(targetDir)
    pos=int(path.rindex('/'))
    picPath=os.path.join(localPath,path[pos+1:])
    return picPath

def saveFile(data):
    savePath='C:\\kankan\\temp.txt'
    if not os.path.exists(savePath):
        os.mkdir(savePath)
    file=open(savePath,'wb')
    file.write(data)
    file.close()

if __name__=='__main__':
    url='https://music.douban.com/'   #抓取的是豆瓣音乐页面上的所有图片，更改网址后可以抓取其他网页上的页面
    headers={
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'Accept-Encoding':'gzip, deflate, sdch, br',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        # 'Host':'www.douban.com',
        # 'Connection':'keep-alive',
        # 'Accept-Language':'zh-CN,zh;q=0.8'
        }
    req=urllib.request.Request(url=url,headers=headers)
    html=urllib.request.urlopen(req)
    
    Page=html.read()
    savePage=Page.decode('utf-8')

    print(type(html))             #<class 'http.client.HTTPResponse'>
    print(type(Page))             #<class 'bytes'>
    print(type(savePage))         #<class 'str'>
    saveFile(Page)
    
    bs=BeautifulSoup(markup=html,features='html.parser')
    for link in bs.findAll('img'):
        print(link['src'])
        try:
            urllib.request.urlretrieve(link['src'],fileName(link['src']))
        except:
            print('Error')

