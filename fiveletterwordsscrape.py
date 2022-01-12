import bs4
import sys
import requests

website_list = []
for i in range(2,16):
    website_list.append('https://www.bestwordlist.com/5letterwordspage'+str(i)+'.htm')

res = [requests.get('https://www.bestwordlist.com/5letterwords.htm')]
res[0].raise_for_status()
for url in website_list:
    res.append(requests.get(url))
    res[-1].raise_for_status()
#res.raise_for_status()

filename = 'fiveletterwords.txt'
with open(filename, 'w+', encoding="utf-8") as f:
    for response in res:
        wordsoup = bs4.BeautifulSoup(response.text,"html.parser")
        for word in wordsoup.select('span.mot'):
            for k in word.getText().split():
                f.write(k+'\n')
f.close()

filename1 = 'crazyfiveletterwords.txt'
with open(filename1, 'w+', encoding="utf-8") as g:
    for response in res:
        wordsoup = bs4.BeautifulSoup(response.text,"html.parser")
        for word in wordsoup.select('span.mot2'):
            for k in word.getText().split():
                g.write(k+'\n')
g.close()
