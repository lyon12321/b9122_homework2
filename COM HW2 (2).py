#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib
import urllib.request
import requests
import re
from tqdm import tqdm
from bs4 import BeautifulSoup


# In[2]:


def getAllUrl(url):
    import urllib.request
    from bs4 import BeautifulSoup
    req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, features='html.parser')
    tags = soup.find_all('a')
    lst = []
    for tag in tags:
        lst.append(str(tag.get('href')).strip())
    return lst


# In[3]:


a=getAllUrl(url='https://www.federalreserve.gov/newsevents/pressreleases.htm')
test='/'
res = [idx for idx in a if idx[0].lower() == test.lower()]


# In[5]:


res


# In[4]:


def getAllword(url):
    import urllib.request
    from bs4 import BeautifulSoup
    req = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode("utf-8")


# In[6]:


#Question 1 No.1
url='https://www.federalreserve.gov'
result=[]
for url_value in tqdm(res):
    url_whole = url+url_value
    html=requests.get(url_whole)
    soup=BeautifulSoup(html.text)
    text = soup.get_text()
    text=text.lower()
    if 'covid' in text:
        result.append(url_whole)


# In[36]:


print(result)


# In[20]:


#Question 1 No.2
b=getAllUrl(url='https://www.sec.gov/news/pressreleases')
test='/'
test_1='/news/press-release/'
c=[]
for url in b:
    if len(url) != 0:
        c.append(url)
res_0 = [idx for idx in c if idx[0].lower() == test.lower()]
res_1 = [idx for idx in res_0 if test_1 in idx]


# In[21]:


#Question 1 No.2

url_2='https://www.sec.gov'
result_2=[]
for url_value in tqdm(res_1):
    url_whole = url_2+url_value
    html=requests.get(url_whole)
    soup=BeautifulSoup(html.text)
    text = soup.get_text()
    text_1=text.lower()
    if 'charges' in text_1:
        result_2.append(url_whole)
    if len(result_2)==20:
        break
print(result_2)


# In[14]:


final_res=[]
for url_res in result_2:
    comb = []
    html=requests.get(url_res)
    soup=BeautifulSoup(html.text)
    text = soup.get_text()
    comb.append(url_res)
    comb.append(text)
    final_res.append(comb)


# In[22]:


for i in final_res:
    print(i)

