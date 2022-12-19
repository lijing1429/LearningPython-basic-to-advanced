import requests
from bs4 import BeautifulSoup

def url_pro(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup.get_text().replace("\n\n", "")

URL = "https://www.haitang16.com/book/62941.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("ol", class_="inline mb20")

l1 = []

for ele in results.find_all("li"):

    url = ele.find("a").get('href')
    l1.append(ele.get_text())
    l1.append(url_pro(url))
    print(1)
    # print(ele.get_text())
    # break

with open("file12.txt", "w", encoding='utf-8') as output:
    for row in l1:  
        output.write(str(row) + '\n')
        print(2)

# print(l1)
    
    
    # url = 'http://m.marchettieng.com'+ ele.find("a").get('href')
    # print(url)



# # print(soup)
# print(results)
# print(len(results))
# print(type(soup))