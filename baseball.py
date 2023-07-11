from bs4 import BeautifulSoup
import requests
import json 

results=[]

def crawler(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    
    for article in soup.find_all(class_="r-ent"):
        if article.find("a") == None:
            continue
        title = article.find(class_="title").text.strip()
        author =  article.find(class_="author").text.strip()
        link =  article.find(class_="title").a['href']

        results.append({"title":title, "author":author, "limk":link})
    


url = 'https://www.ptt.cc/bbs/Baseball/index13816.html'
crawler(url)

soup = BeautifulSoup(requests.get(url).text, "html.parser")
next_url = soup.find_all(class_="btn wide")[1]
print(next_url.a['href'])

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, sort_keys=True, ensure_ascii=False)
