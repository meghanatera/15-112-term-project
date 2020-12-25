import requests 
from requests import get 
from bs4 import BeautifulSoup
import sys
import urllib
import urllib.request
import os
from PIL import Image, ImageTk

def Piada(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Piada'
    filename2 = 'Piada2'
    for img in soup.findAll('img')[3:4]: 
        temp = img.get('src')
        if temp[:1] == '/': 
            image = 'https://mypiada.com' + temp 
        else: 
            image = temp 
        imagefile = open(filename + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()
    for img in soup.findAll('img')[11:12]: 
        temp = img.get('src')
        if temp[:1] == '/': 
            image = 'https://mypiada.com' + temp 
        else: 
            image = temp 
        imagefile = open(filename2 + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()
        
def Porch(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Porch' 
    temp = '/UserFiles/News/2020-11-Takeout-Deals-NEWS.png'
    web = 'https://www.dineattheporch.com/'
    image = web + temp
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
    
def Mercurios(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Mercurios' 
    temp = 'https://menufyproduction.imgix.net/636861884224034641+84037.png?auto=compress,format&h=1080&w=1920&fit=max'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()
    
def Fujiya(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Fujiya'
    for img in soup.findAll('img')[:1]: 
        temp = img.get('src')
        if temp[:1] == 'i': 
            image = 'http://www.fujiyaramenpa.com/' + temp 
        else: 
            image = temp 
        imagefile = open(filename + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()

def Waffallonia(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Waffallonia'
    for img in soup.findAll('img')[:1]: 
        temp = img.get('src')
        if temp[:1] == '/': 
            image = 'https://www.waffallonia.com' + temp 
        else: 
            image = temp 
        imagefile = open(filename + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()

def Chipotle(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Chipotle' 
    temp = 'https://www.chipotle.com/content/dam/poc/order/images/entrees/bowl.jpg'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

def Zen(url):  
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Zen' 
    temp = 'https://media-cdn.grubhub.com/image/upload/d_search:browse-images:default.jpg/w_70,h_70,f_auto,fl_lossy,q_80,c_fit/oylwturwu3ukwavhnp3o'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close() 

def Tamarind(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Tamarind' 
    temp = 'https://media-cdn.grubhub.com/image/upload/d_search:browse-images:default.jpg/w_70,h_70,f_auto,fl_lossy,q_80,c_fit/v31viadctzyuq5bpx35c'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close() 

def Subway(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Subway' 
    temp = 'https://image.shutterstock.com/image-photo/two-fresh-submarine-sandwiches-ham-260nw-497930494.jpg'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close() 

def Chikn(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Chikn' 
    temp = 'https://scontent-iad3-1.cdninstagram.com/v/t51.29350-15/122612997_1300312870310777_4517524154162600765_n.jpg?_nc_cat=107&ccb=2&_nc_sid=8ae9d6&_nc_ohc=epk84sdNU0IAX8X04bU&_nc_ht=scontent-iad3-1.cdninstagram.com&oh=3fe5f5ef4a772983e8d80f9151c2979a&oe=5FF4F794'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

def FiveGuys(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Five Guys' 
    temp = 'https://media.gettyimages.com/photos/five-guys-inc-restaurant-stands-in-dublin-california-us-on-wednesday-picture-id117828443?k=6&m=117828443&s=612x612&w=0&h=zjjnj7gykv3T13Tlw2tM4vAmYPYnRuX-xwO162i5n6I='
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

def Panera(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Panera' 
    temp = 'https://media.gettyimages.com/photos/sign-marks-the-location-of-a-panera-bread-restaurant-on-may-5-2015-in-picture-id472270482?k=6&m=472270482&s=612x612&w=0&h=WGuKH_Qgih_U8gTRhgp8WIhOybCQr-s_QxJCE0fcl_Q='
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

def Moulin(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Cafe Moulin' 
    temp = 'https://lh3.googleusercontent.com/niouRrcy1QCRUwv7jG2Ryds9GD08nNYm7KIyoRerNS8mR7tsSY4PcWmBba0FZ8t31H5tTWzyyQ=w1080-h608-p-no-v0'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

def McD(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'McD'
    for img in soup.findAll('img')[12:13]: 
        temp = img.get('src')
        if temp[:1] == '/': 
            image = 'https://www.mcdonalds.com' + temp 
        else: 
            image = temp 
        imagefile = open(filename + '.jpeg', 'wb')
        imagefile.write(urllib.request.urlopen(image).read())
        imagefile.close()

def Honeygrow(url): 
    results = requests.get(url) 
    soup = BeautifulSoup(results.text, 'html.parser')
    filename = 'Honeygrow' 
    temp = 'https://images.getbento.com/accounts/4f414de3ec33336001dcb4ead38fcfb1/media/images/91140logotype_only_black.png'
    imagefile = open(filename + '.jpeg', 'wb')
    imagefile.write(urllib.request.urlopen(temp).read())
    imagefile.close()

    
Piada('https://mypiada.com')
Porch('https://www.dineattheporch.com/')
Mercurios('https://mercurios.menufy.com/#/')
Fujiya('http://www.fujiyaramenpa.com/menu.htm')
Waffallonia('https://www.waffallonia.com/index.php/menu')
Chipotle('https://catering.chipotle.com/')
Zen('https://www.grubhub.com/restaurant/zen-noodle-house-3531-forbes-ave-pittsburgh/504051')
Tamarind('https://www.grubhub.com/restaurant/tamarind-flavor-of-india-257-n-craig-st-pittsburgh/482935')
Subway('https://www.shutterstock.com/search/subway+sandwich')
Chikn('https://www.hotchikn.com/')
FiveGuys('https://www.gettyimages.com/photos/five-guys-burgers-and-fries?phrase=five%20guys%20burgers%20and%20fries&sort=mostpopular')
Panera('https://www.gettyimages.com/photos/panera-bread?phrase=panera%20bread&sort=mostpopular')
Moulin('https://cafemoulinpgh.com/')
McD('https://www.mcdonalds.com/us/en-us.html')
Honeygrow('https://www.honeygrow.com/menu/')

