import requests, json


url='https://api.thecatapi.com/v1/images/search'

n=int(input('please input a number : '))

result=[]
for i in range(n):
    res=requests.get(url).json()
    pic=res[0]['url']
    result.append(pic)

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, sort_keys=True, ensure_ascii=False)
