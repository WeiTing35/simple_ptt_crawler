# Simple Crawler
import urllib.request as req
url="https://www.ptt.cc/bbs/Stock/index.html"

request=req.Request(url, headers={
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.3"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")

# print(data)    

import bs4
root = bs4.BeautifulSoup(data,'html.parser')
titles=root.findAll("div", class_="title")

#列出所有標題
for title in titles:
    if title!= None:
        print(title.a.string) #找尋a標題裡面的string
