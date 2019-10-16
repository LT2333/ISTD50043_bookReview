import requests
from bs4 import BeautifulSoup as soup
import csv
# get list of asin
with open('scrap.csv', 'r') as csvfile:
    asin_ls = list(csv.reader(csvfile, delimiter=','))[0]

#function to get author+title from asin
def get_info_API(number):
    payload = {'api_key': '833be2d6782f042e3c2006cc2b9e7736', 'url':'https://httpbin.org/ip', 'render': 'true'}
    r = requests.get('https://www.amazon.com/dp/'+number, params=payload).text
    page_soup=soup(r,'html.parser')
    title=page_soup.find("h1",{"id":"title"}).get_text().replace("\n","")
    author=page_soup.find('span', {"class" :"author notFaded"}).get_text().replace("\n","")
    return title,author

#loop and write the result to the resultant csv
out_ls=[]# result 
fail_ls=[]# asin that failed (due to non-book, html format unmatched)
for number in asin_ls[4000:]:  #0-1000,1000-2000,2000-4000
    try:
        title,author=get_info_API(number)
        with open('scrap_out.csv', 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            ls=[number,title,author]
            wr.writerow(ls) 
            out_ls.append(ls)    
    except:
        fail_ls.append(number)
