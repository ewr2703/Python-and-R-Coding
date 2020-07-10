# Eric Rodgers & Keith Kunz
# IST 736 Text Mining
# Final Project
# Professor Jeremy Bolton

import requests #requesting yelp reviews 
import csv
import nltk
from nltk.tokenize import word_tokenize # tokenizing reviews
from nltk.probability import FreqDist
from bs4 import BeautifulSoup # for brining in yelp data
import re # (running regular expressions)
from nltk.corpus import stopwords # needed to apply stopwords
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()

# Restaurants, name is in the html link, take newest 60 reviews for each restaurant. Start on $ first

############################################################################################################### 
# Mexican Restaurants

#Pueblas
m1 = requests.get('https://www.yelp.com/biz/pueblas-mexican-kitchen-houston-2?osq=Mexican%20Food&sort_by=date_desc')
m1.status_code
m1.text
soup_m1 = BeautifulSoup(m1.text, "html.parser")
divs = soup_m1.findAll(itemprop="review")

reviews_mex_1 = []
for div in divs:
    reviews_mex_1.append(div.find('p').text)

m2 = requests.get('https://www.yelp.com/biz/pueblas-mexican-kitchen-houston-2?osq=Mexican%20Food&start=20&sort_by=date_desc')
m2.status_code
m2.text
soup_m2 = BeautifulSoup(m2.text, "html.parser")
divs = soup_m2.findAll(itemprop="review")

reviews_mex_2 = []
for div in divs:
    reviews_mex_2.append(div.find('p').text)

m3 = requests.get('https://www.yelp.com/biz/pueblas-mexican-kitchen-houston-2?osq=Mexican%20Food&start=40&sort_by=date_desc')
m3.status_code
m3.text
soup_m3 = BeautifulSoup(m3.text, "html.parser")
divs = soup_m3.findAll(itemprop="review")

reviews_mex_3 = []
for div in divs:
    reviews_mex_3.append(div.find('p').text)

pueblas = reviews_mex_1 + reviews_mex_2 + reviews_mex_3
len(pueblas)
    
# La Calle Tacos
m4 = requests.get('https://www.yelp.com/biz/la-calle-tacos-houston-5?osq=Mexican%20Food&sort_by=date_desc')
m4.status_code
m4.text
soup_m4 = BeautifulSoup(m4.text, "html.parser")
divs = soup_m4.findAll(itemprop="review")

reviews_mex_4 = []
for div in divs:
    reviews_mex_4.append(div.find('p').text)

m5 = requests.get('https://www.yelp.com/biz/la-calle-tacos-houston-5?osq=Mexican%20Food&start=20&sort_by=date_desc')
m5.status_code
m5.text
soup_m5 = BeautifulSoup(m5.text, "html.parser")
divs = soup_m5.findAll(itemprop="review")

reviews_mex_5 = []
for div in divs:
    reviews_mex_5.append(div.find('p').text)

m6 = requests.get('https://www.yelp.com/biz/la-calle-tacos-houston-5?osq=Mexican%20Food&start=40&sort_by=date_desc')
m6.status_code
m6.text
soup_m6 = BeautifulSoup(m6.text, "html.parser")
divs = soup_m6.findAll(itemprop="review")

reviews_mex_6 = []
for div in divs:
    reviews_mex_6.append(div.find('p').text)
    
la_calle = reviews_mex_4 + reviews_mex_5 + reviews_mex_6 
len(la_calle)

# Taqueria Del Sol
m7 = requests.get('https://www.yelp.com/biz/taqueria-del-sol-houston?osq=Mexican%20Food&sort_by=date_desc')
m7.status_code
m7.text
soup_m7 = BeautifulSoup(m7.text, "html.parser")
divs = soup_m7.findAll(itemprop="review")

reviews_mex_7 = []
for div in divs:
    reviews_mex_7.append(div.find('p').text)

m8 = requests.get('https://www.yelp.com/biz/taqueria-del-sol-houston?osq=Mexican%20Food&start=20&sort_by=date_desc')
m8.status_code
m8.text
soup_m8 = BeautifulSoup(m8.text, "html.parser")
divs = soup_m8.findAll(itemprop="review")

reviews_mex_8 = []
for div in divs:
    reviews_mex_8.append(div.find('p').text)

m9 = requests.get('https://www.yelp.com/biz/taqueria-del-sol-houston?osq=Mexican%20Food&start=40&sort_by=date_desc')
m9.status_code
m9.text
soup_m9 = BeautifulSoup(m9.text, "html.parser")
divs = soup_m9.findAll(itemprop="review")

reviews_mex_9 = []
for div in divs:
    reviews_mex_9.append(div.find('p').text)
    
taq = reviews_mex_7 + reviews_mex_8 + reviews_mex_9
len(taq)

# Dona Maria
m10 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Mexican%20Food&sort_by=date_desc')
m10.status_code
m10.text
soup_m10 = BeautifulSoup(m10.text, "html.parser")
divs = soup_m10.findAll(itemprop="review")

reviews_mex_10 = []
for div in divs:
    reviews_mex_10.append(div.find('p').text)

m11 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Mexican%20Food&start=20&sort_by=date_desc')
m11.status_code
m11.text
soup_m11 = BeautifulSoup(m11.text, "html.parser")
divs = soup_m11.findAll(itemprop="review")

reviews_mex_11 = []
for div in divs:
    reviews_mex_11.append(div.find('p').text)

m12 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Mexican%20Food&start=40&sort_by=date_desc')
m12.status_code
m12.text
soup_m12 = BeautifulSoup(m12.text, "html.parser")
divs = soup_m12.findAll(itemprop="review")

reviews_mex_12 = []
for div in divs:
    reviews_mex_12.append(div.find('p').text)

don_m = reviews_mex_10 + reviews_mex_11 + reviews_mex_12
len(don_m)

# Las Tortas Perronas
m13 = requests.get('https://www.yelp.com/biz/las-tortas-perronas-houston-8?osq=Mexican%20Food&sort_by=date_desc')
m13.status_code
m13.text
soup_m13 = BeautifulSoup(m13.text, "html.parser")
divs = soup_m13.findAll(itemprop="review")

reviews_mex_13 = []
for div in divs:
    reviews_mex_13.append(div.find('p').text)

m14 = requests.get('https://www.yelp.com/biz/las-tortas-perronas-houston-8?osq=Mexican%20Food&start=20&sort_by=date_desc')
m14.status_code
m14.text
soup_m14 = BeautifulSoup(m14.text, "html.parser")
divs = soup_m14.findAll(itemprop="review")

reviews_mex_14 = []
for div in divs:
    reviews_mex_14.append(div.find('p').text)

m15 = requests.get('https://www.yelp.com/biz/las-tortas-perronas-houston-8?osq=Mexican%20Food&start=40&sort_by=date_desc')
m15.status_code
m15.text
soup_m15 = BeautifulSoup(m15.text, "html.parser")
divs = soup_m15.findAll(itemprop="review")

reviews_mex_15 = []
for div in divs:
    reviews_mex_15.append(div.find('p').text)
    
las_tort = reviews_mex_13 + reviews_mex_14 + reviews_mex_15
len(las_tort)

# All mexican restaurants
mex_rest = pueblas + la_calle + taq + don_m + las_tort
mex_rest = [x.lower() for x in mex_rest] # lower all words
for review in mex_rest:
    print(review, "\n")
len(mex_rest)

############################################################################################################### 
# Vietnamese Restaurants

# Roostar Vietnamese Grill
v1 = requests.get('https://www.yelp.com/biz/roostar-vietnamese-grill-houston-2?osq=Vietnamese%20Food&sort_by=date_desc')
v1.status_code
v1.text
soup_v1 = BeautifulSoup(v1.text, "html.parser")
divs = soup_v1.findAll(itemprop="review")

reviews_viet_1 = []
for div in divs:
    reviews_viet_1.append(div.find('p').text)

v2 = requests.get('https://www.yelp.com/biz/roostar-vietnamese-grill-houston-2?osq=Vietnamese%20Food&start=20&sort_by=date_desc')
v2.status_code
v2.text
soup_v2 = BeautifulSoup(v2.text, "html.parser")
divs = soup_v2.findAll(itemprop="review")

reviews_viet_2 = []
for div in divs:
    reviews_viet_2.append(div.find('p').text)

v3 = requests.get('https://www.yelp.com/biz/roostar-vietnamese-grill-houston-2?osq=Vietnamese%40Food&start=40&sort_by=date_desc')
v3.status_code
v3.text
soup_v3 = BeautifulSoup(v3.text, "html.parser")
divs = soup_v3.findAll(itemprop="review")

reviews_viet_3 = []
for div in divs:
    reviews_viet_3.append(div.find('p').text)

roo = reviews_viet_1 + reviews_viet_2 + reviews_viet_3
    
# Pho Saigon
v4 = requests.get('https://www.yelp.com/biz/pho-saigon-houston-12?osq=Vietnamese%20Food&sort_by=date_desc')
v4.status_code
v4.text
soup_v4 = BeautifulSoup(v4.text, "html.parser")
divs = soup_v4.findAll(itemprop="review")

reviews_viet_4 = []
for div in divs:
    reviews_viet_4.append(div.find('p').text)

v5 = requests.get('https://www.yelp.com/biz/pho-saigon-houston-12?osq=Vietnamese%20Food&start=20&sort_by=date_desc')
v5.status_code
v5.text
soup_v5 = BeautifulSoup(v5.text, "html.parser")
divs = soup_v5.findAll(itemprop="review")

reviews_viet_5 = []
for div in divs:
    reviews_viet_5.append(div.find('p').text)

v6 = requests.get('https://www.yelp.com/biz/pho-saigon-houston-12?osq=Vietnamese%20Food&start=40&sort_by=date_desc')
v6.status_code
v6.text
soup_v6 = BeautifulSoup(v6.text, "html.parser")
divs = soup_v6.findAll(itemprop="review")

reviews_viet_6 = []
for div in divs:
    reviews_viet_6.append(div.find('p').text)
    
phosai = reviews_viet_4 + reviews_viet_5 + reviews_viet_6  

# Manna Noodle House
v7 = requests.get('https://www.yelp.com/biz/manna-noodle-house-houston?sort_by=date_desc')
v7.status_code
v7.text
soup_v7 = BeautifulSoup(v7.text, "html.parser")
divs = soup_v7.findAll(itemprop="review")

reviews_viet_7 = []
for div in divs:
    reviews_viet_7.append(div.find('p').text)

v8 = requests.get('https://www.yelp.com/biz/manna-noodle-house-houston?start=20&sort_by=date_desc')
v8.status_code
v8.text
soup_v8 = BeautifulSoup(v8.text, "html.parser")
divs = soup_v8.findAll(itemprop="review")

reviews_viet_8 = []
for div in divs:
    reviews_viet_8.append(div.find('p').text)

v9 = requests.get('https://www.yelp.com/biz/manna-noodle-house-houston?start=40&sort_by=date_desc')
v9.status_code
v9.text
soup_v9 = BeautifulSoup(v9.text, "html.parser")
divs = soup_v9.findAll(itemprop="review")

reviews_viet_9 = []
for div in divs:
    reviews_viet_9.append(div.find('p').text)
    
manna = reviews_viet_7 + reviews_viet_8 + reviews_viet_9

# Nam Giao
v10 = requests.get('https://www.yelp.com/biz/nam-giao-houston?osq=Vietnamese%20Food&sort_by=date_desc')
v10.status_code
v10.text
soup_v10 = BeautifulSoup(v10.text, "html.parser")
divs = soup_v10.findAll(itemprop="review")

reviews_viet_10 = []
for div in divs:
    reviews_viet_10.append(div.find('p').text)

v11 = requests.get('https://www.yelp.com/biz/nam-giao-houston?osq=Vietnamese%20Food&start=20&sort_by=date_desc')
v11.status_code
v11.text
soup_v11 = BeautifulSoup(v11.text, "html.parser")
divs = soup_v11.findAll(itemprop="review")

reviews_viet_11 = []
for div in divs:
    reviews_viet_11.append(div.find('p').text)

v12 = requests.get('https://www.yelp.com/biz/nam-giao-houston?osq=Vietnamese%20Food&start=40&sort_by=date_desc')
v12.status_code
v12.text
soup_v12 = BeautifulSoup(v12.text, "html.parser")
divs = soup_v12.findAll(itemprop="review")

reviews_viet_12 = []
for div in divs:
    reviews_viet_12.append(div.find('p').text)

namg = reviews_viet_10 + reviews_viet_11 + reviews_viet_12  

# Les Givral's Sandwich & Café
v13 = requests.get('https://www.yelp.com/biz/les-givrals-sandwich-and-caf%C3%A9-houston-2?osq=Vietnamese%20Food&sort_by=date_desc')
v13.status_code
v13.text
soup_v13 = BeautifulSoup(v13.text, "html.parser")
divs = soup_v13.findAll(itemprop="review")

reviews_viet_13 = []
for div in divs:
    reviews_viet_13.append(div.find('p').text)

v14 = requests.get('https://www.yelp.com/biz/les-givrals-sandwich-and-caf%C3%A9-houston-2?osq=Vietnamese%20Food&start=20&sort_by=date_desc')
v14.status_code
v14.text
soup_v14 = BeautifulSoup(v14.text, "html.parser")
divs = soup_v14.findAll(itemprop="review")

reviews_viet_14 = []
for div in divs:
    reviews_viet_14.append(div.find('p').text)

v15 = requests.get('https://www.yelp.com/biz/les-givrals-sandwich-and-caf%C3%A9-houston-2?osq=Vietnamese%20Food&start=40&sort_by=date_desc')
v15.status_code
v15.text
soup_v15 = BeautifulSoup(v15.text, "html.parser")
divs = soup_v15.findAll(itemprop="review")

reviews_viet_15 = []
for div in divs:
    reviews_viet_15.append(div.find('p').text)
    
lesgiv = reviews_viet_13 + reviews_viet_14 + reviews_viet_15

viet_rest = roo + phosai + manna + namg + lesgiv
viet_rest = [x.lower() for x in viet_rest] # lower all words
for review in viet_rest:
    print(review, "\n")
len(viet_rest)

############################################################################################################### 
# BBQ Restaurants

# Jimee's BBQ
bbq1 = requests.get('https://www.yelp.com/biz/jimees-bbq-houston?osq=BBQ&sort_by=date_desc')
bbq1.status_code
bbq1.text
soup_bbq1 = BeautifulSoup(bbq1.text, "html.parser")
divs = soup_bbq1.findAll(itemprop="review")

reviews_bbq_1 = []
for div in divs:
    reviews_bbq_1.append(div.find('p').text)

bbq2 = requests.get('https://www.yelp.com/biz/jimees-bbq-houston?osq=BBQ&start=20&sort_by=date_desc')
bbq2.status_code
bbq2.text
soup_bbq2 = BeautifulSoup(bbq2.text, "html.parser")
divs = soup_bbq2.findAll(itemprop="review")

reviews_bbq_2 = []
for div in divs:
    reviews_bbq_2.append(div.find('p').text)

bbq3 = requests.get('https://www.yelp.com/biz/jimees-bbq-houston?osq=BBQ&start=40&sort_by=date_desc')
bbq3.status_code
bbq3.text
soup_bbq3 = BeautifulSoup(bbq3.text, "html.parser")
divs = soup_bbq3.findAll(itemprop="review")

reviews_bbq_3 = []
for div in divs:
    reviews_bbq_3.append(div.find('p').text)

jimee = reviews_bbq_1 + reviews_bbq_2 + reviews_bbq_3
len(jimee)

# Fainmous BBQ
bbq4 = requests.get('https://www.yelp.com/biz/fainmous-bbq-houston?osq=BBQ&sort_by=date_desc')
bbq4.status_code
bbq4.text
soup_bbq4 = BeautifulSoup(bbq4.text, "html.parser")
divs = soup_bbq4.findAll(itemprop="review")

reviews_bbq_4 = []
for div in divs:
    reviews_bbq_4.append(div.find('p').text)

bbq5 = requests.get('https://www.yelp.com/biz/fainmous-bbq-houston?osq=BBQ&start=20&sort_by=date_desc')
bbq5.status_code
bbq5.text
soup_bbq5 = BeautifulSoup(bbq5.text, "html.parser")
divs = soup_bbq5.findAll(itemprop="review")

reviews_bbq_5 = []
for div in divs:
    reviews_bbq_5.append(div.find('p').text)

bbq6 = requests.get('https://www.yelp.com/biz/fainmous-bbq-houston?osq=BBQ&start=40&sort_by=date_desc')
bbq6.status_code
bbq6.text
soup_bbq6 = BeautifulSoup(bbq6.text, "html.parser")
divs = soup_bbq6.findAll(itemprop="review")

reviews_bbq_6 = []
for div in divs:
    reviews_bbq_6.append(div.find('p').text)
    
fain = reviews_bbq_4 + reviews_bbq_5 + reviews_bbq_6
len(fain)

# Hitters BBQ & Catering
bbq7 = requests.get('https://www.yelp.com/biz/hitters-bbq-and-catering-houston?osq=BBQ&sort_by=date_desc')
bbq7.status_code
bbq7.text
soup_bbq7 = BeautifulSoup(bbq7.text, "html.parser")
divs = soup_bbq7.findAll(itemprop="review")

reviews_bbq_7 = []
for div in divs:
    reviews_bbq_7.append(div.find('p').text)

bbq8 = requests.get('https://www.yelp.com/biz/hitters-bbq-and-catering-houston?osq=BBQ&start=20&sort_by=date_desc')
bbq8.status_code
bbq8.text
soup_bbq8 = BeautifulSoup(bbq8.text, "html.parser")
divs = soup_bbq8.findAll(itemprop="review")

reviews_bbq_8 = []
for div in divs:
    reviews_bbq_8.append(div.find('p').text)

bbq9 = requests.get('https://www.yelp.com/biz/hitters-bbq-and-catering-houston?osq=BBQ&start=40&sort_by=date_desc')
bbq9.status_code
bbq9.text
soup_bbq9 = BeautifulSoup(bbq9.text, "html.parser")
divs = soup_bbq9.findAll(itemprop="review")

reviews_bbq_9 = []
for div in divs:
    reviews_bbq_9.append(div.find('p').text)
    
hitbbq = reviews_bbq_7 + reviews_bbq_8 + reviews_bbq_9 
len(hitbbq)

# Two Brothers Smokin Oak Kitchen
bbq10 = requests.get('https://www.yelp.com/biz/two-brothers-smokin-oak-kitchen-houston-2?osq=BBQ&sort_by=date_desc')
bbq10.status_code
bbq10.text
soup_bbq10 = BeautifulSoup(bbq10.text, "html.parser")
divs = soup_bbq10.findAll(itemprop="review")

reviews_bbq_10 = []
for div in divs:
    reviews_bbq_10.append(div.find('p').text)

bbq11 = requests.get('https://www.yelp.com/biz/two-brothers-smokin-oak-kitchen-houston-2?osq=BBQ&start=20&sort_by=date_desc')
bbq11.status_code
bbq11.text
soup_bbq11 = BeautifulSoup(bbq11.text, "html.parser")
divs = soup_bbq11.findAll(itemprop="review")

reviews_bbq_11 = []
for div in divs:
    reviews_bbq_11.append(div.find('p').text)

two_bro = reviews_bbq_10 + reviews_bbq_11
len(two_bro)

# Xin Jiang BBQ
bbq13 = requests.get('https://www.yelp.com/biz/xin-jiang-bbq-houston?osq=BBQ&sort_by=date_desc')
bbq13.status_code
bbq13.text
soup_bbq13 = BeautifulSoup(bbq13.text, "html.parser")
divs = soup_bbq13.findAll(itemprop="review")

reviews_bbq_13 = []
for div in divs:
    reviews_bbq_13.append(div.find('p').text)

bbq14 = requests.get('https://www.yelp.com/biz/xin-jiang-bbq-houston?osq=BBQ&start=20&sort_by=date_desc')
bbq14.status_code
bbq14.text
soup_bbq14 = BeautifulSoup(bbq14.text, "html.parser")
divs = soup_bbq14.findAll(itemprop="review")

reviews_bbq_14 = []
for div in divs:
    reviews_bbq_14.append(div.find('p').text)

bbq15 = requests.get('https://www.yelp.com/biz/xin-jiang-bbq-houston?osq=BBQ&start=40&sort_by=date_desc')
bbq15.status_code
bbq15.text
soup_bbq15 = BeautifulSoup(bbq15.text, "html.parser")
divs = soup_bbq15.findAll(itemprop="review")

reviews_bbq_15 = []
for div in divs:
    reviews_bbq_15.append(div.find('p').text)
    
xin_bbq = reviews_bbq_13 + reviews_bbq_14 + reviews_bbq_15
len(xin_bbq)

bbq_rest = jimee + fain + hitbbq + two_bro + xin_bbq
bbq_rest = [x.lower() for x in bbq_rest] # lower all words
for review in bbq_rest:
    print(review, "\n")
len(bbq_rest)

############################################################################################################### 
# Japanese Restaurants

# Hokkaido Japanese Restaurant
jap1 = requests.get('https://www.yelp.com/biz/hokkaido-japanese-restaurant-houston?osq=Japanese%20Food&sort_by=date_desc')
jap1.status_code
jap1.text
soup_jap1 = BeautifulSoup(jap1.text, "html.parser")
divs = soup_jap1.findAll(itemprop="review")

reviews_jap_1 = []
for div in divs:
    reviews_jap_1.append(div.find('p').text)

jap2 = requests.get('https://www.yelp.com/biz/hokkaido-japanese-restaurant-houston?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap2.status_code
jap2.text
soup_jap2 = BeautifulSoup(jap2.text, "html.parser")
divs = soup_jap2.findAll(itemprop="review")

reviews_jap_2 = []
for div in divs:
    reviews_jap_2.append(div.find('p').text)

jap3 = requests.get('https://www.yelp.com/biz/hokkaido-japanese-restaurant-houston?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap3.status_code
jap3.text
soup_jap3 = BeautifulSoup(jap3.text, "html.parser")
divs = soup_jap3.findAll(itemprop="review")

reviews_jap_3 = []
for div in divs:
    reviews_jap_3.append(div.find('p').text)

hokk = reviews_jap_1 + reviews_jap_2 + reviews_jap_3
len(hokk)

# Katsu Bar and Noodle
jap4 = requests.get('https://www.yelp.com/biz/katsu-bar-and-noodle-houston-4?osq=Japanese%20Food&sort_by=date_desc')
jap4.status_code
jap4.text
soup_jap4 = BeautifulSoup(jap4.text, "html.parser")
divs = soup_jap4.findAll(itemprop="review")

reviews_jap_4 = []
for div in divs:
    reviews_jap_4.append(div.find('p').text)

jap5 = requests.get('https://www.yelp.com/biz/katsu-bar-and-noodle-houston-4?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap5.status_code
jap5.text
soup_jap5 = BeautifulSoup(jap5.text, "html.parser")
divs = soup_jap5.findAll(itemprop="review")

reviews_jap_5 = []
for div in divs:
    reviews_jap_5.append(div.find('p').text)

jap6 = requests.get('https://www.yelp.com/biz/katsu-bar-and-noodle-houston-4?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap6.status_code
jap6.text
soup_jap6 = BeautifulSoup(jap6.text, "html.parser")
divs = soup_jap6.findAll(itemprop="review")

reviews_jap_6 = []
for div in divs:
    reviews_jap_6.append(div.find('p').text)
    
Katsub = reviews_jap_4 + reviews_jap_5 + reviews_jap_6 
len(Katsub)

# Jin Bento
jap7 = requests.get('https://www.yelp.com/biz/jin-bento-houston-3?osq=Japanese%20Food&sort_by=date_desc')
jap7.status_code
jap7.text
soup_jap7 = BeautifulSoup(jap7.text, "html.parser")
divs = soup_jap7.findAll(itemprop="review")

reviews_jap_7 = []
for div in divs:
    reviews_jap_7.append(div.find('p').text)

jap8 = requests.get('https://www.yelp.com/biz/jin-bento-houston-3?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap8.status_code
jap8.text
soup_jap8 = BeautifulSoup(jap8.text, "html.parser")
divs = soup_jap8.findAll(itemprop="review")

reviews_jap_8 = []
for div in divs:
    reviews_jap_8.append(div.find('p').text)
    
jinb = reviews_jap_7 + reviews_jap_8 
len(jinb)

# Genji Japanese Restaurant & Karaoke Bar
jap10 = requests.get('https://www.yelp.com/biz/genji-japanese-restaurant-and-karaoke-bar-houston-3?osq=Japanese%20Food&sort_by=date_desc')
jap10.status_code
jap10.text
soup_jap10 = BeautifulSoup(jap10.text, "html.parser")
divs = soup_jap10.findAll(itemprop="review")

reviews_jap_10 = []
for div in divs:
    reviews_jap_10.append(div.find('p').text)

jap11 = requests.get('https://www.yelp.com/biz/genji-japanese-restaurant-and-karaoke-bar-houston-3?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap11.status_code
jap11.text
soup_jap11 = BeautifulSoup(jap11.text, "html.parser")
divs = soup_jap11.findAll(itemprop="review")

reviews_jap_11 = []
for div in divs:
    reviews_jap_11.append(div.find('p').text)

jap12 = requests.get('https://www.yelp.com/biz/genji-japanese-restaurant-and-karaoke-bar-houston-3?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap12.status_code
jap12.text
soup_jap12 = BeautifulSoup(jap12.text, "html.parser")
divs = soup_jap12.findAll(itemprop="review")

reviews_jap_12 = []
for div in divs:
    reviews_jap_12.append(div.find('p').text)

gen_ji = reviews_jap_10 + reviews_jap_11 + reviews_jap_12

# Napa Udon House and Wine Bar
jap13 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&sort_by=date_desc')
jap13.status_code
jap13.text
soup_jap13 = BeautifulSoup(jap13.text, "html.parser")
divs = soup_jap13.findAll(itemprop="review")

reviews_jap_13 = []
for div in divs:
    reviews_jap_13.append(div.find('p').text)

jap14 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap14.status_code
jap14.text
soup_jap14 = BeautifulSoup(jap14.text, "html.parser")
divs = soup_jap14.findAll(itemprop="review")

reviews_jap_14 = []
for div in divs:
    reviews_jap_14.append(div.find('p').text)

jap15 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap15.status_code
jap15.text
soup_jap15 = BeautifulSoup(jap15.text, "html.parser")
divs = soup_jap15.findAll(itemprop="review")

reviews_jap_15 = []
for div in divs:
    reviews_jap_15.append(div.find('p').text)
    
napau = reviews_jap_13 + reviews_jap_14 + reviews_jap_15

jap_rest = hokk + jinb + Katsub + gen_ji + napau
jap_rest = [x.lower() for x in jap_rest] # lower all words
for review in jap_rest:
    print(review, "\n")
len(jap_rest)

############################################################################################################### 
# Korean Restaurants

# Kimchi's Korean Cafe
kor1 = requests.get('https://www.yelp.com/biz/kimchis-korean-cafe-houston?osq=korean&sort_by=date_desc')
kor1.status_code
kor1.text
soup_kor1 = BeautifulSoup(kor1.text, "html.parser")
divs = soup_kor1.findAll(itemprop="review")

reviews_kor_1 = []
for div in divs:
    reviews_kor_1.append(div.find('p').text)

kor2 = requests.get('https://www.yelp.com/biz/kimchis-korean-cafe-houston?osq=korean&start=20&sort_by=date_desc')
kor2.status_code
kor2.text
soup_kor2 = BeautifulSoup(kor2.text, "html.parser")
divs = soup_kor2.findAll(itemprop="review")

reviews_kor_2 = []
for div in divs:
    reviews_kor_2.append(div.find('p').text)

kor3 = requests.get('https://www.yelp.com/biz/kimchis-korean-cafe-houston?osq=korean&start=40&sort_by=date_desc')
kor3.status_code
kor3.text
soup_kor3 = BeautifulSoup(kor3.text, "html.parser")
divs = soup_kor3.findAll(itemprop="review")

reviews_kor_3 = []
for div in divs:
    reviews_kor_3.append(div.find('p').text)

kimkcaf = reviews_kor_1 + reviews_kor_2 + reviews_kor_3

# Chimac
kor4 = requests.get('https://www.yelp.com/biz/chimac-houston?osq=korean&sort_by=date_desc')
kor4.status_code
kor4.text
soup_kor4 = BeautifulSoup(kor4.text, "html.parser")
divs = soup_kor4.findAll(itemprop="review")

reviews_kor_4 = []
for div in divs:
    reviews_kor_4.append(div.find('p').text)

kor5 = requests.get('https://www.yelp.com/biz/chimac-houston?osq=korean&start=20&sort_by=date_desc')
kor5.status_code
kor5.text
soup_kor5 = BeautifulSoup(kor5.text, "html.parser")
divs = soup_kor5.findAll(itemprop="review")

reviews_kor_5 = []
for div in divs:
    reviews_kor_5.append(div.find('p').text)

kor6 = requests.get('https://www.yelp.com/biz/chimac-houston?osq=korean&start=40&sort_by=date_desc')
kor6.status_code
kor6.text
soup_kor6 = BeautifulSoup(kor6.text, "html.parser")
divs = soup_kor6.findAll(itemprop="review")

reviews_kor_6 = []
for div in divs:
    reviews_kor_6.append(div.find('p').text)

chim = reviews_kor_4 + reviews_kor_5 + reviews_kor_6

# Paik's Noodle
kor7 = requests.get('https://www.yelp.com/biz/paiks-noodle-houston-4?osq=korean&sort_by=date_desc')
kor7.status_code
kor7.text
soup_kor7 = BeautifulSoup(kor7.text, "html.parser")
divs = soup_kor7.findAll(itemprop="review")

reviews_kor_7 = []
for div in divs:
    reviews_kor_7.append(div.find('p').text)

kor8 = requests.get('https://www.yelp.com/biz/paiks-noodle-houston-4?osq=korean&start=20&sort_by=date_desc')
kor8.status_code
kor8.text
soup_kor8 = BeautifulSoup(kor8.text, "html.parser")
divs = soup_kor8.findAll(itemprop="review")

reviews_kor_8 = []
for div in divs:
    reviews_kor_8.append(div.find('p').text)

kor9 = requests.get('https://www.yelp.com/biz/paiks-noodle-houston-4?osq=korean&start=40&sort_by=date_desc')
kor9.status_code
kor9.text
soup_kor9 = BeautifulSoup(kor9.text, "html.parser")
divs = soup_kor9.findAll(itemprop="review")

reviews_kor_9 = []
for div in divs:
    reviews_kor_9.append(div.find('p').text)

paik = reviews_kor_7 + reviews_kor_8 + reviews_kor_9

# Go Hyang Jib Korean Restaurant
kor10 = requests.get('https://www.yelp.com/biz/go-hyang-jib-korean-restaurant-houston?osq=korean&sort_by=date_desc')
kor10.status_code
kor10.text
soup_kor10 = BeautifulSoup(kor10.text, "html.parser")
divs = soup_kor10.findAll(itemprop="review")

reviews_kor_10 = []
for div in divs:
    reviews_kor_10.append(div.find('p').text)

kor11 = requests.get('https://www.yelp.com/biz/go-hyang-jib-korean-restaurant-houston?osq=korean&start=20&sort_by=date_desc')
kor11.status_code
kor11.text
soup_kor11 = BeautifulSoup(kor11.text, "html.parser")
divs = soup_kor11.findAll(itemprop="review")

reviews_kor_11 = []
for div in divs:
    reviews_kor_11.append(div.find('p').text)

kor12 = requests.get('https://www.yelp.com/biz/go-hyang-jib-korean-restaurant-houston?osq=korean&start=40&sort_by=date_desc')
kor12.status_code
kor12.text
soup_kor12 = BeautifulSoup(kor12.text, "html.parser")
divs = soup_kor12.findAll(itemprop="review")

reviews_kor_12 = []
for div in divs:
    reviews_kor_12.append(div.find('p').text)

gohy = reviews_kor_10 + reviews_kor_11 + reviews_kor_12

# BiBiJo Express
kor13 = requests.get('https://www.yelp.com/biz/bibijo-express-houston?osq=korean&sort_by=date_desc')
kor13.status_code
kor13.text
soup_kor13 = BeautifulSoup(kor13.text, "html.parser")
divs = soup_kor13.findAll(itemprop="review")

reviews_kor_13 = []
for div in divs:
    reviews_kor_13.append(div.find('p').text)

kor14 = requests.get('https://www.yelp.com/biz/bibijo-express-houston?osq=korean&start=20&sort_by=date_desc')
kor14.status_code
kor14.text
soup_kor14 = BeautifulSoup(kor14.text, "html.parser")
divs = soup_kor14.findAll(itemprop="review")

reviews_kor_14 = []
for div in divs:
    reviews_kor_14.append(div.find('p').text)

kor15 = requests.get('https://www.yelp.com/biz/bibijo-express-houston?osq=korean&start=40&sort_by=date_desc')
kor15.status_code
kor15.text
soup_kor15 = BeautifulSoup(kor15.text, "html.parser")
divs = soup_kor15.findAll(itemprop="review")

reviews_kor_15 = []
for div in divs:
    reviews_kor_15.append(div.find('p').text)
    
bibi_jo = reviews_kor_13 + reviews_kor_14 + reviews_kor_15

kor_rest = kimkcaf + chim + paik + gohy + bibi_jo
kor_rest = [x.lower() for x in kor_rest] # lower all words
for review in kor_rest:
    print(review, "\n")
len(kor_rest)
    
############################################################################################################### 
# Pizza Restaurants

# Frank's Pizza
piz1 = requests.get('https://www.yelp.com/biz/franks-pizza-houston?osq=Pizza&sort_by=date_desc')
piz1.status_code
piz1.text
soup_piz1 = BeautifulSoup(piz1.text, "html.parser")
divs = soup_piz1.findAll(itemprop="review")

reviews_piz_1 = []
for div in divs:
    reviews_piz_1.append(div.find('p').text)

piz2 = requests.get('https://www.yelp.com/biz/franks-pizza-houston?osq=Pizza&start=20&sort_by=date_desc')
piz2.status_code
piz2.text
soup_piz2 = BeautifulSoup(piz2.text, "html.parser")
divs = soup_piz2.findAll(itemprop="review")

reviews_piz_2 = []
for div in divs:
    reviews_piz_2.append(div.find('p').text)

piz3 = requests.get('https://www.yelp.com/biz/franks-pizza-houston?osq=Pizza&start=40&sort_by=date_desc')
piz3.status_code
piz3.text
soup_piz3 = BeautifulSoup(piz3.text, "html.parser")
divs = soup_piz3.findAll(itemprop="review")

reviews_piz_3 = []
for div in divs:
    reviews_piz_3.append(div.find('p').text)

frapiz = reviews_piz_1 + reviews_piz_2 + reviews_piz_3

# Pepperoni's - Montrose
piz4 = requests.get('https://www.yelp.com/biz/pepperonis-montrose-houston?osq=Pizza&sort_by=date_desc')
piz4.status_code
piz4.text
soup_piz4 = BeautifulSoup(piz4.text, "html.parser")
divs = soup_piz4.findAll(itemprop="review")

reviews_piz_4 = []
for div in divs:
    reviews_piz_4.append(div.find('p').text)

piz5 = requests.get('https://www.yelp.com/biz/pepperonis-montrose-houston?osq=Pizza&start=20&sort_by=date_desc')
piz5.status_code
piz5.text
soup_piz5 = BeautifulSoup(piz5.text, "html.parser")
divs = soup_piz5.findAll(itemprop="review")

reviews_piz_5 = []
for div in divs:
    reviews_piz_5.append(div.find('p').text)

piz6 = requests.get('https://www.yelp.com/biz/pepperonis-montrose-houston?osq=Pizza&start=40&sort_by=date_desc')
piz6.status_code
piz6.text
soup_piz6 = BeautifulSoup(piz6.text, "html.parser")
divs = soup_piz6.findAll(itemprop="review")

reviews_piz_6 = []
for div in divs:
    reviews_piz_6.append(div.find('p').text)

pepper_mont = reviews_piz_4 + reviews_piz_5 + reviews_piz_6

# Brother's Pizzeria
piz7 = requests.get('https://www.yelp.com/biz/brothers-pizzeria-houston-2?osq=Pizza&sort_by=date_desc')
piz7.status_code
piz7.text
soup_piz7 = BeautifulSoup(piz7.text, "html.parser")
divs = soup_piz7.findAll(itemprop="review")

reviews_piz_7 = []
for div in divs:
    reviews_piz_7.append(div.find('p').text)

piz8 = requests.get('https://www.yelp.com/biz/brothers-pizzeria-houston-2?osq=Pizza&start=20&sort_by=date_desc')
piz8.status_code
piz8.text
soup_piz8 = BeautifulSoup(piz8.text, "html.parser")
divs = soup_piz8.findAll(itemprop="review")

reviews_piz_8 = []
for div in divs:
    reviews_piz_8.append(div.find('p').text)

piz9 = requests.get('https://www.yelp.com/biz/brothers-pizzeria-houston-2?osq=Pizza&start=40&sort_by=date_desc')
piz9.status_code
piz9.text
soup_piz9 = BeautifulSoup(piz9.text, "html.parser")
divs = soup_piz9.findAll(itemprop="review")

reviews_piz_9 = []
for div in divs:
    reviews_piz_9.append(div.find('p').text)

bro_piz = reviews_piz_7 + reviews_piz_8 + reviews_piz_9

# Your Pie
piz10 = requests.get('https://www.yelp.com/biz/your-pie-houston?osq=Pizza&sort_by=date_desc')
piz10.status_code
piz10.text
soup_piz10 = BeautifulSoup(piz10.text, "html.parser")
divs = soup_piz10.findAll(itemprop="review")

reviews_piz_10 = []
for div in divs:
    reviews_piz_10.append(div.find('p').text)

piz11 = requests.get('https://www.yelp.com/biz/your-pie-houston?osq=Pizza&start=20&sort_by=date_desc')
piz11.status_code
piz11.text
soup_piz11 = BeautifulSoup(piz11.text, "html.parser")
divs = soup_piz11.findAll(itemprop="review")

reviews_piz_11 = []
for div in divs:
    reviews_piz_11.append(div.find('p').text)

piz12 = requests.get('https://www.yelp.com/biz/your-pie-houston?osq=Pizza&start=40&sort_by=date_desc')
piz12.status_code
piz12.text
soup_piz12 = BeautifulSoup(piz12.text, "html.parser")
divs = soup_piz12.findAll(itemprop="review")

reviews_piz_12 = []
for div in divs:
    reviews_piz_12.append(div.find('p').text)

your_pie = reviews_piz_10 + reviews_piz_11 + reviews_piz_12

# Empire Pizza
piz13 = requests.get('https://www.yelp.com/biz/empire-pizza-houston?osq=Pizza&sort_by=date_desc')
piz13.status_code
piz13.text
soup_piz13 = BeautifulSoup(piz13.text, "html.parser")
divs = soup_piz13.findAll(itemprop="review")

reviews_piz_13 = []
for div in divs:
    reviews_piz_13.append(div.find('p').text)

piz14 = requests.get('https://www.yelp.com/biz/empire-pizza-houston?osq=Pizza&start=20&sort_by=date_desc')
piz14.status_code
piz14.text
soup_piz14 = BeautifulSoup(piz14.text, "html.parser")
divs = soup_piz14.findAll(itemprop="review")

reviews_piz_14 = []
for div in divs:
    reviews_piz_14.append(div.find('p').text)

piz15 = requests.get('https://www.yelp.com/biz/empire-pizza-houston?osq=Pizza&start=40&sort_by=date_desc')
piz15.status_code
piz15.text
soup_piz15 = BeautifulSoup(piz15.text, "html.parser")
divs = soup_piz15.findAll(itemprop="review")

reviews_piz_15 = []
for div in divs:
    reviews_piz_15.append(div.find('p').text)
    
emp_piz = reviews_piz_13 + reviews_piz_14 + reviews_piz_15

piz_rest = frapiz + pepper_mont + bro_piz + your_pie + emp_piz
piz_rest = [x.lower() for x in piz_rest] # lower all words
for review in piz_rest:
    print(review, "\n")
len(piz_rest)

############################################################################################################### 
# Buffett Restaurants

# Fonda Santa Rosa
buff1 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Buffets&sort_by=date_desc')
buff1.status_code
buff1.text
soup_buff1 = BeautifulSoup(buff1.text, "html.parser")
divs = soup_buff1.findAll(itemprop="review")

reviews_buff_1 = []
for div in divs:
    reviews_buff_1.append(div.find('p').text)

buff2 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Buffets&start=20&sort_by=date_desc')
buff2.status_code
buff2.text
soup_buff2 = BeautifulSoup(buff2.text, "html.parser")
divs = soup_buff2.findAll(itemprop="review")

reviews_buff_2 = []
for div in divs:
    reviews_buff_2.append(div.find('p').text)

buff3 = requests.get('https://www.yelp.com/biz/fonda-santa-rosa-houston-3?osq=Buffets&start=40&sort_by=date_desc')
buff3.status_code
buff3.text
soup_buff3 = BeautifulSoup(buff3.text, "html.parser")
divs = soup_buff3.findAll(itemprop="review")

reviews_buff_3 = []
for div in divs:
    reviews_buff_3.append(div.find('p').text)

fonda_buff = reviews_buff_1 + reviews_buff_2 + reviews_buff_3

# Cocina Latina Pupusa Buffet
buff4 = requests.get('https://www.yelp.com/biz/cocina-latina-pupusa-buffet-houston-5?osq=Buffets&sort_by=date_desc')
buff4.status_code
buff4.text
soup_buff4 = BeautifulSoup(buff4.text, "html.parser")
divs = soup_buff4.findAll(itemprop="review")

reviews_buff_4 = []
for div in divs:
    reviews_buff_4.append(div.find('p').text)

cocina = reviews_buff_4

# Pancho's Mexican Buffet
buff7 = requests.get('https://www.yelp.com/biz/panchos-mexican-buffet-houston-4?osq=Buffets&sort_by=date_desc')
buff7.status_code
buff7.text
soup_buff7 = BeautifulSoup(buff7.text, "html.parser")
divs = soup_buff7.findAll(itemprop="review")

reviews_buff_7 = []
for div in divs:
    reviews_buff_7.append(div.find('p').text)

buff8 = requests.get('https://www.yelp.com/biz/panchos-mexican-buffet-houston-4?osq=Buffets&start=20&sort_by=date_desc')
buff8.status_code
buff8.text
soup_buff8 = BeautifulSoup(buff8.text, "html.parser")
divs = soup_buff8.findAll(itemprop="review")

reviews_buff_8 = []
for div in divs:
    reviews_buff_8.append(div.find('p').text)

buff9 = requests.get('https://www.yelp.com/biz/panchos-mexican-buffet-houston-4?osq=Buffets&start=40&sort_by=date_desc')
buff9.status_code
buff9.text
soup_buff9 = BeautifulSoup(buff9.text, "html.parser")
divs = soup_buff9.findAll(itemprop="review")

reviews_buff_9 = []
for div in divs:
    reviews_buff_9.append(div.find('p').text)

pancho_buff = reviews_buff_7 + reviews_buff_8 + reviews_buff_9

# Best of Filipiniana
buff10 = requests.get('https://www.yelp.com/biz/best-of-filipiniana-houston-2?osq=Buffets&sort_by=date_desc')
buff10.status_code
buff10.text
soup_buff10 = BeautifulSoup(buff10.text, "html.parser")
divs = soup_buff10.findAll(itemprop="review")

reviews_buff_10 = []
for div in divs:
    reviews_buff_10.append(div.find('p').text)

buff11 = requests.get('https://www.yelp.com/biz/best-of-filipiniana-houston-2?osq=Buffets&start=20&sort_by=date_desc')
buff11.status_code
buff11.text
soup_buff11 = BeautifulSoup(buff11.text, "html.parser")
divs = soup_buff11.findAll(itemprop="review")

reviews_buff_11 = []
for div in divs:
    reviews_buff_11.append(div.find('p').text)

buff12 = requests.get('https://www.yelp.com/biz/best-of-filipiniana-houston-2?osq=Buffets&start=40&sort_by=date_desc')
buff12.status_code
buff12.text
soup_buff12 = BeautifulSoup(buff12.text, "html.parser")
divs = soup_buff12.findAll(itemprop="review")

reviews_buff_12 = []
for div in divs:
    reviews_buff_12.append(div.find('p').text)

fillip = reviews_buff_10 + reviews_buff_11 + reviews_buff_12

# Hong Kong City Buffet
buff13 = requests.get('https://www.yelp.com/biz/hong-kong-city-buffet-houston?osq=Buffets&sort_by=date_desc')
buff13.status_code
buff13.text
soup_buff13 = BeautifulSoup(buff13.text, "html.parser")
divs = soup_buff13.findAll(itemprop="review")

reviews_buff_13 = []
for div in divs:
    reviews_buff_13.append(div.find('p').text)

buff14 = requests.get('https://www.yelp.com/biz/hong-kong-city-buffet-houston?osq=Buffets&start=20&sort_by=date_desc')
buff14.status_code
buff14.text
soup_buff14 = BeautifulSoup(buff14.text, "html.parser")
divs = soup_buff14.findAll(itemprop="review")

reviews_buff_14 = []
for div in divs:
    reviews_buff_14.append(div.find('p').text)

emp_buff = reviews_buff_13 + reviews_buff_14

buff_rest = fonda_buff + cocina + pancho_buff + fillip + emp_buff
buff_rest = [x.lower() for x in buff_rest] # lower all words
for review in buff_rest:
    print(review, "\n")
len(buff_rest)

############################################################################################################### 
# Indian Restaurants

# Tarka Indian Kitchen
ind1 = requests.get('https://www.yelp.com/biz/tarka-indian-kitchen-houston?osq=Indian%20Food&sort_by=date_desc')
ind1.status_code
ind1.text
soup_ind1 = BeautifulSoup(ind1.text, "html.parser")
divs = soup_ind1.findAll(itemprop="review")

reviews_ind_1 = []
for div in divs:
    reviews_ind_1.append(div.find('p').text)

ind2 = requests.get('https://www.yelp.com/biz/tarka-indian-kitchen-houston?osq=Indian%20Food&start=20&sort_by=date_desc')
ind2.status_code
ind2.text
soup_ind2 = BeautifulSoup(ind2.text, "html.parser")
divs = soup_ind2.findAll(itemprop="review")

reviews_ind_2 = []
for div in divs:
    reviews_ind_2.append(div.find('p').text)

ind3 = requests.get('https://www.yelp.com/biz/tarka-indian-kitchen-houston?osq=Indian%20Food&start=40&sort_by=date_desc')
ind3.status_code
ind3.text
soup_ind3 = BeautifulSoup(ind3.text, "html.parser")
divs = soup_ind3.findAll(itemprop="review")

reviews_ind_3 = []
for div in divs:
    reviews_ind_3.append(div.find('p').text)

tarka = reviews_ind_1 + reviews_ind_2 + reviews_ind_3

# Flying Idlis
ind4 = requests.get('https://www.yelp.com/biz/flying-idlis-houston-2?osq=Indian%20Food&sort_by=date_desc')
ind4.status_code
ind4.text
soup_ind4 = BeautifulSoup(ind4.text, "html.parser")
divs = soup_ind4.findAll(itemprop="review")

reviews_ind_4 = []
for div in divs:
    reviews_ind_4.append(div.find('p').text)
    
ind5 = requests.get('https://www.yelp.com/biz/flying-idlis-houston-2?osq=Indian%20Food&start=20&sort_by=date_desc')
ind5.status_code
ind5.text
soup_ind5 = BeautifulSoup(ind5.text, "html.parser")
divs = soup_ind5.findAll(itemprop="review")

reviews_ind_5 = []
for div in divs:
    reviews_ind_5.append(div.find('p').text)
    
ind6 = requests.get('https://www.yelp.com/biz/flying-idlis-houston-2?osq=Indian%20Food&start=40&sort_by=date_desc')
ind6.status_code
ind6.text
soup_ind6 = BeautifulSoup(ind6.text, "html.parser")
divs = soup_ind6.findAll(itemprop="review")

reviews_ind_6 = []
for div in divs:
    reviews_ind_6.append(div.find('p').text)

flying = reviews_ind_4 + reviews_ind_5 + reviews_ind_6

# Shri Balaji Bhavan
ind7 = requests.get('https://www.yelp.com/biz/shri-balaji-bhavan-houston?osq=Indian%20Food&sort_by=date_desc')
ind7.status_code
ind7.text
soup_ind7 = BeautifulSoup(ind7.text, "html.parser")
divs = soup_ind7.findAll(itemprop="review")

reviews_ind_7 = []
for div in divs:
    reviews_ind_7.append(div.find('p').text)

ind8 = requests.get('https://www.yelp.com/biz/shri-balaji-bhavan-houston?osq=Indian%20Food&start=20&sort_by=date_desc')
ind8.status_code
ind8.text
soup_ind8 = BeautifulSoup(ind8.text, "html.parser")
divs = soup_ind8.findAll(itemprop="review")

reviews_ind_8 = []
for div in divs:
    reviews_ind_8.append(div.find('p').text)

ind9 = requests.get('https://www.yelp.com/biz/shri-balaji-bhavan-houston?osq=Indian%20Food&start=40&sort_by=date_desc')
ind9.status_code
ind9.text
soup_ind9 = BeautifulSoup(ind9.text, "html.parser")
divs = soup_ind9.findAll(itemprop="review")

reviews_ind_9 = []
for div in divs:
    reviews_ind_9.append(div.find('p').text)

shri = reviews_ind_7 + reviews_ind_8 + reviews_ind_9

# Shiv Sagar
ind10 = requests.get('https://www.yelp.com/biz/shiv-sagar-houston?osq=Indian%20Food&sort_by=date_desc')
ind10.status_code
ind10.text
soup_ind10 = BeautifulSoup(ind10.text, "html.parser")
divs = soup_ind10.findAll(itemprop="review")

reviews_ind_10 = []
for div in divs:
    reviews_ind_10.append(div.find('p').text)

ind11 = requests.get('https://www.yelp.com/biz/shiv-sagar-houston?osq=Indian%20Food&start=20&sort_by=date_desc')
ind11.status_code
ind11.text
soup_ind11 = BeautifulSoup(ind11.text, "html.parser")
divs = soup_ind11.findAll(itemprop="review")

reviews_ind_11 = []
for div in divs:
    reviews_ind_11.append(div.find('p').text)

ind12 = requests.get('https://www.yelp.com/biz/shiv-sagar-houston?osq=Indian%20Food&start=40&sort_by=date_desc')
ind12.status_code
ind12.text
soup_ind12 = BeautifulSoup(ind12.text, "html.parser")
divs = soup_ind12.findAll(itemprop="review")

reviews_ind_12 = []
for div in divs:
    reviews_ind_12.append(div.find('p').text)

shiv = reviews_ind_10 + reviews_ind_11 + reviews_ind_12

# Deli Deluxe
ind13 = requests.get('https://www.yelp.com/biz/deli-deluxe-houston-2?osq=Indian%20Food&sort_by=date_desc')
ind13.status_code
ind13.text
soup_ind13 = BeautifulSoup(ind13.text, "html.parser")
divs = soup_ind13.findAll(itemprop="review")

reviews_ind_13 = []
for div in divs:
    reviews_ind_13.append(div.find('p').text)

ind14 = requests.get('https://www.yelp.com/biz/deli-deluxe-houston-2?osq=Indian%20Food&start=20&sort_by=date_desc')
ind14.status_code
ind14.text
soup_ind14 = BeautifulSoup(ind14.text, "html.parser")
divs = soup_ind14.findAll(itemprop="review")

reviews_ind_14 = []
for div in divs:
    reviews_ind_14.append(div.find('p').text)
    
ind15 = requests.get('https://www.yelp.com/biz/deli-deluxe-houston-2?osq=Indian%20Food&start=40&sort_by=date_desc')
ind15.status_code
ind15.text
soup_ind15 = BeautifulSoup(ind15.text, "html.parser")
divs = soup_ind15.findAll(itemprop="review")

reviews_ind_15 = []
for div in divs:
    reviews_ind_15.append(div.find('p').text)

deli = reviews_ind_13 + reviews_ind_14 + reviews_ind_15

ind_rest = tarka + flying + shri + shiv + deli
ind_rest = [x.lower() for x in ind_rest] # lower all words
for review in ind_rest:
    print(review, "\n")
len(ind_rest)

############################################################################################################### 
# Steak Restaurants

# Velvet Taco
stk1 = requests.get('https://www.yelp.com/biz/velvet-taco-houston?osq=Steakhouses&sort_by=date_desc')
stk1.status_code
stk1.text
soup_stk1 = BeautifulSoup(stk1.text, "html.parser")
divs = soup_stk1.findAll(itemprop="review")

reviews_stk_1 = []
for div in divs:
    reviews_stk_1.append(div.find('p').text)

stk2 = requests.get('https://www.yelp.com/biz/velvet-taco-houston?osq=Steakhouses&start=20&sort_by=date_desc')
stk2.status_code
stk2.text
soup_stk2 = BeautifulSoup(stk2.text, "html.parser")
divs = soup_stk2.findAll(itemprop="review")

reviews_stk_2 = []
for div in divs:
    reviews_stk_2.append(div.find('p').text)

stk3 = requests.get('https://www.yelp.com/biz/velvet-taco-houston?osq=Steakhouses&start=40&sort_by=date_desc')
stk3.status_code
stk3.text
soup_stk3 = BeautifulSoup(stk3.text, "html.parser")
divs = soup_stk3.findAll(itemprop="review")

reviews_stk_3 = []
for div in divs:
    reviews_stk_3.append(div.find('p').text)

velvtac = reviews_stk_1 + reviews_stk_2 + reviews_stk_3

# T-Bones Sports Pub
stk4 = requests.get('https://www.yelp.com/biz/t-bones-sports-pub-houston?osq=Steakhouses&sort_by=date_desc')
stk4.status_code
stk4.text
soup_stk4 = BeautifulSoup(stk4.text, "html.parser")
divs = soup_stk4.findAll(itemprop="review")

reviews_stk_4 = []
for div in divs:
    reviews_stk_4.append(div.find('p').text)
    
stk5 = requests.get('https://www.yelp.com/biz/t-bones-sports-pub-houston?osq=Steakhouses&start=20&sort_by=date_desc')
stk5.status_code
stk5.text
soup_stk5 = BeautifulSoup(stk5.text, "html.parser")
divs = soup_stk5.findAll(itemprop="review")

reviews_stk_5 = []
for div in divs:
    reviews_stk_5.append(div.find('p').text)
    
stk6 = requests.get('https://www.yelp.com/biz/t-bones-sports-pub-houston?osq=Steakhouses&start=40&sort_by=date_desc')
stk6.status_code
stk6.text
soup_stk6 = BeautifulSoup(stk6.text, "html.parser")
divs = soup_stk6.findAll(itemprop="review")

reviews_stk_6 = []
for div in divs:
    reviews_stk_6.append(div.find('p').text)

tbon_sport = reviews_stk_4 + reviews_stk_5 + reviews_stk_6

# Stanton's City Bites
stk7 = requests.get('https://www.yelp.com/biz/stantons-city-bites-houston?osq=Steakhouses&sort_by=date_desc')
stk7.status_code
stk7.text
soup_stk7 = BeautifulSoup(stk7.text, "html.parser")
divs = soup_stk7.findAll(itemprop="review")

reviews_stk_7 = []
for div in divs:
    reviews_stk_7.append(div.find('p').text)

stk8 = requests.get('https://www.yelp.com/biz/stantons-city-bites-houston?osq=Steakhouses&start=20&sort_by=date_desc')
stk8.status_code
stk8.text
soup_stk8 = BeautifulSoup(stk8.text, "html.parser")
divs = soup_stk8.findAll(itemprop="review")

reviews_stk_8 = []
for div in divs:
    reviews_stk_8.append(div.find('p').text)

stk9 = requests.get('https://www.yelp.com/biz/stantons-city-bites-houston?osq=Steakhouses&start=40&sort_by=date_desc')
stk9.status_code
stk9.text
soup_stk9 = BeautifulSoup(stk9.text, "html.parser")
divs = soup_stk9.findAll(itemprop="review")

reviews_stk_9 = []
for div in divs:
    reviews_stk_9.append(div.find('p').text)

stan_bites = reviews_stk_7 + reviews_stk_8 + reviews_stk_9

# Freddy's Cafe
stk10 = requests.get('https://www.yelp.com/biz/freddys-cafe-houston?osq=Steakhouses&sort_by=date_desc')
stk10.status_code
stk10.text
soup_stk10 = BeautifulSoup(stk10.text, "html.parser")
divs = soup_stk10.findAll(itemprop="review")

reviews_stk_10 = []
for div in divs:
    reviews_stk_10.append(div.find('p').text)

stk11 = requests.get('https://www.yelp.com/biz/freddys-cafe-houston?osq=Steakhouses&start=20&sort_by=date_desc')
stk11.status_code
stk11.text
soup_stk11 = BeautifulSoup(stk11.text, "html.parser")
divs = soup_stk11.findAll(itemprop="review")

reviews_stk_11 = []
for div in divs:
    reviews_stk_11.append(div.find('p').text)

stk12 = requests.get('https://www.yelp.com/biz/freddys-cafe-houston?osq=Steakhouses&start=40&sort_by=date_desc')
stk12.status_code
stk12.text
soup_stk12 = BeautifulSoup(stk12.text, "html.parser")
divs = soup_stk12.findAll(itemprop="review")

reviews_stk_12 = []
for div in divs:
    reviews_stk_12.append(div.find('p').text)

fred = reviews_stk_10 + reviews_stk_11 + reviews_stk_12

# Mesquite Grill & Taco Factory
stk13 = requests.get('https://www.yelp.com/biz/mesquite-grill-and-taco-factory-la-porte?osq=Steakhouses&sort_by=date_desc')
stk13.status_code
stk13.text
soup_stk13 = BeautifulSoup(stk13.text, "html.parser")
divs = soup_stk13.findAll(itemprop="review")

reviews_stk_13 = []
for div in divs:
    reviews_stk_13.append(div.find('p').text)

stk14 = requests.get('https://www.yelp.com/biz/mesquite-grill-and-taco-factory-la-porte?osq=Steakhouses&start=20&sort_by=date_desc')
stk14.status_code
stk14.text
soup_stk14 = BeautifulSoup(stk14.text, "html.parser")
divs = soup_stk14.findAll(itemprop="review")

reviews_stk_14 = []
for div in divs:
    reviews_stk_14.append(div.find('p').text)

mesq = reviews_stk_13 + reviews_stk_14

stk_rest = velvtac + tbon_sport + stan_bites + fred + mesq
stk_rest = [x.lower() for x in stk_rest] # lower all words
for review in stk_rest:
    print(review, "\n")
len(stk_rest)
    
############################################################################################################### 
# Chinese Restaurants

# Siu Lap City
chin1 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&sort_by=date_desc')
chin1.status_code
chin1.text
soup_chin1 = BeautifulSoup(chin1.text, "html.parser")
divs = soup_chin1.findAll(itemprop="review")

reviews_chin_1 = []
for div in divs:
    reviews_chin_1.append(div.find('p').text)

chin2 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin2.status_code
chin2.text
soup_chin2 = BeautifulSoup(chin2.text, "html.parser")
divs = soup_chin2.findAll(itemprop="review")

reviews_chin_2 = []
for div in divs:
    reviews_chin_2.append(div.find('p').text)

chin3 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&start=40&sort_by=date_desc')
chin3.status_code
chin3.text
soup_chin3 = BeautifulSoup(chin3.text, "html.parser")
divs = soup_chin3.findAll(itemprop="review")

reviews_chin_3 = []
for div in divs:
    reviews_chin_3.append(div.find('p').text)

siulap = reviews_chin_1 + reviews_chin_2 + reviews_chin_3

# Golden Wok
chin4 = requests.get('https://www.yelp.com/biz/golden-wok-houston-3?osq=Chinese%20Food&sort_by=date_desc')
chin4.status_code
chin4.text
soup_chin4 = BeautifulSoup(chin4.text, "html.parser")
divs = soup_chin4.findAll(itemprop="review")

reviews_chin_4 = []
for div in divs:
    reviews_chin_4.append(div.find('p').text)
    
chin5 = requests.get('https://www.yelp.com/biz/golden-wok-houston-3?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin5.status_code
chin5.text
soup_chin5 = BeautifulSoup(chin5.text, "html.parser")
divs = soup_chin5.findAll(itemprop="review")

reviews_chin_5 = []
for div in divs:
    reviews_chin_5.append(div.find('p').text)
    
chin6 = requests.get('https://www.yelp.com/biz/golden-wok-houston-3?osq=Chinese%20Food&start=40&sort_by=date_desc')
chin6.status_code
chin6.text
soup_chin6 = BeautifulSoup(chin6.text, "html.parser")
divs = soup_chin6.findAll(itemprop="review")

reviews_chin_6 = []
for div in divs:
    reviews_chin_6.append(div.find('p').text)

gwok = reviews_chin_4 + reviews_chin_5 + reviews_chin_6

# House of Bowls
chin7 = requests.get('https://www.yelp.com/biz/house-of-bowls-houston?osq=Chinese%20Food&sort_by=date_desc')
chin7.status_code
chin7.text
soup_chin7 = BeautifulSoup(chin7.text, "html.parser")
divs = soup_chin7.findAll(itemprop="review")

reviews_chin_7 = []
for div in divs:
    reviews_chin_7.append(div.find('p').text)

chin8 = requests.get('https://www.yelp.com/biz/house-of-bowls-houston?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin8.status_code
chin8.text
soup_chin8 = BeautifulSoup(chin8.text, "html.parser")
divs = soup_chin8.findAll(itemprop="review")

reviews_chin_8 = []
for div in divs:
    reviews_chin_8.append(div.find('p').text)

chin9 = requests.get('https://www.yelp.com/biz/house-of-bowls-houston?osq=Chinese%20Food&start=40&sort_by=date_desc')
chin9.status_code
chin9.text
soup_chin9 = BeautifulSoup(chin9.text, "html.parser")
divs = soup_chin9.findAll(itemprop="review")

reviews_chin_9 = []
for div in divs:
    reviews_chin_9.append(div.find('p').text)

hbowls_bites = reviews_chin_7 + reviews_chin_8 + reviews_chin_9

# P. King Authentic Chinese Food
chin10 = requests.get('https://www.yelp.com/biz/p-king-authentic-chinese-food-bellaire-2?osq=Chinese%20Food&sort_by=date_desc')
chin10.status_code
chin10.text
soup_chin10 = BeautifulSoup(chin10.text, "html.parser")
divs = soup_chin10.findAll(itemprop="review")

reviews_chin_10 = []
for div in divs:
    reviews_chin_10.append(div.find('p').text)

chin11 = requests.get('https://www.yelp.com/biz/p-king-authentic-chinese-food-bellaire-2?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin11.status_code
chin11.text
soup_chin11 = BeautifulSoup(chin11.text, "html.parser")
divs = soup_chin11.findAll(itemprop="review")

reviews_chin_11 = []
for div in divs:
    reviews_chin_11.append(div.find('p').text)

chin12 = requests.get('https://www.yelp.com/biz/p-king-authentic-chinese-food-bellaire-2?osq=Chinese%20Food&start=40&sort_by=date_desc')
chin12.status_code
chin12.text
soup_chin12 = BeautifulSoup(chin12.text, "html.parser")
divs = soup_chin12.findAll(itemprop="review")

reviews_chin_12 = []
for div in divs:
    reviews_chin_12.append(div.find('p').text)

pking = reviews_chin_10 + reviews_chin_11 + reviews_chin_12

# China 101 Express
chin13 = requests.get('https://www.yelp.com/biz/china-101-express-houston?osq=Chinese%20Food&sort_by=date_desc')
chin13.status_code
chin13.text
soup_chin13 = BeautifulSoup(chin13.text, "html.parser")
divs = soup_chin13.findAll(itemprop="review")

reviews_chin_13 = []
for div in divs:
    reviews_chin_13.append(div.find('p').text)

chin14 = requests.get('https://www.yelp.com/biz/china-101-express-houston?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin14.status_code
chin14.text
soup_chin14 = BeautifulSoup(chin14.text, "html.parser")
divs = soup_chin14.findAll(itemprop="review")

reviews_chin_14 = []
for div in divs:
    reviews_chin_14.append(div.find('p').text)
    
express = reviews_chin_13 + reviews_chin_14

chin_rest = siulap + gwok + hbowls_bites + pking + express
chin_rest = [x.lower() for x in chin_rest] # lower all words
for review in chin_rest:
    print(review, "\n")
len(chin_rest)    

############################################################################################################### 
# Thai Restaurants

# Thai Style Fast Food
thai1 = requests.get('https://www.yelp.com/biz/thai-style-fast-food-houston-3?osq=Thai%20Food&sort_by=date_desc')
thai1.status_code
thai1.text
soup_thai1 = BeautifulSoup(thai1.text, "html.parser")
divs = soup_thai1.findAll(itemprop="review")

reviews_thai_1 = []
for div in divs:
    reviews_thai_1.append(div.find('p').text)

thai2 = requests.get('https://www.yelp.com/biz/thai-style-fast-food-houston-3?osq=Thai%20Food&start=20&sort_by=date_desc')
thai2.status_code
thai2.text
soup_thai2 = BeautifulSoup(thai2.text, "html.parser")
divs = soup_thai2.findAll(itemprop="review")

reviews_thai_2 = []
for div in divs:
    reviews_thai_2.append(div.find('p').text)

thai3 = requests.get('https://www.yelp.com/biz/thai-style-fast-food-houston-3?osq=Thai%20Food&start=40&sort_by=date_desc')
thai3.status_code
thai3.text
soup_thai3 = BeautifulSoup(thai3.text, "html.parser")
divs = soup_thai3.findAll(itemprop="review")

reviews_thai_3 = []
for div in divs:
    reviews_thai_3.append(div.find('p').text)

thai_style = reviews_thai_1 + reviews_thai_2 + reviews_thai_3

# Asia Market Thai Lao Food
thai4 = requests.get('https://www.yelp.com/biz/asia-market-thai-lao-food-houston-2?osq=Thai%20Food&sort_by=date_desc')
thai4.status_code
thai4.text
soup_thai4 = BeautifulSoup(thai4.text, "html.parser")
divs = soup_thai4.findAll(itemprop="review")

reviews_thai_4 = []
for div in divs:
    reviews_thai_4.append(div.find('p').text)
    
thai5 = requests.get('https://www.yelp.com/biz/asia-market-thai-lao-food-houston-2?osq=Thai%20Food&sort_by=date_desc')
thai5.status_code
thai5.text
soup_thai5 = BeautifulSoup(thai5.text, "html.parser")
divs = soup_thai5.findAll(itemprop="review")

reviews_thai_5 = []
for div in divs:
    reviews_thai_5.append(div.find('p').text)
    
thai6 = requests.get('https://www.yelp.com/biz/asia-market-thai-lao-food-houston-2?osq=Thai%40Food&sort_by=date_desc')
thai6.status_code
thai6.text
soup_thai6 = BeautifulSoup(thai6.text, "html.parser")
divs = soup_thai6.findAll(itemprop="review")

reviews_thai_6 = []
for div in divs:
    reviews_thai_6.append(div.find('p').text)

asian_markt = reviews_thai_4 + reviews_thai_5 + reviews_thai_6

# Little Thai Cafe
thai7 = requests.get('https://www.yelp.com/biz/little-thai-cafe-houston-3?osq=Thai%20Food&sort_by=date_desc')
thai7.status_code
thai7.text
soup_thai7 = BeautifulSoup(thai7.text, "html.parser")
divs = soup_thai7.findAll(itemprop="review")

reviews_thai_7 = []
for div in divs:
    reviews_thai_7.append(div.find('p').text)

thai8 = requests.get('https://www.yelp.com/biz/little-thai-cafe-houston-3?osq=Thai%20Food&start=20&sort_by=date_desc')
thai8.status_code
thai8.text
soup_thai8 = BeautifulSoup(thai8.text, "html.parser")
divs = soup_thai8.findAll(itemprop="review")

reviews_thai_8 = []
for div in divs:
    reviews_thai_8.append(div.find('p').text)

thai9 = requests.get('https://www.yelp.com/biz/little-thai-cafe-houston-3?osq=Thai%20Food&start=40&sort_by=date_desc')
thai9.status_code
thai9.text
soup_thai9 = BeautifulSoup(thai9.text, "html.parser")
divs = soup_thai9.findAll(itemprop="review")

reviews_thai_9 = []
for div in divs:
    reviews_thai_9.append(div.find('p').text)

little_thai = reviews_thai_7 + reviews_thai_8 + reviews_thai_9

# Thai Jasmine Restaurant
thai10 = requests.get('https://www.yelp.com/biz/thai-jasmine-restaurant-houston?osq=Thai%20Food&sort_by=date_desc')
thai10.status_code
thai10.text
soup_thai10 = BeautifulSoup(thai10.text, "html.parser")
divs = soup_thai10.findAll(itemprop="review")

reviews_thai_10 = []
for div in divs:
    reviews_thai_10.append(div.find('p').text)

thai11 = requests.get('https://www.yelp.com/biz/thai-jasmine-restaurant-houston?osq=Thai%20Food&start=20&sort_by=date_desc')
thai11.status_code
thai11.text
soup_thai11 = BeautifulSoup(thai11.text, "html.parser")
divs = soup_thai11.findAll(itemprop="review")

reviews_thai_11 = []
for div in divs:
    reviews_thai_11.append(div.find('p').text)

thai12 = requests.get('https://www.yelp.com/biz/thai-jasmine-restaurant-houston?osq=Thai%20Food&start=40&sort_by=date_desc')
thai12.status_code
thai12.text
soup_thai12 = BeautifulSoup(thai12.text, "html.parser")
divs = soup_thai12.findAll(itemprop="review")

reviews_thai_12 = []
for div in divs:
    reviews_thai_12.append(div.find('p').text)

thai_jasm = reviews_thai_10 + reviews_thai_11 + reviews_thai_12

# Aim Thai Restaurant
thai13 = requests.get('https://www.yelp.com/biz/aim-thai-restaurant-houston?osq=Thai%20Food&sort_by=date_desc')
thai13.status_code
thai13.text
soup_thai13 = BeautifulSoup(thai13.text, "html.parser")
divs = soup_thai13.findAll(itemprop="review")

reviews_thai_13 = []
for div in divs:
    reviews_thai_13.append(div.find('p').text)

thai14 = requests.get('https://www.yelp.com/biz/aim-thai-restaurant-houston?osq=Thai%20Food&start=20&sort_by=date_desc')
thai14.status_code
thai14.text
soup_thai14 = BeautifulSoup(thai14.text, "html.parser")
divs = soup_thai14.findAll(itemprop="review")

reviews_thai_14 = []
for div in divs:
    reviews_thai_14.append(div.find('p').text)
    
thai15 = requests.get('https://www.yelp.com/biz/aim-thai-restaurant-houston?osq=Thai%20Food&start=20&sort_by=date_desc')
thai15.status_code
thai15.text
soup_thai15 = BeautifulSoup(thai15.text, "html.parser")
divs = soup_thai15.findAll(itemprop="review")

reviews_thai_15 = []
for div in divs:
    reviews_thai_15.append(div.find('p').text)

aim_thai = reviews_thai_13 + reviews_thai_14 + reviews_thai_15

thai_rest = thai_style + asian_markt + little_thai + thai_jasm + aim_thai
thai_rest = [x.lower() for x in thai_rest] # lower all words
for review in thai_rest:
    print(review, "\n")
len(thai_rest)

###################################################################################
# Lets summarize reviews into groups (local variables to global variables)

all_reviews = buff_rest + chin_rest + ind_rest + jap_rest + kor_rest + mex_rest + piz_rest + viet_rest + stk_rest + thai_rest + bbq_rest

mexican = mex_rest
vietnamese = viet_rest
bbq = bbq_rest
japanese = jap_rest
korean = kor_rest
pizza = piz_rest
buffet = buff_rest
indian = ind_rest
steak  = stk_rest
chinese = chin_rest
thai = thai_rest

###################################################################################
# Create data frames / Frequencies are given at the bottom of the code

stop_words = set(stopwords.words('english')) 

# All Restaurants
df_all = pd.DataFrame(np.array(all_reviews), columns=['review'])
df_all['word_count'] = df_all['review'].apply(lambda x: len(str(x).split(" ")))
df_all['stopword_coun'] = df_all['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_all['review_lower'] = df_all['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_all['review_nopunc'] = df_all['review_lower'].str.replace('[^\w\s]', '')
df_all['review_nopunc_nostop'] = df_all['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_all = ["food","place","get","order","one","time","also", "go", "ordered", "rice", "pizza",
                       "restaurant", "ive"]
df_all['review_nopunc_nostop_nocommon'] = df_all['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_all)))
freq_all = pd.Series(" ".join(df_all['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_all)

# Mexican Restaurant
df_mex = pd.DataFrame(np.array(mexican), columns=['review'])
df_mex['word_count'] = df_mex['review'].apply(lambda x: len(str(x).split(" ")))
df_mex['stopword_coun'] = df_mex['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_mex['review_lower'] = df_mex['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_mex['review_nopunc'] = df_mex['review_lower'].str.replace('[^\w\s]', '')
df_mex['review_nopunc_nostop'] = df_mex['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_mex = ['food', 'place', 'one', 'torta', 'tortas', 'got', 'ordered', 'salsa', 'would', 'im', 'get', 'restaurant', 'dont','tacos','mexican','meat',
                       'order','ordered','breakfast','really','also','de','houston','time','well','us','go','come','recommend','little','taco','coming','eat',
                       'tortillas','always','try']
df_mex['review_nopunc_nostop_nocommon'] = df_mex['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_mex)))
freq_mex= pd.Series(" ".join(df_mex['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_mex)

# Vietnamese Restaurant
df_viet = pd.DataFrame(np.array(vietnamese), columns=['review'])
df_viet['word_count'] = df_viet['review'].apply(lambda x: len(str(x).split(" ")))
df_viet['stopword_coun'] = df_viet['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_viet['review_lower'] = df_viet['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_viet['review_nopunc'] = df_viet['review_lower'].str.replace('[^\w\s]', '')
df_viet['review_nopunc_nostop'] = df_viet['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_viet = ['food', 'place', 'banh', 'rice', 'pho', 'got', 'ordered', 'mi','pork','sauce','noodle','vietnamese',
                        'rolls','soup','spring','bahn','meat','would', 'im', 'get', 'restaurant', 'dont', 'ive', 'came', 'noodles','sandwich', 'broth',
                        'order','ordered','go','one','houston','try','spicy','menu','dish','dishes','korean','fried','beo']
df_viet['review_nopunc_nostop_nocommon'] = df_viet['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_viet)))
freq_viet = pd.Series(" ".join(df_viet['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_viet)

# BBQ Restaurant
df_bbq = pd.DataFrame(np.array(bbq), columns=['review'])
df_bbq['word_count'] = df_bbq['review'].apply(lambda x: len(str(x).split(" ")))
df_bbq['stopword_coun'] = df_bbq['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_bbq['review_lower'] = df_bbq['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_bbq['review_nopunc'] = df_bbq['review_lower'].str.replace('[^\w\s]', '')
df_bbq['review_nopunc_nostop'] = df_bbq['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_bbq = ['food', 'place', 'one', 'bbq', 'got', 'ordered',  'would', 'im', 'get', 'restaurant', 'dont', 'brisket', 'skewers','beef','lamb','sauce',
                       'meat','ribs','potato','chicken','pork','ive','also','beans','sandwich', 'sausage', 'plate','eat','tender','order','ordered',
                       'salad','time','try','come','go','little']
df_bbq['review_nopunc_nostop_nocommon'] = df_bbq['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_bbq)))
freq_bbq = pd.Series(" ".join(df_bbq['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_bbq)

# Japanese Restaurant
df_jap = pd.DataFrame(np.array(japanese), columns=['review'])
df_jap['word_count'] = df_jap['review'].apply(lambda x: len(str(x).split(" ")))
df_jap['stopword_coun'] = df_jap['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_jap['review_lower'] = df_jap['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_jap['review_nopunc'] = df_jap['review_lower'].str.replace('[^\w\s]', '')
df_jap['review_nopunc_nostop'] = df_jap['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_jap = ['food', 'place', 'one', 'sushi', 'got', 'ordered',  'would', 'im', 'get', 'restaurant', 'dont', 'udon', 'soup','katsu','roll','spicy',
                       'miso','tempura','tea','chicken','pork','ive','also','beans','sandwich', 'curry', 'plate','eat','tender','order','ordered',
                       'go','time']
df_jap['review_nopunc_nostop_nocommon'] = df_jap['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_jap)))
freq_jap = pd.Series(" ".join(df_jap['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_jap)

# Korean Restaurant
df_kor = pd.DataFrame(np.array(korean), columns=['review'])
df_kor['word_count'] = df_kor['review'].apply(lambda x: len(str(x).split(" ")))
df_kor['stopword_coun'] = df_kor['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_kor['review_lower'] = df_kor['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_kor['review_nopunc'] = df_kor['review_lower'].str.replace('[^\w\s]', '')
df_kor['review_nopunc_nostop'] = df_kor['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_kor = ['food', 'place', 'chicken', 'rice', 'got', 'ordered',  'korean', 'im', 'spicy', 'restaurant', 'dont', 'sauce', 'bowl','menu',
                       'noodles','tempura','tea','soup','pork','ive','also','wings','sandwich', 'fried', 'kimchi','eat','side','go','bulgogi','seafood','beef',
                       'dishes','order','ordered','one','come','time','try','hot','would','dish','lunch','much','houston','inside','even']
df_kor['review_nopunc_nostop_nocommon'] = df_kor['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_kor)))
freq_kor = pd.Series(" ".join(df_kor['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_kor)

# Pizza Restaurant
df_piz = pd.DataFrame(np.array(pizza), columns=['review'])
df_piz['word_count'] = df_piz['review'].apply(lambda x: len(str(x).split(" ")))
df_piz['stopword_coun'] = df_piz['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_piz['review_lower'] = df_piz['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_piz['review_nopunc'] = df_piz['review_lower'].str.replace('[^\w\s]', '')
df_piz['review_nopunc_nostop'] = df_piz['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_piz = ['food', 'place', 'pizza', 'slice', 'got', 'ordered',  'cheese', 'im', 'slices', 'restaurant', 'dont', 'crust', 'pepperoni','menu',
                       'downtown','ive','also','pie','sauce','eat','side','go','york','order','ordered','get','houston','time','one','would']
df_piz['review_nopunc_nostop_nocommon'] = df_piz['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_piz)))
freq_piz = pd.Series(" ".join(df_piz['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_piz)

# Buffet Restaurant
df_buf = pd.DataFrame(np.array(buffet), columns=['review'])
df_buf['word_count'] = df_buf['review'].apply(lambda x: len(str(x).split(" ")))
df_buf['stopword_coun'] = df_buf['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_buf['review_lower'] = df_buf['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_buf['review_nopunc'] = df_buf['review_lower'].str.replace('[^\w\s]', '')
df_buf['review_nopunc_nostop'] = df_buf['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_buf = ['food', 'place', 'chicken', 'slice', 'got', 'ordered',  'cheese', 'im', 'slices', 'restaurant', 'dont', 'crust', 'pepperoni','menu',
                       'enchiladas','ive','also','panchos','mexican','eat','side','go','filipino','order','ordered',
                       'one','time','get','would','come','back','even','well']
df_buf['review_nopunc_nostop_nocommon'] = df_buf['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_buf)))
freq_buf = pd.Series(" ".join(df_buf['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_buf)

# Indian Restaurant
df_ind = pd.DataFrame(np.array(indian), columns=['review'])
df_ind['word_count'] = df_ind['review'].apply(lambda x: len(str(x).split(" ")))
df_ind['stopword_coun'] = df_ind['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_ind['review_lower'] = df_ind['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_ind['review_nopunc'] = df_ind['review_lower'].str.replace('[^\w\s]', '')
df_ind['review_nopunc_nostop'] = df_ind['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_ind = ['food', 'place', 'indian', 'got', 'ordered', 'masala', 'im', 'spicy', 'puri', 'dont', 'idlis', 'naan','menu','tikka','chicken', 'dosa',
                       'order','ordered','go','really','also','time','one','get','would','back','lunch','houston', 'restaurant','south','breakfast','came','come',
                       'ive']
df_ind['review_nopunc_nostop_nocommon'] = df_ind['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_ind)))
freq_ind = pd.Series(" ".join(df_ind['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_ind)

# Steak Restaurant
df_stk = pd.DataFrame(np.array(steak), columns=['review'])
df_stk['word_count'] = df_stk['review'].apply(lambda x: len(str(x).split(" ")))
df_stk['stopword_coun'] = df_stk['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_stk['review_lower'] = df_stk['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_stk['review_nopunc'] = df_stk['review_lower'].str.replace('[^\w\s]', '')
df_stk['review_nopunc_nostop'] = df_stk['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_stk = ['food', 'place', 'burger', 'taco', 'tacos', 'cheese', 'im', 'breakfast', 'burgers', 'burger', 'menu', 'ive', 'one', 'also','bar','eat','chicken',
                       'fries','order','ordered','time','back','got','get','would','go','well','came']
df_stk['review_nopunc_nostop_nocommon'] = df_stk['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_stk)))
freq_stk = pd.Series(" ".join(df_stk['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_stk)

# Chinese Restaurant
df_chin = pd.DataFrame(np.array(chinese), columns=['review'])
df_chin['word_count'] = df_chin['review'].apply(lambda x: len(str(x).split(" ")))
df_chin['stopword_coun'] = df_chin['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_chin['review_lower'] = df_chin['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_chin['review_nopunc'] = df_chin['review_lower'].str.replace('[^\w\s]', '')
df_chin['review_nopunc_nostop'] = df_chin['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_chin = ['food', 'place', 'chinese', 'rice', 'pork', 'fried', 'egg', 'sauce', 'soup', 'duck', 'shrimp', 'ive', 'one', 'also','beef','eat','chicken',
                       'fries','order','ordered','hot','bbq','sour','im','chow','meat','go','get','time','would','try','got']
df_chin['review_nopunc_nostop_nocommon'] = df_chin['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_chin)))
freq_chin = pd.Series(" ".join(df_chin['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_chin)

# Thai Restaurant
df_thai = pd.DataFrame(np.array(thai), columns=['review'])
df_thai['word_count'] = df_thai['review'].apply(lambda x: len(str(x).split(" ")))
df_thai['stopword_coun'] = df_thai['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_thai['review_lower'] = df_thai['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_thai['review_nopunc'] = df_thai['review_lower'].str.replace('[^\w\s]', '')
df_thai['review_nopunc_nostop'] = df_thai['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_thai = ['food', 'place', 'chinese', 'rice', 'thai', 'pad', 'im', 'curry', 'ive', 'spicy', 'houston', 'restaurant', 'rolls', 'shrimp','eat','chicken',
                       'bbq','hot', 'also','one', 'order','ordered','beef','sour','meat','go','get','back','time','would','try','lunch','came','got','soup','small',
                       'noodles','egg','dish','dishes','first','come','ever','fried','tom','menu','tea','mao']
df_thai['review_nopunc_nostop_nocommon'] = df_thai['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_thai)))
freq_thai = pd.Series(" ".join(df_thai['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_thai)
type(freq_thai)

###################################################################################
# most common words add below

###################################################################################
# export for label acquisition - cheap restaurants

df_all.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/all.csv')
df_mex.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/mex.csv')
df_viet.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/viet.csv')
df_bbq.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/bbq.csv')
df_jap.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/jap.csv')
df_kor.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/kor.csv')
df_piz.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/piz.csv')
df_buf.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/buf.csv')
df_ind.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/ind.csv')
df_stk.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/stk.csv')
df_chin.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/chin.csv')
df_thai.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/thai.csv')

############################################################################################################### 
# Mexican Restaurants

# Studewood Cantine
m16 = requests.get('https://www.yelp.com/biz/studewood-cantine-houston?osq=Mexican%20Food&sort_by=date_desc')
m16.status_code
m16.text
soup_m16 = BeautifulSoup(m16.text, "html.parser")
divs = soup_m16.findAll(itemprop="review")

reviews_mex_16 = []
for div in divs:
    reviews_mex_16.append(div.find('p').text)

m17 = requests.get('https://www.yelp.com/biz/studewood-cantine-houston?osq=Mexican%20Food&start=20&sort_by=date_desc')
m17.status_code
m17.text
soup_m17 = BeautifulSoup(m17.text, "html.parser")
divs = soup_m17.findAll(itemprop="review")

reviews_mex_17 = []
for div in divs:
    reviews_mex_17.append(div.find('p').text)

m18 = requests.get('https://www.yelp.com/biz/studewood-cantine-houston?osq=Mexican%20Food&start=40&sort_by=date_desc')
m18.status_code
m18.text
soup_m18 = BeautifulSoup(m18.text, "html.parser")
divs = soup_m18.findAll(itemprop="review")

reviews_mex_18 = []
for div in divs:
    reviews_mex_18.append(div.find('p').text)

studcan = reviews_mex_16 + reviews_mex_17 + reviews_mex_18
    
# El Tiempo Cantina
m19 = requests.get('https://www.yelp.com/biz/el-tiempo-cantina-richmond-houston-2?osq=Mexican%20Food&sort_by=date_desc')
m19.status_code
m19.text
soup_m19 = BeautifulSoup(m19.text, "html.parser")
divs = soup_m19.findAll(itemprop="review")

reviews_mex_19 = []
for div in divs:
    reviews_mex_19.append(div.find('p').text)

m20 = requests.get('https://www.yelp.com/biz/el-tiempo-cantina-richmond-houston-2?osq=Mexican%20Food&start=20&sort_by=date_desc')
m20.status_code
m20.text
soup_m20 = BeautifulSoup(m20.text, "html.parser")
divs = soup_m20.findAll(itemprop="review")

reviews_mex_20 = []
for div in divs:
    reviews_mex_20.append(div.find('p').text)

m21 = requests.get('https://www.yelp.com/biz/el-tiempo-cantina-richmond-houston-2?osq=Mexican%20Food&start=40&sort_by=date_desc')
m21.status_code
m21.text
soup_m21 = BeautifulSoup(m21.text, "html.parser")
divs = soup_m21.findAll(itemprop="review")

reviews_mex_21 = []
for div in divs:
    reviews_mex_21.append(div.find('p').text)
    
eltiecan = reviews_mex_19 + reviews_mex_20 + reviews_mex_21 

# The Original Ninfa's on Navigation
m22 = requests.get('https://www.yelp.com/biz/the-original-ninfas-on-navigation-houston-3?osq=Mexican%20Food&sort_by=date_desc')
m2.status_code
m2.text
soup_m22 = BeautifulSoup(m22.text, "html.parser")
divs = soup_m22.findAll(itemprop="review")

reviews_mex_22 = []
for div in divs:
    reviews_mex_22.append(div.find('p').text)

m23 = requests.get('https://www.yelp.com/biz/the-original-ninfas-on-navigation-houston-3?osq=Mexican%20Food&start=20&sort_by=date_desc')
m23.status_code
m23.text
soup_m23 = BeautifulSoup(m23.text, "html.parser")
divs = soup_m23.findAll(itemprop="review")

reviews_mex_23 = []
for div in divs:
    reviews_mex_23.append(div.find('p').text)

m24 = requests.get('https://www.yelp.com/biz/the-original-ninfas-on-navigation-houston-3?osq=Mexican%20Food&start=40&sort_by=date_desc')
m24.status_code
m24.text
soup_m24 = BeautifulSoup(m24.text, "html.parser")
divs = soup_m24.findAll(itemprop="review")

reviews_mex_24 = []
for div in divs:
    reviews_mex_24.append(div.find('p').text)
    
ninfa = reviews_mex_22 + reviews_mex_23 + reviews_mex_24

# Teotihuacan Mexican Cafe
m25 = requests.get('https://www.yelp.com/biz/teotihuacan-mexican-cafe-houston-4?osq=Mexican%20Food&sort_by=date_desc')
m25.status_code
m25.text
soup_m25 = BeautifulSoup(m25.text, "html.parser")
divs = soup_m25.findAll(itemprop="review")

reviews_mex_25 = []
for div in divs:
    reviews_mex_25.append(div.find('p').text)

m26 = requests.get('https://www.yelp.com/biz/teotihuacan-mexican-cafe-houston-4?osq=Mexican%20Food&start=20&sort_by=date_desc')
m26.status_code
m26.text
soup_m26 = BeautifulSoup(m26.text, "html.parser")
divs = soup_m11.findAll(itemprop="review")

reviews_mex_26 = []
for div in divs:
    reviews_mex_26.append(div.find('p').text)

m27 = requests.get('https://www.yelp.com/biz/teotihuacan-mexican-cafe-houston-4?osq=Mexican%20Food&start=40&sort_by=date_desc')
m27.status_code
m27.text
soup_m27 = BeautifulSoup(m27.text, "html.parser")
divs = soup_m27.findAll(itemprop="review")

reviews_mex_27 = []
for div in divs:
    reviews_mex_27.append(div.find('p').text)

teotih = reviews_mex_25 + reviews_mex_26 + reviews_mex_27

# Candente
m28 = requests.get('https://www.yelp.com/biz/candente-houston?osq=Mexican%20Food&sort_by=date_desc')
m28.status_code
m28.text
soup_m28 = BeautifulSoup(m28.text, "html.parser")
divs = soup_m28.findAll(itemprop="review")

reviews_mex_28 = []
for div in divs:
    reviews_mex_28.append(div.find('p').text)

m29 = requests.get('https://www.yelp.com/biz/candente-houston?osq=Mexican%20Food&start=20&sort_by=date_desc')
m29.status_code
m29.text
soup_m29 = BeautifulSoup(m29.text, "html.parser")
divs = soup_m29.findAll(itemprop="review")

reviews_mex_29 = []
for div in divs:
    reviews_mex_29.append(div.find('p').text)

m30 = requests.get('https://www.yelp.com/biz/candente-houston?osq=Mexican%20Food&start=40&sort_by=date_desc')
m30.status_code
m30.text
soup_m30 = BeautifulSoup(m30.text, "html.parser")
divs = soup_m30.findAll(itemprop="review")

reviews_mex_30 = []
for div in divs:
    reviews_mex_30.append(div.find('p').text)
    
candente = reviews_mex_28 + reviews_mex_29 + reviews_mex_30

# All mexican restaurants
mex_rest_exp = studcan + eltiecan + ninfa + teotih + candente
mex_rest_exp = [x.lower() for x in mex_rest_exp] # lower all words
for review in mex_rest_exp:
    print(review, "\n")
len(mex_rest_exp)

############################################################################################################### 
# Vietnamese Restaurants

# No $$$$ Vietnamese Restaurant 

############################################################################################################### 
# BBQ Restaurants

# International Smoke
bbq16 = requests.get('https://www.yelp.com/biz/international-smoke-houston-2?osq=BBQ&sort_by=date_desc')
bbq16.status_code
bbq16.text
soup_bbq16 = BeautifulSoup(bbq16.text, "html.parser")
divs = soup_bbq16.findAll(itemprop="review")

reviews_bbq_16 = []
for div in divs:
    reviews_bbq_16.append(div.find('p').text)

bbq17 = requests.get('https://www.yelp.com/biz/international-smoke-houston-2?osq=BBQ&start=20&sort_by=date_desc')
bbq17.status_code
bbq17.text
soup_bbq17 = BeautifulSoup(bbq17.text, "html.parser")
divs = soup_bbq17.findAll(itemprop="review")

reviews_bbq_17 = []
for div in divs:
    reviews_bbq_17.append(div.find('p').text)

bbq18 = requests.get('https://www.yelp.com/biz/international-smoke-houston-2?osq=BBQ&start=40&sort_by=date_desc')
bbq18.status_code
bbq18.text
soup_bbq18 = BeautifulSoup(bbq18.text, "html.parser")
divs = soup_bbq18.findAll(itemprop="review")

reviews_bbq_18 = []
for div in divs:
    reviews_bbq_18.append(div.find('p').text)

intsmoke = reviews_bbq_16 + reviews_bbq_17 + reviews_bbq_18

# Killen's Steakhouse
bbq19 = requests.get('https://www.yelp.com/biz/killens-steakhouse-pearland-2?osq=BBQ&sort_by=date_desc')
bbq19.status_code
bbq19.text
soup_bbq19 = BeautifulSoup(bbq19.text, "html.parser")
divs = soup_bbq19.findAll(itemprop="review")

reviews_bbq_19 = []
for div in divs:
    reviews_bbq_19.append(div.find('p').text)

bbq20 = requests.get('https://www.yelp.com/biz/killens-steakhouse-pearland-2?osq=BBQ&start=20&sort_by=date_desc')
bbq20.status_code
bbq20.text
soup_bbq20 = BeautifulSoup(bbq20.text, "html.parser")
divs = soup_bbq20.findAll(itemprop="review")

reviews_bbq_20 = []
for div in divs:
    reviews_bbq_20.append(div.find('p').text)

bbq21 = requests.get('https://www.yelp.com/biz/killens-steakhouse-pearland-2?osq=BBQ&start=40&sort_by=date_desc')
bbq21.status_code
bbq21.text
soup_bbq21 = BeautifulSoup(bbq21.text, "html.parser")
divs = soup_bbq21.findAll(itemprop="review")

reviews_bbq_21 = []
for div in divs:
    reviews_bbq_21.append(div.find('p').text)
    
killstk = reviews_bbq_19 + reviews_bbq_20 + reviews_bbq_21

# Del Frisco's Double Eagle Steakhouse
bbq22 = requests.get('https://www.yelp.com/biz/del-friscos-double-eagle-steakhouse-houston-2?osq=BBQ&sort_by=date_desc')
bbq22.status_code
bbq22.text
soup_bbq22 = BeautifulSoup(bbq22.text, "html.parser")
divs = soup_bbq22.findAll(itemprop="review")

reviews_bbq_22 = []
for div in divs:
    reviews_bbq_22.append(div.find('p').text)

bbq23 = requests.get('https://www.yelp.com/biz/del-friscos-double-eagle-steakhouse-houston-2?osq=BBQ&start=20&sort_by=date_desc')
bbq23.status_code
bbq23.text
soup_bbq23 = BeautifulSoup(bbq23.text, "html.parser")
divs = soup_bbq23.findAll(itemprop="review")

reviews_bbq_23 = []
for div in divs:
    reviews_bbq_23.append(div.find('p').text)

bbq24 = requests.get('https://www.yelp.com/biz/del-friscos-double-eagle-steakhouse-houston-2?osq=BBQ&start=40&sort_by=date_desc')
bbq24.status_code
bbq24.text
soup_bbq24 = BeautifulSoup(bbq24.text, "html.parser")
divs = soup_bbq24.findAll(itemprop="review")

reviews_bbq_24 = []
for div in divs:
    reviews_bbq_24.append(div.find('p').text)
    
delfris = reviews_bbq_22 + reviews_bbq_23 + reviews_bbq_24 

# Steak 48
bbq25 = requests.get('https://www.yelp.com/biz/two-brothers-smokin-oak-kitchen-houston-2?osq=BBQ&sort_by=date_desc')
bbq25.status_code
bbq25.text
soup_bbq25 = BeautifulSoup(bbq25.text, "html.parser")
divs = soup_bbq25.findAll(itemprop="review")

reviews_bbq_25 = []
for div in divs:
    reviews_bbq_25.append(div.find('p').text)

bbq26 = requests.get('https://www.yelp.com/biz/two-brothers-smokin-oak-kitchen-houston-2?osq=BBQ&start=20&sort_by=date_desc')
bbq26.status_code
bbq26.text
soup_bbq26 = BeautifulSoup(bbq26.text, "html.parser")
divs = soup_bbq26.findAll(itemprop="review")

reviews_bbq_26 = []
for div in divs:
    reviews_bbq_26.append(div.find('p').text)
    
bbq27 = requests.get('https://www.yelp.com/biz/two-brothers-smokin-oak-kitchen-houston-2?osq=BBQ&start=20&sort_by=date_desc')
bbq27.status_code
bbq27.text
soup_bbq27 = BeautifulSoup(bbq27.text, "html.parser")
divs = soup_bbq27.findAll(itemprop="review")

reviews_bbq_27 = []
for div in divs:
    reviews_bbq_27.append(div.find('p').text)

stk48 = reviews_bbq_25 + reviews_bbq_26 + reviews_bbq_27

# Pappas Bros. Steakhouse
bbq28 = requests.get('https://www.yelp.com/biz/pappas-bros-steakhouse-houston-4?osq=BBQ&sort_by=date_desc')
bbq28.status_code
bbq28.text
soup_bbq28 = BeautifulSoup(bbq28.text, "html.parser")
divs = soup_bbq28.findAll(itemprop="review")

reviews_bbq_28 = []
for div in divs:
    reviews_bbq_28.append(div.find('p').text)

bbq29 = requests.get('https://www.yelp.com/biz/pappas-bros-steakhouse-houston-4?osq=BBQ&start=20&sort_by=date_desc')
bbq29.status_code
bbq29.text
soup_bbq29 = BeautifulSoup(bbq29.text, "html.parser")
divs = soup_bbq29.findAll(itemprop="review")

reviews_bbq_29 = []
for div in divs:
    reviews_bbq_29.append(div.find('p').text)

bbq30 = requests.get('https://www.yelp.com/biz/pappas-bros-steakhouse-houston-4?osq=BBQ&start=40&sort_by=date_desc')
bbq30.status_code
bbq30.text
soup_bbq30 = BeautifulSoup(bbq30.text, "html.parser")
divs = soup_bbq30.findAll(itemprop="review")

reviews_bbq_30 = []
for div in divs:
    reviews_bbq_30.append(div.find('p').text)
    
pbs = reviews_bbq_28 + reviews_bbq_29 + reviews_bbq_30

bbq_rest_exp = intsmoke + killstk + delfris + stk48 + pbs
bbq_rest_exp = [x.lower() for x in bbq_rest] # lower all words
for review in bbq_rest_exp:
    print(review, "\n")
len(bbq_rest_exp)

############################################################################################################### 
# Japanese Restaurants

# Shun Japanese Kitchen
jap16 = requests.get('https://www.yelp.com/biz/shun-japanese-kitchen-houston-2?osq=Japanese%20Food&sort_by=date_desc')
jap16.status_code
jap16.text
soup_jap16 = BeautifulSoup(jap1.text, "html.parser")
divs = soup_jap16.findAll(itemprop="review")

reviews_jap_16 = []
for div in divs:
    reviews_jap_16.append(div.find('p').text)

jap17 = requests.get('https://www.yelp.com/biz/shun-japanese-kitchen-houston-2?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap17.status_code
jap17.text
soup_jap17 = BeautifulSoup(jap17.text, "html.parser")
divs = soup_jap17.findAll(itemprop="review")

reviews_jap_17 = []
for div in divs:
    reviews_jap_17.append(div.find('p').text)

jap18 = requests.get('https://www.yelp.com/biz/shun-japanese-kitchen-houston-2?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap18.status_code
jap18.text
soup_jap18 = BeautifulSoup(jap18.text, "html.parser")
divs = soup_jap18.findAll(itemprop="review")

reviews_jap_18 = []
for div in divs:
    reviews_jap_18.append(div.find('p').text)

shunj = reviews_jap_16 + reviews_jap_17 + reviews_jap_18

# izakaya
jap19 = requests.get('https://www.yelp.com/biz/izakaya-wa-houston?osq=Japanese%20Food&sort_by=date_desc')
jap19.status_code
jap19.text
soup_jap19 = BeautifulSoup(jap19.text, "html.parser")
divs = soup_jap19.findAll(itemprop="review")

reviews_jap_19 = []
for div in divs:
    reviews_jap_19.append(div.find('p').text)

jap20 = requests.get('https://www.yelp.com/biz/izakaya-wa-houston?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap20.status_code
jap20.text
soup_jap20 = BeautifulSoup(jap20.text, "html.parser")
divs = soup_jap20.findAll(itemprop="review")

reviews_jap_20 = []
for div in divs:
    reviews_jap_20.append(div.find('p').text)

jap21 = requests.get('https://www.yelp.com/biz/izakaya-wa-houston?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap21.status_code
jap21.text
soup_jap21 = BeautifulSoup(jap21.text, "html.parser")
divs = soup_jap21.findAll(itemprop="review")

reviews_jap_21 = []
for div in divs:
    reviews_jap_21.append(div.find('p').text)
    
izakaya = reviews_jap_19 + reviews_jap_20 + reviews_jap_21 

# Zen Japanese Izakaya
jap22 = requests.get('https://www.yelp.com/biz/zen-japanese-izakaya-houston?osq=Japanese%20Food&sort_by=date_desc')
jap22.status_code
jap22.text
soup_jap22 = BeautifulSoup(jap22.text, "html.parser")
divs = soup_jap22.findAll(itemprop="review")

reviews_jap_22 = []
for div in divs:
    reviews_jap_22.append(div.find('p').text)

jap23 = requests.get('https://www.yelp.com/biz/zen-japanese-izakaya-houston?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap23.status_code
jap23.text
soup_jap23 = BeautifulSoup(jap23.text, "html.parser")
divs = soup_jap23.findAll(itemprop="review")

reviews_jap_23 = []
for div in divs:
    reviews_jap_23.append(div.find('p').text)
    
jap24 = requests.get('https://www.yelp.com/biz/zen-japanese-izakaya-houston?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap24.status_code
jap24.text
soup_jap24 = BeautifulSoup(jap24.text, "html.parser")
divs = soup_jap24.findAll(itemprop="review")

reviews_jap_24 = []
for div in divs:
    reviews_jap_24.append(div.find('p').text)
    
zenjap = reviews_jap_22 + reviews_jap_23 + reviews_jap_24

# Kokoro
jap25 = requests.get('https://www.yelp.com/biz/kokoro-houston-2?osq=Japanese%20Food&sort_by=date_desc')
jap25.status_code
jap25.text
soup_jap25 = BeautifulSoup(jap25.text, "html.parser")
divs = soup_jap25.findAll(itemprop="review")

reviews_jap_25 = []
for div in divs:
    reviews_jap_25.append(div.find('p').text)

jap26 = requests.get('https://www.yelp.com/biz/kokoro-houston-2?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap26.status_code
jap26.text
soup_jap26 = BeautifulSoup(jap26.text, "html.parser")
divs = soup_jap26.findAll(itemprop="review")

reviews_jap_26 = []
for div in divs:
    reviews_jap_26.append(div.find('p').text)

jap27 = requests.get('https://www.yelp.com/biz/kokoro-houston-2?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap27.status_code
jap27.text
soup_jap27 = BeautifulSoup(jap27.text, "html.parser")
divs = soup_jap27.findAll(itemprop="review")

reviews_jap_27 = []
for div in divs:
    reviews_jap_27.append(div.find('p').text)

koko = reviews_jap_25 + reviews_jap_26 + reviews_jap_27

# Izakaya Hi
jap28 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&sort_by=date_desc')
jap28.status_code
jap28.text
soup_jap28 = BeautifulSoup(jap28.text, "html.parser")
divs = soup_jap28.findAll(itemprop="review")

reviews_jap_28 = []
for div in divs:
    reviews_jap_28.append(div.find('p').text)

jap29 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&start=20&sort_by=date_desc')
jap29.status_code
jap29.text
soup_jap29 = BeautifulSoup(jap29.text, "html.parser")
divs = soup_jap29.findAll(itemprop="review")

reviews_jap_29 = []
for div in divs:
    reviews_jap_29.append(div.find('p').text)

jap30 = requests.get('https://www.yelp.com/biz/napa-udon-house-and-wine-bar-houston-4?osq=Japanese%20Food&start=40&sort_by=date_desc')
jap30.status_code
jap30.text
soup_jap30 = BeautifulSoup(jap30.text, "html.parser")
divs = soup_jap30.findAll(itemprop="review")

reviews_jap_30 = []
for div in divs:
    reviews_jap_30.append(div.find('p').text)
    
izahi = reviews_jap_28 + reviews_jap_29 + reviews_jap_30

jap_rest_exp = shunj + izakaya + zenjap + koko + izahi
jap_rest_exp = [x.lower() for x in jap_rest_exp] # lower all words
for review in jap_rest_exp:
    print(review, "\n")
len(jap_rest_exp)

############################################################################################################### 
# Korean Restaurants

# No $$$$ Korean Restaurant 

############################################################################################################### 
# Pizza Restaurants

# No $$$$ Pizza Restaurant 

############################################################################################################### 
# Buffett Restaurants

# No $$$$ Buffet Restaurant 

############################################################################################################### 
# Indian Restaurants

# No $$$$ Indian Restaurant 

############################################################################################################### 
# Steak Restaurants

# Capital Grille
stk16 = requests.get('https://www.yelp.com/biz/the-capital-grille-houston?osq=Steakhouses&sort_by=date_desc')
stk16.status_code
stk16.text
soup_stk16 = BeautifulSoup(stk16.text, "html.parser")
divs = soup_stk16.findAll(itemprop="review")

reviews_stk_16 = []
for div in divs:
    reviews_stk_16.append(div.find('p').text)

stk17 = requests.get('https://www.yelp.com/biz/the-capital-grille-houston?osq=Steakhouses&start=20&sort_by=date_desc')
stk17.status_code
stk17.text
soup_stk17 = BeautifulSoup(stk17.text, "html.parser")
divs = soup_stk17.findAll(itemprop="review")

reviews_stk_17 = []
for div in divs:
    reviews_stk_17.append(div.find('p').text)

stk18 = requests.get('https://www.yelp.com/biz/the-capital-grille-houston?osq=Steakhouses&start=40&sort_by=date_desc')
stk18.status_code
stk18.text
soup_stk18 = BeautifulSoup(stk18.text, "html.parser")
divs = soup_stk18.findAll(itemprop="review")

reviews_stk_18 = []
for div in divs:
    reviews_stk_18.append(div.find('p').text)

capg = reviews_stk_16 + reviews_stk_17 + reviews_stk_18

# Tony's
stk19 = requests.get('https://www.yelp.com/biz/tonys-houston-2?osq=Steakhouses&sort_by=date_desc')
stk19.status_code
stk19.text
soup_stk19 = BeautifulSoup(stk19.text, "html.parser")
divs = soup_stk19.findAll(itemprop="review")

reviews_stk_19 = []
for div in divs:
    reviews_stk_19.append(div.find('p').text)
    
stk20 = requests.get('https://www.yelp.com/biz/tonys-houston-2?osq=Steakhouses&start=20&sort_by=date_desc')
stk20.status_code
stk20.text
soup_stk20 = BeautifulSoup(stk20.text, "html.parser")
divs = soup_stk20.findAll(itemprop="review")

reviews_stk_20 = []
for div in divs:
    reviews_stk_20.append(div.find('p').text)
    
stk21 = requests.get('https://www.yelp.com/biz/tonys-houston-2?osq=Steakhouses&start=40&sort_by=date_desc')
stk21.status_code
stk21.text
soup_stk21 = BeautifulSoup(stk21.text, "html.parser")
divs = soup_stk21.findAll(itemprop="review")

reviews_stk_21 = []
for div in divs:
    reviews_stk_21.append(div.find('p').text)

tonys = reviews_stk_19 + reviews_stk_20 + reviews_stk_21

# Eculent
stk22 = requests.get('https://www.yelp.com/biz/eculent-kemah?osq=Steakhouses&sort_by=date_desc')
stk22.status_code
stk22.text
soup_stk22 = BeautifulSoup(stk22.text, "html.parser")
divs = soup_stk22.findAll(itemprop="review")

reviews_stk_22 = []
for div in divs:
    reviews_stk_22.append(div.find('p').text)

stk23 = requests.get('https://www.yelp.com/biz/eculent-kemah?osq=Steakhouses&start=20&sort_by=date_desc')
stk23.status_code
stk23.text
soup_stk23 = BeautifulSoup(stk23.text, "html.parser")
divs = soup_stk23.findAll(itemprop="review")

reviews_stk_23 = []
for div in divs:
    reviews_stk_23.append(div.find('p').text)

stk24 = requests.get('https://www.yelp.com/biz/eculent-kemah?osq=Steakhouses&start=40&sort_by=date_desc')
stk24.status_code
stk24.text
soup_stk24 = BeautifulSoup(stk24.text, "html.parser")
divs = soup_stk24.findAll(itemprop="review")

reviews_stk_24 = []
for div in divs:
    reviews_stk_24.append(div.find('p').text)

ecu = reviews_stk_22 + reviews_stk_23 + reviews_stk_24

stk_rest_exp = capg + tonys + ecu
stk_rest_exp = [x.lower() for x in stk_rest] # lower all words
for review in stk_rest_exp:
    print(review, "\n")
len(stk_rest_exp)
    
############################################################################################################### 
# Chinese Restaurants (only one chinese restaurant with $$$$)

# Orient Express II
chin16 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&sort_by=date_desc')
chin16.status_code
chin16.text
soup_chin16 = BeautifulSoup(chin16.text, "html.parser")
divs = soup_chin16.findAll(itemprop="review")

reviews_chin_16 = []
for div in divs:
    reviews_chin_16.append(div.find('p').text)

chin17 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&start=20&sort_by=date_desc')
chin17.status_code
chin2.text
soup_chin17 = BeautifulSoup(chin17.text, "html.parser")
divs = soup_chin17.findAll(itemprop="review")

reviews_chin_17 = []
for div in divs:
    reviews_chin_17.append(div.find('p').text)

chin18 = requests.get('https://www.yelp.com/biz/siu-lap-city-houston?osq=Chinese%20Food&start=40&sort_by=date_desc')
chin18.status_code
chin18.text
soup_chin18 = BeautifulSoup(chin18.text, "html.parser")
divs = soup_chin18.findAll(itemprop="review")

reviews_chin_18 = []
for div in divs:
    reviews_chin_18.append(div.find('p').text)

oriexp = reviews_chin_16 + reviews_chin_17 + reviews_chin_18

chin_rest_exp = oriexp
chin_rest_exp = [x.lower() for x in chin_rest_exp] # lower all words
for review in chin_rest_exp:
    print(review, "\n")
len(chin_rest_exp)

###################################################################################
# Lets summarize reviews into groups (local variables to global variables)

all_reviews_exp = mex_rest_exp + jap_rest_exp + bbq_rest_exp + stk_rest_exp + chin_rest_exp

mexican_exp = mex_rest_exp
japanese_exp = jap_rest_exp
bbq_exp = bbq_rest_exp
steak_exp  = stk_rest_exp
chinese_exp = chin_rest_exp

###################################################################################
# Create data frames / Frequencies are given at the bottom of the code

stop_words = set(stopwords.words('english')) 

# All Expensive Restaurant
df_all_exp = pd.DataFrame(np.array(all_reviews_exp), columns=['review'])
df_all_exp['word_count'] = df_all_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_all_exp['stopword_coun'] = df_all_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_all_exp['review_lower'] = df_all_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_all_exp['review_nopunc'] = df_all_exp['review_lower'].str.replace('[^\w\s]', '')
df_all_exp['review_nopunc_nostop'] = df_all_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_all_exp = ['food', 'place', 'one', 'torta', 'tortas', 'got', 'ordered', 'salsa', 'would', 'im', 'get', 'restaurant', 'dont','tacos','mexican','meat',
                       'order','breakfast','really','also','de','houston','time','well','us','go','come','recommend','little','taco','coming','eat',
                       'tortillas','always','try','fajitas','chips','margaritas','texmex','chicken','queso','beef','two','beans', 'bbq', 'brisket', 'skewers','lamb','sauce',
                       'ribs','potato','pork','ive','sandwich', 'sausage', 'plate','tender', 'salad','try', 'sushi','udon', 'soup','katsu','roll','spicy',
                       'miso','tempura','tea', 'curry', 'japanese', 'burger', 'cheese', 'burgers', 'menu','bar',
                       'fries','back', 'came', 'chinese', 'rice', 'fried', 'egg', 'sauce', 'duck', 'shrimp', 'hot','sour','chow','try', 'roasted','siu','roast','belly','meats']
df_all_exp['review_nopunc_nostop_nocommon'] = df_all_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_all_exp)))
freq_all_exp = pd.Series(" ".join(df_all_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_all_exp)

# Mexican Restaurant
df_mex_exp = pd.DataFrame(np.array(mexican_exp), columns=['review'])
df_mex_exp['word_count'] = df_mex_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_mex_exp['stopword_coun'] = df_mex_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_mex_exp['review_lower'] = df_mex_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_mex_exp['review_nopunc'] = df_mex_exp['review_lower'].str.replace('[^\w\s]', '')
df_mex_exp['review_nopunc_nostop'] = df_mex_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_mex_exp = ['food', 'place', 'one', 'torta', 'tortas', 'got', 'ordered', 'salsa', 'would', 'im', 'get', 'restaurant', 'dont','tacos','mexican','meat',
                       'order','ordered','breakfast','really','also','de','houston','time','well','us','go','come','recommend','little','taco','coming','eat',
                       'tortillas','always','try','fajitas','chips','margaritas','texmex','chicken','queso','beef','two','beans']
df_mex_exp['review_nopunc_nostop_nocommon'] = df_mex_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_mex_exp)))
freq_mex_exp = pd.Series(" ".join(df_mex_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_mex_exp)

# BBQ Restaurant
df_bbq_exp = pd.DataFrame(np.array(bbq_exp), columns=['review'])
df_bbq_exp['word_count'] = df_bbq_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_bbq_exp['stopword_coun'] = df_bbq_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_bbq_exp['review_lower'] = df_bbq_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_bbq_exp['review_nopunc'] = df_bbq_exp['review_lower'].str.replace('[^\w\s]', '')
df_bbq_exp['review_nopunc_nostop'] = df_bbq_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_bbq_exp = ['food', 'place', 'one', 'bbq', 'got', 'ordered',  'would', 'im', 'get', 'restaurant', 'dont', 'brisket', 'skewers','beef','lamb','sauce',
                       'meat','ribs','potato','chicken','pork','ive','also','beans','sandwich', 'sausage', 'plate','eat','tender','order','ordered',
                       'salad','time','try','come','go','little']
df_bbq_exp['review_nopunc_nostop_nocommon'] = df_bbq_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_bbq_exp)))
freq_bbq_exp = pd.Series(" ".join(df_bbq_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_bbq_exp)

# Japanese Restaurant
df_jap_exp = pd.DataFrame(np.array(japanese_exp), columns=['review'])
df_jap_exp['word_count'] = df_jap_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_jap_exp['stopword_coun'] = df_jap_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_jap_exp['review_lower'] = df_jap_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_jap_exp['review_nopunc'] = df_jap_exp['review_lower'].str.replace('[^\w\s]', '')
df_jap_exp['review_nopunc_nostop'] = df_jap_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_jap_exp = ['food', 'place', 'one', 'sushi', 'got', 'ordered',  'would', 'im', 'get', 'restaurant', 'dont', 'udon', 'soup','katsu','roll','spicy',
                       'miso','tempura','tea','chicken','pork','ive','also','beans','sandwich', 'curry', 'plate','eat','tender','order','ordered',
                       'go','time','japanese']
df_jap_exp['review_nopunc_nostop_nocommon'] = df_jap_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_jap_exp)))
freq_jap_exp = pd.Series(" ".join(df_jap_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_jap_exp)

# Steak Restaurant
df_stk_exp = pd.DataFrame(np.array(steak_exp), columns=['review'])
df_stk_exp['word_count'] = df_stk_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_stk_exp['stopword_coun'] = df_stk_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_stk_exp['review_lower'] = df_stk_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_stk_exp['review_nopunc'] = df_stk_exp['review_lower'].str.replace('[^\w\s]', '')
df_stk_exp['review_nopunc_nostop'] = df_stk_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_stk_exp = ['food', 'place', 'burger', 'taco', 'tacos', 'cheese', 'im', 'breakfast', 'burgers', 'burger', 'menu', 'ive', 'one', 'also','bar','eat','chicken',
                       'fries','order','ordered','time','back','got','get','would','go','well','came']
df_stk_exp['review_nopunc_nostop_nocommon'] = df_stk_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_stk_exp)))
freq_stk_exp = pd.Series(" ".join(df_stk_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_stk_exp)

# Chinese Restaurant
df_chin_exp = pd.DataFrame(np.array(chinese_exp), columns=['review'])
df_chin_exp['word_count'] = df_chin_exp['review'].apply(lambda x: len(str(x).split(" ")))
df_chin_exp['stopword_coun'] = df_chin_exp['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_chin_exp['review_lower'] = df_chin_exp['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_chin_exp['review_nopunc'] = df_chin_exp['review_lower'].str.replace('[^\w\s]', '')
df_chin_exp['review_nopunc_nostop'] = df_chin_exp['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_chin_exp = ['food', 'place', 'chinese', 'rice', 'pork', 'fried', 'egg', 'sauce', 'soup', 'duck', 'shrimp', 'ive', 'one', 'also','beef','eat','chicken',
                       'fries','order','ordered','hot','bbq','sour','im','chow','meat','go','get','time','would','try','got', 'roasted','siu','roast','belly','meat','meats']
df_chin_exp['review_nopunc_nostop_nocommon'] = df_chin_exp['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_chin_exp)))
freq_chin_exp = pd.Series(" ".join(df_chin_exp['review_nopunc_nostop_nocommon']).split()).value_counts()[:15]
print(freq_chin_exp)

###################################################################################
# export for label acquisition - expensive restaurants

df_all_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/all_exp.csv')
df_mex_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/mex_exp.csv')
df_bbq_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/bbq_exp.csv')
df_jap_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/jap_exp.csv')
df_stk_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/stk_exp.csv')
df_chin_exp.to_csv(r'C:/Users/ewr27/Dropbox/E/School/Syracuse/IST 736 Text Mining/Final Project/Final Project/Importing For Models/chin_exp.csv')

###################################################################################
# Word clouds

# Mexican Restaurant
new_list_mex = df_mex['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_mex)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Vietnamese Restaurant
new_list_viet= df_viet['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_viet)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# BBQ Restaurant
new_list_bbq= df_bbq['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_bbq)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Japenese Restaurant
new_list_jap= df_jap['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_jap)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Korean Restaurant
new_list_kor= df_kor['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_kor)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Pizza Restaurant
new_list_piz= df_piz['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_piz)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Buffett Restaurant
new_list_buf= df_buf['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_buf)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Indian Restaurant
new_list_ind= df_ind['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_ind)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Steak Restaurant
new_list_stk= df_stk['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_stk)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Chinese Restaurant
new_list_chin= df_chin['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_chin)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# Thai Restaurant
new_list_thai= df_thai['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_thai)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

# All Rest combined
df_all = pd.DataFrame(np.array(all_reviews), columns=['review'])
df_all['word_count'] = df_all['review'].apply(lambda x: len(str(x).split(" ")))
df_all['stopword_coun'] = df_all['review'].apply(lambda x: len([x for x in x.split() if x in stop_words]))
df_all['review_lower'] = df_all['review'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_all['review_nopunc'] = df_all['review_lower'].str.replace('[^\w\s]', '')
df_all['review_nopunc_nostop'] = df_all['review_nopunc'].apply(lambda x: " ".join(x for x in x.split() if x not in stop_words))
other_stopwords_all = ['food']
df_all['review_nopunc_nostop_nocommon'] = df_all['review_nopunc_nostop'].apply(lambda x: "".join(" ".join(x for x in x.split() if x not in other_stopwords_mex)))
freq_all= pd.Series(" ".join(df_all['review_nopunc_nostop_nocommon']).split()).value_counts()[:20]
print(freq_all)

new_list_all= df_all['review_nopunc_nostop_nocommon'].values.tolist()
unique_string=(" ").join(new_list_all)
wordcloud = WordCloud(width = 1000, max_words=30, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

allhead = freq_all.head(15)
allhead = allhead.to_frame().reset_index()
type(allhead)

###################################################################################
#Histogram

allhead.columns = ['Token', 'Count']

objects = allhead.Token
y_pos = np.arange(len(allhead.Token))
performance = allhead.Count

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects,rotation=90)
plt.ylabel('Count')
plt.title('All Restaurant Tokens Top 15')
plt.show()

###################################################################################
# LDA Modeling - Find in Other Py File

###################################################################################
# Tokenize all lists by groups - Expensive Restaurants

# all restaurants strings for tokenizing 
all_string_exp = str(all_reviews_exp)
all_review__tokens_exp = nltk.word_tokenize(all_string_exp) #123,862 tokens

# mexican restaurant strings for tokenizing 
mex_string_exp = str(mexican_exp)
mex_tokens_exp = nltk.word_tokenize(mex_string_exp) #30,494 tokens

# bbq restaurant strings for tokenizing 
bbq_string_exp = str(bbq_exp)
bbq_tokens_exp = nltk.word_tokenize(bbq_string_exp) #25,904 tokens

# japanese restaurant strings for tokenizing 
jap_string_exp = str(japanese_exp)
jap_tokens_exp = nltk.word_tokenize(jap_string_exp) #34,678 tokens

# steak restaurant strings for tokenizing 
stk_string_exp = str(steak_exp)
stk_tokens_exp = nltk.word_tokenize(stk_string_exp) #25,924 tokens

# chinese restaurant strings for tokenizing 
chin_string_exp = str(chinese_exp)
chin_tokens_exp = nltk.word_tokenize(chin_string_exp) #6,866 tokens

###################################################################################
# Tokenize all lists by groups - Cheap Restaurants

# all restaurants strings for tokenizing 
all_string = str(all_reviews)
all_review__tokens = nltk.word_tokenize(all_string) #296,603 tokens

# mexican restaurant strings for tokenizing 
mex_string = str(mexican)
mex_tokens = nltk.word_tokenize(mex_string) #23,978 tokens

# vietnamese restaurant strings for tokenizing 
viet_string = str(vietnamese)
viet_tokens = nltk.word_tokenize(viet_string) #29,716 tokens

# bbq restaurant strings for tokenizing 
bbq_string = str(bbq)
bbq_tokens = nltk.word_tokenize(bbq_string) #25,904 tokens

# japanese restaurant strings for tokenizing 
jap_string = str(japanese)
jap_tokens = nltk.word_tokenize(jap_string) #27,453 tokens

# korean restaurant strings for tokenizing 
kor_string = str(korean)
kor_tokens = nltk.word_tokenize(kor_string) #31,599 tokens

# pizza restaurant strings for tokenizing 
piz_string = str(pizza)
piz_tokens = nltk.word_tokenize(piz_string) #26,429 tokens

# buffet restaurant strings for tokenizing 
buf_string = str(buffet)
buf_tokens = nltk.word_tokenize(buf_string) #22,375 tokens

# indian restaurant strings for tokenizing 
ind_string = str(indian)
ind_tokens = nltk.word_tokenize(ind_string) #26,531 tokens
    
# steak restaurant strings for tokenizing 
stk_string = str(steak)
stk_tokens = nltk.word_tokenize(stk_string) #25,924 tokens

# chinese restaurant strings for tokenizing 
chin_string = str(chinese)
chin_tokens = nltk.word_tokenize(chin_string) #27,665 tokens

# thai restaurant strings for tokenizing 
thai_string = str(thai)
thai_tokens = nltk.word_tokenize(thai_string) #29,039 tokens

###################################################################################
# LDA Model

import pandas as pd

#data = pd.read_csv('DATA/abcnews_date_text_Kaggle.csv', error_bad_lines=False);
data_small=pd.read_csv("C:\Users\ewr27\Dropbox\E\School\Syracuse\IST 736 Text Mining\Final Project\Final Project\Importing For Models/all.csv", error_bad_lines=False);
print(data_small.head())
## headline_text is the column name for the headline in the dataset
#data_text = data[['headline_text']]
data_text_small = data_small[['review_nopunc_nostop_nocommon']]
print(data_text_small)

#data_text['index'] = data_text.index
data_text_small['index'] = data_text_small.index
#print(data_text_small.index)
#print(data_text_small['index'])

#documents = data_text
documents = data_text_small
print(documents)

print("The length of the file - or number of docs is", len(documents))
print(documents[:5])

#%%
###################################################
###
### Data Prep and Pre-processing
###
###################################################
#https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python

import gensim
## IMPORTANT - you must install gensim first ##
## conda install -c anaconda gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer

import numpy as np
np.random.seed(2018)

import nltk
nltk.download('wordnet')
from nltk import PorterStemmer
from nltk.stem import PorterStemmer 
stemmer = PorterStemmer()

from nltk.tokenize import word_tokenize 
from nltk.stem.porter import *

#NOTES
##### Installing gensim caused my Spyder IDE no fail and no re-open
## I used two things and did a restart
## 1) in cmd (if PC)  psyder --reset
## 2) in cmd (if PC) conda upgrade qt

######################################
## function to perform lemmatize and stem preprocessing
############################################################
## Function 1
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

## Function 2
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

#Select a document to preview after preprocessing
doc_sample = documents[documents['index'] == 50].values[0][0]
print(doc_sample)
print('original document: ')
words = []
for word in doc_sample.split(' '):
    words.append(word)
print(words)
print('\n\n tokenized and lemmatized document: ')
print(preprocess(doc_sample))


#%%

## Preprocess the headline text, saving the results as ‘processed_docs’
processed_docs = documents['review_nopunc_nostop_nocommon'].map(preprocess)
print(processed_docs[:10])

#%%

## Create a dictionary from ‘processed_docs’ containing the 
## number of times a word appears in the training set.

dictionary = gensim.corpora.Dictionary(processed_docs)

## Take a look ...you can set count to any number of items to see
## break will stop the loop when count gets to your determined value
count = 0
for k, v in dictionary.iteritems():
    print(k, v)
    count += 1
    if count > 5:
        break

#%%    
#print(processed_docs)   
## Filter out tokens that appear in
## - - less than 15 documents (absolute number) or
## - - more than 0.5 documents (fraction of total corpus size, not absolute number).
## - - after the above two steps, keep only the first 100000 most frequent tokens
 ############## NOTE - this line of code did not work with my small sample
## as it created blank lists.....       
#dictionary.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)

for doc in processed_docs:
    print(doc)

print(dictionary)

#%%
#######################
## For each document we create a dictionary reporting how many
##words and how many times those words appear. Save this to ‘bow_corpus’
##############################################################################
#### bow: Bag Of Words
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
print(bow_corpus[3:5])

#%%
#################################################################
### TF-IDF
#################################################################
##Create tf-idf model object using models.TfidfModel on ‘bow_corpus’ 
## and save it to ‘tfidf’, then apply transformation to the entire 
## corpus and call it ‘corpus_tfidf’. Finally we preview TF-IDF 
## scores for our first document.

from gensim import corpora, models

tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]
## pprint is pretty print
from pprint import pprint

for doc in corpus_tfidf:
    pprint(doc)
    ## the break will stop it after the first doc
    break

#%%

#############################################################
### Running LDA using Bag of Words
#################################################################
    
# ~ 12 minutes
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=12, id2word=dictionary, passes=10)
    
# Print the Keyword in the 10 topics
pprint(lda_model.print_topics())

#doc_lda = lda_model[bow_corpus]


# Compute Perplexity
perplx = lda_model.log_perplexity(bow_corpus)
print('\nPerplexity: ', perplx )  # a measure of how good the model is. lower the better.

#%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Compute Coherence Score (Measures the fit of the model, how well it fit)
from gensim.models import CoherenceModel
#coherence_model_lda = CoherenceModel(model=lda_model, texts=data_text_small, dictionary=dictionary, coherence='c_v')
#coherence_lda = coherence_model_lda.get_coherence()
#print('\nCoherence Score: ', coherence_lda)

#%%

import pyLDAvis.sklearn as LDAvis
import pyLDAvis
import pyLDAvis.gensim 
import matplotlib.pyplot as plt
#conda install -c conda-forge pyldavis
pyLDAvis.enable_notebook() ## not using notebook
pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model, bow_corpus, dictionary)
pyLDAvis.show(vis)

###################################################################################
# MNB and SVM for project (pos,neg,neu)

#!/usr/bin/env python
# coding: utf-8

# In[66]:


##Project MNBs and SVMs for predicting sentiment##

#Import packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[113]:


##Import Data 
train=pd.read_csv("allcostreviews.csv")
y=train['sentiment'].values
X=train['review'].values


# In[114]:


#Split Data For Training model

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print(X_train[0])
print(y_train[0])
print(X_test[0])
print(y_test[0])

# Check how many training examples in each category
# this is important to see whether the data set is balanced or skewed

unique, counts = np.unique(y_train, return_counts=True)
print(np.asarray((unique, counts)))

#Check Test Data
unique, countstest = np.unique(y_test, return_counts=True)
print(np.asarray((unique, countstest)))

##NOTES: Data has already been cleaned##


# In[115]:


#Vectorize the data

#  unigram boolean vectorizer, set minimum document frequency to 5
#  unigram_bool_vectorizer = CountVectorizer(encoding='utf-8', binary=True, min_df=5, stop_words='english')

#  unigram term frequency vectorizer, set minimum document frequency to 5
unigram_count_vectorizer = CountVectorizer(encoding='utf-8', binary=False, min_df=5)

#  unigram and bigram term frequency vectorizer, set minimum document frequency to 5
gram12_count_vectorizer = CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)

#  unigram tfidf vectorizer, set minimum document frequency to 5
unigram_tfidf_vectorizer = TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)


# In[116]:


# The vectorizer can do "fit" and "transform"
# fit is a process to collect unique tokens into the vocabulary
# transform is a process to convert each document to vector based on the vocabulary
# These two processes can be done together using fit_transform(), or used individually: fit() or transform()

# fit vocabulary in training documents and transform the training documents into vectors
X_train_vec = unigram_count_vectorizer.fit_transform(X_train)
X_train_vec1 = gram12_count_vectorizer.fit_transform(X_train)
X_train_vec2 = unigram_tfidf_vectorizer.fit_transform(X_train)

# check the content of a document vector
print(X_train_vec.shape)
print(X_train_vec[0].toarray())

print(X_train_vec1.shape)
print(X_train_vec1[0].toarray())

print(X_train_vec2.shape)
print(X_train_vec2[0].toarray())

# check the size of the constructed vocabulary
print(len(unigram_count_vectorizer.vocabulary_))
print(len(gram12_count_vectorizer.vocabulary_))
print(len(unigram_tfidf_vectorizer.vocabulary_))

# print out the first 10 items in the vocabulary
print(list(unigram_count_vectorizer.vocabulary_.items())[:10])
print(list(gram12_count_vectorizer.vocabulary_.items())[:10])
print(list(unigram_tfidf_vectorizer.vocabulary_.items())[:10])

# check word index in vocabulary
print(unigram_count_vectorizer.vocabulary_.get('great'))
print(gram12_count_vectorizer.vocabulary_.get('great'))
print(unigram_tfidf_vectorizer.vocabulary_.get('great'))


# In[117]:


# use the vocabulary constructed from the training data to vectorize the test data. 
# Therefore, use "transform" only, not "fit_transform", 
# otherwise "fit" would generate a new vocabulary from the test data

X_test_vec = unigram_count_vectorizer.transform(X_test)
X_test_vec1 = gram12_count_vectorizer.transform(X_test)
X_test_vec2 = unigram_tfidf_vectorizer.transform(X_test)

# print out #examples and #features in the test set
print(X_test_vec.shape) #unigram TF
print(X_test_vec1.shape) #unigram and bigramTF
print(X_test_vec2.shape) #unigram TFIDF


# In[118]:


#MNB models

# initialize the MNB model
nb_clf= MultinomialNB() #unigram TF
nb_clf1= MultinomialNB() #unigram and bigramTF
nb_clf2= MultinomialNB() #unigram TFIDF

# use the training data to train the MNB model
nb_clf.fit(X_train_vec,y_train) #unigram TF
nb_clf1.fit(X_train_vec1,y_train) #unigram and bigramTF
nb_clf2.fit(X_train_vec2,y_train) #unigram TFIDF


# In[119]:


unigram_count_vectorizer.vocabulary_.get('great')
for i in range(0,3):
  print(nb_clf.feature_log_prob_[i][unigram_count_vectorizer.vocabulary_.get('great')])


# In[120]:


# test the classifier on the test data set, print accuracy score

print(nb_clf.score(X_test_vec,y_test)) #unigram TF
print(nb_clf1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(nb_clf2.score(X_test_vec2,y_test))  #unigram TFIDF


# In[121]:


# print confusion matrix (row: ground truth; col: prediction)

#unigram TF
y_pred = nb_clf.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=["positive","neutral","negative"])
print(cm)

#unigram and bigramTF
y_pred1 = nb_clf1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=["positive","neutral","negative"])
print(cm1)

#unigram TFIDF
y_pred2 = nb_clf.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=["positive","neutral","negative"])
print(cm2)


# In[122]:


# print classification reports
target_names = ["negative","neutral","positive"]

#unigram TF
print(classification_report(y_test, y_pred, target_names=target_names))

#unigram and bigramTF
print(classification_report(y_test, y_pred1, target_names=target_names))

#unigram TFIDF
print(classification_report(y_test, y_pred2, target_names=target_names))


# In[123]:


### Negative Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[0], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[0], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[0], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[124]:


### Neutral Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[1], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[1], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[1], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[125]:


### Positive Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[2], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[2], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[2], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[126]:


#Show errors for data where test was review was pos, pred was neg

err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="negative" and y_pred[i]=="positive"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[127]:


#Show errors for data where test was review was neg, pred was pos

err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="positive" and y_pred[i]=="negative"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[128]:


# MNB cross validation

#unigram TF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', binary=False, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram and bigramTF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram TFIDF
nb_clf_pipe = Pipeline([('vect', TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)


# In[129]:


#SVMs
from sklearn.svm import LinearSVC
SVM_Model=LinearSVC(C=.10) #unigram TF
SVM_Model1=LinearSVC(C=.10) #unigram and bigramTF
SVM_Model2=LinearSVC(C=.10) #unigram TFIDF

SVM_Model.fit(X_train_vec,y_train) #unigram TF
SVM_Model1.fit(X_train_vec1,y_train) #unigram and bigramTF
SVM_Model2.fit(X_train_vec2,y_train) #unigram TFIDF


# In[130]:


# SVM predictions
# print confusion matrix (row: ground truth; col: prediction)

#unigram TF
y_predsvm = SVM_Model.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=["negative","neutral","positive"])
print(cm)

#unigram and bigramTF
y_pred1svm = SVM_Model1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=["negative","neutral","positive"])
print(cm1)

#unigram TFIDF
y_pred2svm = SVM_Model.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=["negative","neutral","positive"])
print(cm2)


# In[131]:


# test the classifier on the test data set, print accuracy score

print(SVM_Model.score(X_test_vec,y_test)) #unigram TF
print(SVM_Model1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(SVM_Model2.score(X_test_vec2,y_test)) #unigram tfidf


# In[132]:


# print classification reports

#unigram TF
print(classification_report(y_test, y_predsvm, target_names=target_names))

#unigram and bigramTF
print(classification_report(y_test, y_pred1svm, target_names=target_names))

#unigram TFIDF
print(classification_report(y_test, y_pred2svm, target_names=target_names))


# In[133]:


###SVM Feature Ranks for unigram Negative##

feature_ranks = sorted(zip(SVM_Model.coef_[0], unigram_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Negative")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Negative")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[134]:


###SVM Feature Ranks for unigram and bigram Negative##

feature_ranks = sorted(zip(SVM_Model1.coef_[0], gram12_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Negative")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Negative")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[135]:


###SVM Feature Ranks for tfidf Negative##

feature_ranks = sorted(zip(SVM_Model2.coef_[0], unigram_tfidf_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Negative")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Negative")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[136]:


###SVM Feature Ranks for unigram Neutral##

feature_ranks = sorted(zip(SVM_Model.coef_[1], unigram_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Neutral")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Neutral")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[137]:


###SVM Feature Ranks for unigram and bigram##

feature_ranks = sorted(zip(SVM_Model1.coef_[1], gram12_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Neutral")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Neutral")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[138]:


###SVM Feature Ranks for tfidf##

feature_ranks = sorted(zip(SVM_Model2.coef_[1], unigram_tfidf_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Neutral")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Neutral")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[139]:


###SVM Feature Ranks for unigram Positive##

feature_ranks = sorted(zip(SVM_Model.coef_[2], unigram_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Positive")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Positive")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[140]:


###SVM Feature Ranks for unigram and bigram##

feature_ranks = sorted(zip(SVM_Model1.coef_[2], gram12_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Positive")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Positive")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[141]:


###SVM Feature Ranks for tfidf##

feature_ranks = sorted(zip(SVM_Model2.coef_[2], unigram_tfidf_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Positive")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Positive")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[142]:


err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="positive" and y_predsvm[i]=="negative"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)

###################################################################################
# Project MNB and SVM for 1$ vs 4$

#!/usr/bin/env python
# coding: utf-8

# In[78]:


#Import packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[79]:


##Import Data 
train=pd.read_csv("allcostreviews.csv")
y=train['cost'].values
X=train['review'].values


# In[80]:


#Split Data For Training model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print(X_train[0])
print(y_train[0])
print(X_test[0])
print(y_test[0])

# Check how many training examples in each category
# this is important to see whether the data set is balanced or skewed

unique, counts = np.unique(y_train, return_counts=True)
print(np.asarray((unique, counts)))

#Check Test Data
unique, countstest = np.unique(y_test, return_counts=True)
print(np.asarray((unique, countstest)))

##NOTES: Data has already been cleaned##


# In[81]:


#Vectorize the data
#  unigram boolean vectorizer, set minimum document frequency to 5
#  unigram_bool_vectorizer = CountVectorizer(encoding='utf-8', binary=True, min_df=5, stop_words='english')

#  unigram term frequency vectorizer, set minimum document frequency to 5
unigram_count_vectorizer = CountVectorizer(encoding='utf-8', binary=False, min_df=5)

#  unigram and bigram term frequency vectorizer, set minimum document frequency to 5
gram12_count_vectorizer = CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)

#  unigram tfidf vectorizer, set minimum document frequency to 5
unigram_tfidf_vectorizer = TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)


# In[82]:


# The vectorizer can do "fit" and "transform"
# fit is a process to collect unique tokens into the vocabulary
# transform is a process to convert each document to vector based on the vocabulary
# These two processes can be done together using fit_transform(), or used individually: fit() or transform()

# fit vocabulary in training documents and transform the training documents into vectors
X_train_vec = unigram_count_vectorizer.fit_transform(X_train)
X_train_vec1 = gram12_count_vectorizer.fit_transform(X_train)
X_train_vec2 = unigram_tfidf_vectorizer.fit_transform(X_train)

# check the content of a document vector
print(X_train_vec.shape)
print(X_train_vec[0].toarray()) #unigram TF

print(X_train_vec1.shape)
print(X_train_vec1[0].toarray()) #unigram and bigramTF

print(X_train_vec2.shape)
print(X_train_vec2[0].toarray()) #unigram tfidf

# check the size of the constructed vocabulary
print(len(unigram_count_vectorizer.vocabulary_))
print(len(gram12_count_vectorizer.vocabulary_))
print(len(unigram_tfidf_vectorizer.vocabulary_))

# print out the first 10 items in the vocabulary
print(list(unigram_count_vectorizer.vocabulary_.items())[:10])
print(list(gram12_count_vectorizer.vocabulary_.items())[:10])
print(list(unigram_tfidf_vectorizer.vocabulary_.items())[:10])

# check word index in vocabulary
print(unigram_count_vectorizer.vocabulary_.get('great'))
print(gram12_count_vectorizer.vocabulary_.get('great'))
print(unigram_tfidf_vectorizer.vocabulary_.get('great'))


# In[83]:


# use the vocabulary constructed from the training data to vectorize the test data. 
# Therefore, use "transform" only, not "fit_transform", 
# otherwise "fit" would generate a new vocabulary from the test data

X_test_vec = unigram_count_vectorizer.transform(X_test)
X_test_vec1 = gram12_count_vectorizer.transform(X_test)
X_test_vec2 = unigram_tfidf_vectorizer.transform(X_test)

# print out #examples and #features in the test set
print(X_test_vec.shape) #unigram TF
print(X_test_vec1.shape) #unigram and bigramTF
print(X_test_vec2.shape) #unigram tfidf


# In[84]:


#MNB Models

# initialize the MNB model
nb_clf= MultinomialNB() #unigram TF
nb_clf1= MultinomialNB() #unigram and bigramTF
nb_clf2= MultinomialNB()  #unigram tfidf

# use the training data to train the MNB model
nb_clf.fit(X_train_vec,y_train) #unigram TF
nb_clf1.fit(X_train_vec1,y_train) #unigram and bigramTF
nb_clf2.fit(X_train_vec2,y_train) #unigram tfidf


# In[85]:


# test the classifier on the test data set, print accuracy score

print(nb_clf.score(X_test_vec,y_test)) #unigram TF
print(nb_clf1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(nb_clf2.score(X_test_vec2,y_test)) #unigram tfidf


# In[86]:


# print confusion matrix (row: ground truth; col: prediction)

 #unigram TF
y_pred = nb_clf.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=[1, 4])
print(cm)
 #unigram and bigramTF
y_pred1 = nb_clf1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=[1, 4])
print(cm1)
 #unigram tfidf
y_pred2 = nb_clf.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=[1, 4])
print(cm2)


# In[87]:


# print classification reports

target_names = ['1', '4']

#unigram TF
print(classification_report(y_test, y_pred, target_names=target_names))

#unigram and bigramTF
print(classification_report(y_test, y_pred1, target_names=target_names))

#unigram tfidf
print(classification_report(y_test, y_pred2, target_names=target_names))


# In[88]:


### Cheap Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[0], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[0], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[0], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[89]:


### Expensive Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[1], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[1], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[1], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[90]:


#Show errors for data where rest was exp, predicted inexp  #unigram TF

err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]==4 and y_pred[i]==1):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[91]:


# MNB cross validation

#unigram TF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', binary=False, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram and bigramTF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram tfidf
nb_clf_pipe = Pipeline([('vect', TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)


# In[92]:


#SVMs
SVM_Model=LinearSVC(C=.1) #unigram TF
SVM_Model1=LinearSVC(C=.1) #unigram and bigramTF
SVM_Model2=LinearSVC(C=.1) #unigram tfidf

#Fit SVMs
SVM_Model.fit(X_train_vec,y_train) #unigram TF
SVM_Model1.fit(X_train_vec1,y_train) #unigram and bigramTF
SVM_Model2.fit(X_train_vec2,y_train) #unigram tfidf


# In[105]:


# test the classifier on the test data set, print accuracy score

print(SVM_Model.score(X_test_vec,y_test)) #unigram TF
print(SVM_Model1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(SVM_Model2.score(X_test_vec2,y_test)) #unigram tfidf


# In[93]:


#Predictions
#print confusion matrix (row: ground truth; col: prediction)

#unigram TF
y_predsvm = SVM_Model.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=[1,4])
print(cm)

#unigram and bigramTF
y_pred1svm = SVM_Model1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=[1,4])
print(cm1)

#unigram tfidf
y_pred2svm = SVM_Model.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=[1,4])
print(cm2)


# In[94]:


target_names = ['1', '4']
print(classification_report(y_test, y_predsvm, target_names=target_names)) #unigram TF

print(classification_report(y_test, y_pred1svm, target_names=target_names))  #unigram and bigramTF

print(classification_report(y_test, y_pred2svm, target_names=target_names)) #unigram tfidf


# In[99]:


###SVM Feature Ranks for unigram##

feature_ranks = sorted(zip(SVM_Model.coef_[0], unigram_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Cheap")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Cheap")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[100]:


###SVM Feature Ranks for unigram and bigram##

feature_ranks = sorted(zip(SVM_Model1.coef_[0], gram12_count_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Cheap")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not Indicate Cheap")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[102]:


###SVM Feature Ranks for TFIDF##

feature_ranks = sorted(zip(SVM_Model2.coef_[0], unigram_tfidf_vectorizer.get_feature_names()))

## get the 10 features that are best indicators of very negative sentiment (they are at the bottom of the ranked list)
very_negative_10 = feature_ranks[-10:]
print("Words that indicate Cheap")
for i in range(0, len(very_negative_10)):
    print(very_negative_10[i])
print()

## get 10 features that are least relevant to "very negative" sentiment (they are at the top of the ranked list)
not_very_negative_10 = feature_ranks[:10]
print("Words that do not indicate Cheap")
for i in range(0, len(not_very_negative_10)):
    print(not_very_negative_10[i])
print()


# In[103]:


#Error analysis
err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]==1 and y_predsvm[i]==4):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[104]:


# SVM cross validation

#unigram TF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', binary=False, min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram and bigramTF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram tfidf
nb_clf_pipe = Pipeline([('vect', TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

###################################################################################
# Project MNB and SVM for Rest Type

#!/usr/bin/env python
# coding: utf-8

# In[145]:


##Project MNBs and SVMs for predicting restaurnt type##

#Import packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[146]:


##Import Data 
train=pd.read_csv("allcostreviews.csv")
y=train['restaurant'].values
X=train['review'].values


# In[147]:


#Split Data For Training model

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)
print(X_train[0])
print(y_train[0])
print(X_test[0])
print(y_test[0])

# Check how many training examples in each category
# this is important to see whether the data set is balanced or skewed

unique, counts = np.unique(y_train, return_counts=True)
print(np.asarray((unique, counts)))

#Check Test Data
unique, countstest = np.unique(y_test, return_counts=True)
print(np.asarray((unique, countstest)))

##NOTES: Data has already been cleaned##


# In[148]:


#Vectorize the data

#  unigram term frequency vectorizer, set minimum document frequency to 5
unigram_count_vectorizer = CountVectorizer(encoding='utf-8', binary=False, min_df=5)

#  unigram and bigram term frequency vectorizer, set minimum document frequency to 5
gram12_count_vectorizer = CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)

#  unigram tfidf vectorizer, set minimum document frequency to 5
unigram_tfidf_vectorizer = TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)


# In[149]:


# fit vocabulary in training documents and transform the training documents into vectors
X_train_vec = unigram_count_vectorizer.fit_transform(X_train)
X_train_vec1 = gram12_count_vectorizer.fit_transform(X_train)
X_train_vec2 = unigram_tfidf_vectorizer.fit_transform(X_train)

# check the content of a document vector
print(X_train_vec.shape)
print(X_train_vec[0].toarray()) #unigram TF

print(X_train_vec1.shape)
print(X_train_vec1[0].toarray()) #unigram and bigramTF

print(X_train_vec2.shape)
print(X_train_vec2[0].toarray()) #unigram tfidf

# check the size of the constructed vocabulary
print(len(unigram_count_vectorizer.vocabulary_))
print(len(gram12_count_vectorizer.vocabulary_))
print(len(unigram_tfidf_vectorizer.vocabulary_))

# print out the first 10 items in the vocabulary
print(list(unigram_count_vectorizer.vocabulary_.items())[:10])
print(list(gram12_count_vectorizer.vocabulary_.items())[:10])
print(list(unigram_tfidf_vectorizer.vocabulary_.items())[:10])

# check word index in vocabulary
print(unigram_count_vectorizer.vocabulary_.get('great'))
print(gram12_count_vectorizer.vocabulary_.get('great'))
print(unigram_tfidf_vectorizer.vocabulary_.get('great'))


# In[150]:


# use the vocabulary constructed from the training data to vectorize the test data. 
# Therefore, use "transform" only, not "fit_transform", 
# otherwise "fit" would generate a new vocabulary from the test data

X_test_vec = unigram_count_vectorizer.transform(X_test)
X_test_vec1 = gram12_count_vectorizer.transform(X_test)
X_test_vec2 = unigram_tfidf_vectorizer.transform(X_test)

# print out #examples and #features in the test set
print(X_test_vec.shape) #unigram TF
print(X_test_vec1.shape) #unigram and bigramTF
print(X_test_vec2.shape) #unigram tfidf


# In[151]:


#MNB Models

# initialize the MNB model
nb_clf= MultinomialNB() #unigram TF
nb_clf1= MultinomialNB() #unigram and bigramTF
nb_clf2= MultinomialNB()  #unigram tfidf

# use the training data to train the MNB model
nb_clf.fit(X_train_vec,y_train) #unigram TF
nb_clf1.fit(X_train_vec1,y_train) #unigram and bigramTF
nb_clf2.fit(X_train_vec2,y_train) #unigram tfidf


# In[152]:


unigram_count_vectorizer.vocabulary_.get('great')
for i in range(0,3):
  print(nb_clf.feature_log_prob_[i][unigram_count_vectorizer.vocabulary_.get('great')])


# In[153]:


# test the classifier on the test data set, print accuracy score

print(nb_clf.score(X_test_vec,y_test)) #unigram TF
print(nb_clf1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(nb_clf2.score(X_test_vec2,y_test)) #unigram tfidf


# In[154]:


# print confusion matrix (row: ground truth; col: prediction)

 #unigram TF
y_pred = nb_clf.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm)
 #unigram and bigramTF
y_pred1 = nb_clf1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm1)
 #unigram tfidf
y_pred2 = nb_clf.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm2)


# In[155]:


# print classification reports MNB

target_names = ['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet']

#unigram TF
print(classification_report(y_test, y_pred, target_names=target_names))

#unigram and bigramTF
print(classification_report(y_test, y_pred1, target_names=target_names))

#unigram tfidf
print(classification_report(y_test, y_pred2, target_names=target_names))


# In[156]:


###BBQ Feature Ranks###

#BBQ Feature Ranks Unigram
bbqfeature_ranks = sorted(zip(nb_clf.feature_log_prob_[0], unigram_count_vectorizer.get_feature_names()))
bbq_features = bbqfeature_ranks[-10:]
print(bbq_features)

#BBQ Feature Ranks Unigram
bbqfeature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[0], gram12_count_vectorizer.get_feature_names()))
bbq_features1 = bbqfeature_ranks1[-10:]
print(bbq_features1)

#BBQ Feature Ranks Unigram
bbqfeature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[0], unigram_tfidf_vectorizer.get_feature_names()))
bbq_features2 = bbqfeature_ranks2[-10:]
print(bbq_features2)


# In[157]:


###Buffet Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[1], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[1], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[1], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[158]:


###Chinese Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[2], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[2], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[2], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[159]:


###Indian Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[3], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[3], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[3], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[160]:


###Japenese Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[4], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[4], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[4], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[161]:


###Korean Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[5], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[5], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[5], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[162]:


###Mexican Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[6], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[6], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[6], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[163]:


###Pizza Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[7], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[7], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[7], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[164]:


###Steak Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[8], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[8], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[8], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[178]:


###Thai Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[9], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[9], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[9], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)

#Where does curry fall for all?
unigram_count_vectorizer.vocabulary_.get('curry')
for i in range(0,10):
  print(nb_clf.feature_log_prob_[i][unigram_count_vectorizer.vocabulary_.get('curry')])


# In[166]:


###Vietnamese Feature Ranks###

#Feature Ranks Unigram
feature_ranks = sorted(zip(nb_clf.feature_log_prob_[10], unigram_count_vectorizer.get_feature_names()))
features = feature_ranks[-10:]
print(features)

#Feature Ranks Unigram
feature_ranks1 = sorted(zip(nb_clf1.feature_log_prob_[10], gram12_count_vectorizer.get_feature_names()))
features1 = feature_ranks1[-10:]
print(features1)

#Feature Ranks Unigram
feature_ranks2 = sorted(zip(nb_clf2.feature_log_prob_[10], unigram_tfidf_vectorizer.get_feature_names()))
features2 = feature_ranks2[-10:]
print(features2)


# In[167]:


#Show errors for data where rest was chinese, predicted thai

err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="chinese" and y_pred[i]=="thai"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[168]:


# MNB cross validation

#unigram TF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', binary=False, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram and bigramTF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

#unigram tfidf
nb_clf_pipe = Pipeline([('vect', TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)),('nb', MultinomialNB())])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)


# In[169]:


#SVMs
from sklearn.svm import LinearSVC
SVM_Model=LinearSVC(C=.1)#unigram TF
SVM_Model1=LinearSVC(C=.1)#unigram and bigramTF
SVM_Model2=LinearSVC(C=.1)#unigram tfidf

SVM_Model.fit(X_train_vec,y_train)#unigram TF
SVM_Model1.fit(X_train_vec1,y_train)#unigram and bigramTF
SVM_Model2.fit(X_train_vec2,y_train)#unigram tfidf


# In[170]:


# test the classifier on the test data set, print accuracy score

print(SVM_Model.score(X_test_vec,y_test)) #unigram TF
print(SVM_Model1.score(X_test_vec1,y_test)) #unigram and bigramTF
print(SVM_Model2.score(X_test_vec2,y_test)) #unigram tfidf


# In[171]:


#Predictions
#print confusion matrix (row: ground truth; col: prediction)

#unigram TF
y_predsvm = SVM_Model.fit(X_train_vec, y_train).predict(X_test_vec)
cm=confusion_matrix(y_test, y_pred, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm)

#unigram and bigramTF
y_pred1svm = SVM_Model1.fit(X_train_vec1, y_train).predict(X_test_vec1)
cm1=confusion_matrix(y_test, y_pred1, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm1)

#unigram tfidf
y_pred2svm = SVM_Model.fit(X_train_vec2, y_train).predict(X_test_vec2)
cm2=confusion_matrix(y_test, y_pred2, labels=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet'])
print(cm2)


# In[172]:


target_names = ['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza',
  'steak', 'thai', 'viet']
#unigram TF
print(classification_report(y_test, y_predsvm, target_names=target_names))

#unigram and bigramTF
print(classification_report(y_test, y_pred1svm, target_names=target_names))

#unigram tfidf
print(classification_report(y_test, y_pred2svm, target_names=target_names))


# In[173]:


err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="chinese" and y_predsvm[i]=="thai"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[175]:


err_cnt = 0
for i in range(0, len(y_test)):
    if(y_test[i]=="thai" and y_predsvm[i]=="chinese"):
        print(X_test[i])
        err_cnt = err_cnt+1
print("errors:", err_cnt)


# In[174]:


# cross validation -- Multiple trials, best results with settings shown

#unigram TF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', binary=False, min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)


#Unigram and bigramTF
nb_clf_pipe = Pipeline([('vect', CountVectorizer(encoding='utf-8', ngram_range=(1,2), min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)


#unigram tfidf
nb_clf_pipe = Pipeline([('vect', TfidfVectorizer(encoding='utf-8', use_idf=True, min_df=5)),('svm', LinearSVC(C=.1))])
scores = cross_val_score(nb_clf_pipe, X, y, cv=3)
avg=sum(scores)/len(scores)
print(avg)

###################################################################################
# EDA

#!/usr/bin/env python
# coding: utf-8

# In[177]:


##EDA for Project###
import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# In[192]:


##Import Data##
##Data has already been cleaned, stopwords remmoved##
justcheap = pd.read_csv("all_sentiment_tagged.csv")
allcost = pd.read_csv("allcostreviews.csv")
allexp = pd.read_csv("all_exp.csv")

bbq = pd.read_csv("bbq.csv")
buf = pd.read_csv("buffett.csv")
chin = pd.read_csv("chinese.csv")
ind = pd.read_csv("indian.csv")
jap = pd.read_csv("jap.csv")
kor = pd.read_csv("korean.csv")
mex = pd.read_csv("mexican.csv")
piz = pd.read_csv("piz.csv")
stk = pd.read_csv("stk.csv")
thai = pd.read_csv("thai.csv")
viet = pd.read_csv("viet.csv")

print(len(justcheap))
print(len(allcost))
print(len(allexp))


# In[179]:


#Word Clouds
#Just Cheap
new_list_cheap= justcheap['review'].values.tolist()
unique_string=(" ").join(new_list_cheap)
wordcloud = WordCloud(width = 1000, max_words=50, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("Cheap"+".png", bbox_inches='tight')
plt.show()
plt.close()

freq_cheap = pd.Series(" ".join(justcheap['review']).split()).value_counts()[:50]
#print(freq_cheap)
print(len(justcheap))
#allhead = freq_all.head(15)


# In[180]:


##Word Cloud##
#Expensive
new_list_exp= allexp['review'].values.tolist()
unique_string=(" ").join(new_list_exp)
wordcloud = WordCloud(width = 1000, max_words=50, height = 500).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("Expensive"+".png", bbox_inches='tight')
plt.show()
plt.close()

freq_exp = pd.Series(" ".join(allexp['review']).split()).value_counts()[:50]
#print(freq_exp)


# In[181]:


##Percentages -- does this make sense or do we need to Boolean Count the tokens?
print(freq_cheap/len(justcheap))
print(freq_exp/len(allexp))
percentcheap = (freq_cheap/len(justcheap))
percentexp = (freq_exp/len(allexp))


# In[182]:


##Top words for Cheap vs Expensive

import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt

frcheapdf = percentcheap.to_frame()
frexpdf = percentexp.to_frame()

frcheapdf.index.name = "Token"
frexpdf.index.name = "Token"

frcheapdf.columns = ['Percent']
frexpdf.columns = ['Percent']

#print(frcheapdf.head)
#print(frexpdf.head)

Comb = pd.merge(frcheapdf, frexpdf, left_index=True, right_index=True)
Comb.columns = ['Cheap',"Expensive"]
Combsmall = Comb[:15]
Combsmall.plot(y=["Cheap", "Expensive"],figsize=(12,8), kind="bar",width = .75, title='Top Words by Percentage')


# In[183]:


#Converting Data

freq_bbq = pd.Series(" ".join(bbq['review']).split()).value_counts()
freq_buf = pd.Series(" ".join(buf['review']).split()).value_counts()
freq_chin = pd.Series(" ".join(chin['review']).split()).value_counts()
freq_ind = pd.Series(" ".join(ind['review']).split()).value_counts()
freq_jap = pd.Series(" ".join(jap['review']).split()).value_counts()
freq_kor = pd.Series(" ".join(kor['review_nopunc_nostop_nocommon']).split()).value_counts()
freq_mex = pd.Series(" ".join(mex['review']).split()).value_counts()
freq_piz = pd.Series(" ".join(piz['review_nopunc_nostop_nocommon']).split()).value_counts()
freq_stk = pd.Series(" ".join(stk['review']).split()).value_counts()
freq_thai = pd.Series(" ".join(thai['review_nopunc_nostop_nocommon']).split()).value_counts()
freq_viet = pd.Series(" ".join(viet['review_nopunc_nostop_nocommon']).split()).value_counts()

per_bbq = (freq_bbq/len(bbq))
per_buf = (freq_buf/len(buf))
per_chin = (freq_chin/len(chin))
per_ind = (freq_ind/len(ind))
per_jap = (freq_jap/len(jap))
per_kor = (freq_kor/len(kor))
per_mex = (freq_mex/len(mex))
per_piz = (freq_piz/len(piz))
per_stk = (freq_stk/len(stk))
per_thai = (freq_thai/len(thai))
per_viet = (freq_viet/len(viet))

bbqdf = per_bbq.to_frame()
bufdf = per_buf.to_frame()
chindf = per_chin.to_frame()
inddf = per_ind.to_frame()
japdf = per_jap.to_frame()
kordf = per_kor.to_frame()
mexdf = per_mex.to_frame()
pizdf = per_piz.to_frame()
stkdf = per_stk.to_frame()
thaidf = per_thai.to_frame()
vietdf = per_viet.to_frame()

bbqdf.index.name = "Token"
bufdf.index.name = "Token"
chindf.index.name = "Token"
inddf.index.name = "Token"
japdf.index.name = "Token"
kordf.index.name = "Token"
mexdf.index.name = "Token"
pizdf.index.name = "Token"
stkdf.index.name = "Token"
thaidf.index.name = "Token"
vietdf.index.name = "Token"

bbqdf.columns = ['Percent']
bufdf.columns = ['Percent']
chindf.columns = ['Percent']
inddf.columns = ['Percent']
japdf.columns = ['Percent']
kordf.columns = ['Percent']
mexdf.columns = ['Percent']
pizdf.columns = ['Percent']
stkdf.columns = ['Percent']
thaidf.columns = ['Percent']
vietdf.columns = ['Percent']


# In[184]:


print(freq_thai)
print(freq_viet)


# In[149]:


#PLOTS 
#Percentages all together
forplotlist = [bbqdf, bufdf, chindf, inddf, japdf, kordf, mexdf, pizdf, stkdf, thaidf, vietdf]
rest2=bbqdf.merge(bufdf, how = 'outer', on = 'Token')
rest3=rest2.merge(chindf, how = 'outer', on = 'Token')
rest4=rest3.merge(inddf, how = 'outer', on = 'Token')
rest5=rest4.merge(japdf, how = 'outer', on = 'Token')
rest6=rest5.merge(kordf, how = 'outer', on = 'Token')
rest7=rest6.merge(mexdf, how = 'outer', on = 'Token')
rest8=rest7.merge(pizdf, how = 'outer', on = 'Token')
rest9=rest8.merge(stkdf, how = 'outer', on = 'Token')
rest10=rest9.merge(thaidf, how = 'outer', on = 'Token')
rest11=rest10.merge(vietdf, how = 'outer', on = 'Token')

rest11.columns = ['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza','steak', 'thai', 'viet']
#print(rest11.head)
rest11small = rest11[:15]
rest11small.plot(y=['bbq', 'buffet' ,'chinese', 'indian', 'japanese','korean', 'mexican', 'pizza','steak', 'thai', 'viet'],figsize=(12,5), kind="bar", width = .75, title = 'Word Frequency Per Restuarant Type ($ only)')


# In[152]:


print(len(bbq))
print(len(buf))
print(len(chin))
print(len(ind))
print(len(jap))
print(len(kor))
print(len(mex))
print(len(piz))
print(len(stk))
print(len(thai))
print(len(viet))
print(len(justcheap))


# In[199]:


#Check Data
unique, countstest = np.unique(justcheap['sentiment'], return_counts=True)
print(np.asarray((unique, countstest)))

unique, countstest = np.unique(allcost['sentiment'], return_counts=True)
print(np.asarray((unique, countstest)))

unique, countstest = np.unique(justcheap['restaurant'], return_counts=True)
print(np.asarray((unique, countstest)))

unique, countstest = np.unique(allcost['restaurant'], return_counts=True)
print(np.asarray((unique, countstest)))

print(len(justcheap))



