from bs4 import BeautifulSoup
import requests
import json

results = []  # 儲存所有爬蟲的結果
url = 'https://www.ptt.cc/bbs/Baseball/index30.html'  # 把爬取網站網址存在url

def crawler(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser") # 丟給BeautifulSoup處理網頁原始碼

    for article in soup.find_all(class_="r-ent"):  # 找出所有文章(class="r_ent"的元素)
        if article.find("a") == None:  # 如果沒有a這個元素代表文章被刪除了
            continue
        title = article.find(class_="title").text.strip()  # 找到文章的標題
        author = article.find(class_="author").text.strip()  # 找到文章的作者
        link = "https://www.ptt.cc" + article.find(class_="title").a['href']  # 找到文章的連結

        results.append({"title": title, "author": author, "link": link}) # 將此篇文章加到results陣列中
        Url = url # 更新url成前一頁的網址 接著繼續爬

while True:
    crawler(url) #爬取 網址為url網頁 的資料

    soup = BeautifulSoup(requests.get(url).text, "html.parser") # 丟給BeautifulSoup處理網頁原始碼
    btn = soup.find_all(class_="btn wide")  # 取得右上角的那些按鈕
    if len(btn) < 4:  # 如果按鈕數量不足四個 代表沒有上一頁的按鈕了 直接Break
        break
    prev_page__url = "https://www.ptt.cc" + btn[1]['href']  # 取得上一頁的網址
    url = prev_page__url  # 更新url 繼續上一頁的爬蟲

# 儲存結果至json檔
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, sort_keys=True, ensure_ascii=False)
