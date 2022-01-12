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
filename1 = 'crazyfiveletterwords.txt'
filename2 = 'allfiveletterwords.txt'

with open(filename, 'w+', encoding="utf-8") as f, open(filename1, 'w+', encoding="utf-8") as g, open(filename2, 'w+', encoding="utf-8") as h:
    for response in res:
        wordsoup = bs4.BeautifulSoup(response.text,"html.parser")
        for word in wordsoup.select('span.mot,span.mot2'):
            for k in word.getText().split():
                if word['class'] == ['mot']:
                    f.write(k+'\n')
                else:
                    g.write(k+'\n')
                h.write(k+'\n')

f.close()
g.close()
h.close()
