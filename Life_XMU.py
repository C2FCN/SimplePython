import requests
from bs4 import BeautifulSoup
lifexmu="http://life.xmu.edu.cn"
lifexmu_page="http://life.xmu.edu.cn/3791/list"
res = requests.get("http://life.xmu.edu.cn/3791/list.htm")
res.encoding="utf-8"
soup = BeautifulSoup(res.text,"html.parser")
totalnum=soup.select(".all_pages")[0].text
for i in range(1,int(totalnum)+1):
    eachlink=lifexmu_page+str(i)+".htm"
    print(eachlink)
    res = requests.get(eachlink)
    res.encoding="utf-8"
    soup = BeautifulSoup(res.text,"html.parser")
    for link in soup.select("h2"):
        news=link.select("a")
        if(len(news)>0):
            print(news[0]["title"])
            print(eachlink)
            eachlink=lifexmu+news[0]["href"]
            eachres = requests.get(eachlink)
            eachres.encoding="utf-8"
            eachsoup = BeautifulSoup(eachres.text,"html.parser")
            for eachcontent in eachsoup.select(".wp_articlecontent"):
                print(eachcontent.text)
