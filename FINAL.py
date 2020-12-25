#Term Project 
#Meghana Tera, Section F1
from cmu_112_graphics import *
import requests 
from requests import get 
import random 
from bs4 import BeautifulSoup 
import os.path 
import math 
import re
from PIL import Image, ImageTk
import webbrowser

#creates an Account file if it does not already exist 
if not os.path.exists('Account.txt'):
    file = open('Account.txt','w')
    file.close()

ListOfRestaurants = ['The Porch at Schenley', 'Chipotle', 'Waffallonia', 'Piada', 
                    'Mercurios', 'Fujiya', 'Zen Noodle House', 'Tamarind Flavor of India']

#Helper function
#https://www.kosbie.net/cmu/spring-17/15-112/notes/dialogs-demo1.py
def choose(message, title, options):
    msg = message + "\n" + "Type in the number corresponding to your response:"
    for i in range(len(options)):
        msg += "\n" + str(i+1) + ": " + options[i]
    response = simpledialog.askstring(title, msg)
    try:
        return options[int(response)-1]
    except:
        return None

######################
#Menu & Extra Info
######################
class Oakland: 
    def __init__(self, name, price):
        self.name = name 
        self.price = price

def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')

def Porch(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_='menu_item')[:28]
    name = []
    price = []   
    for food in foodDiv: 
        allNames = food.strong.contents[0]
        allPrices = food.span.text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    return Oakland(name, price)

def Piada(url): 
    food = getWebsite(url)  
    foodDiv = food.find_all('div', class_= 'col-md-3 menu-item')
    name = [] 
    price = [] 
    for food in foodDiv:
        allNames = food.h3.text
        allPrices = food.p.small.contents[0]
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    return Oakland(name, price)

def Chipotle(url): 
    food = getWebsite(url)
    foodDiv = food.find_all('tr', class_='tr')[:6]
    foodDiv2 = food.find_all('tr', class_='tr')[21:29]
    name = [] 
    price = []
    for food in foodDiv:
        allNames = food.td.text
        prices = food.find_all('td')
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = [x.text.strip() for x in prices][1]
        name.append(names)
        price.append(prices)
    for food in foodDiv2:
        allNames = food.td.text
        prices = food.find_all('td')
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = [x.text.strip() for x in prices][1]
        name.append(names)
        price.append(prices)
    return Oakland(name, price)

def Zen(url): 
    food = getWebsite(url)
    foodDiv = food.find_all('div', class_='item-title-row')
    name = [] 
    price = []
    for food in foodDiv:
        allNames = food.find('h4', class_='item-title').text
        allPrices = food.find('span', class_='price').text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    return Oakland(name, price)

def Tamarind(url): 
    food = getWebsite(url)
    foodDiv = food.find_all('div', class_='item-title-row')[:19]
    name = [] 
    price = []
    for food in foodDiv:
        allNames = food.find('h4', class_='item-title').text
        allPrices = food.find('span', class_='price').text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    return Oakland(name, price)

class Shadyside: 
    def __init__(self, name, price):
        self.name = name 
        self.price = price
      
def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')

def Mercurios(url): 
    food = getWebsite(url) 
    foodA = food.find_all('a', class_ = 'btn btn-default col-xs-12 menu-item')[:36]
    name = []
    price = []  
    for food in foodA: 
        allNames = food.span.text
        allPrices = food.find('span', class_='menu-item-price').text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)  
    return Shadyside(name, price) 

def Fujiya(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_ = 'col-md-4 menu-items')[:7]
    foodDiv2 = food.find_all('div', class_ = 'col-md-4 menu-items')[24:32]
    name = [] 
    price = [] 
    for food in foodDiv: 
        allNames = food.h5.contents[0]
        allPrices = food.find('span', class_='price').text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    for food in foodDiv2: 
        allNames = food.h5.contents[0]
        allPrices = food.find('span', class_='price').text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        prices = ''.join(line.strip() for line in allPrices.split("\n"))
        name.append(names)
        price.append(prices)
    return Shadyside(name, price)  

class SquirrellHill: 
    def __init__(self, name, price):
        self.name = name 
        self.price = price
       
def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser') 

def Waffallonia(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_ = 'sppb-media-content')[:6]
    name = []
    price = [] 
    for food in foodDiv: 
        allNames = food.h3.text
        names = ''.join(line.strip() for line in allNames.split("\n"))
        name.append(names)
        price.append(names)
    return SquirrellHill(name, price)

class moreOakland: 
    def __init__(self, address, number): 
        self.address = address 
        self.number = number 

def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')

def morePiada(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_='hero-caption location-menu')
    numDiv = food.find_all('br') 
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('p', class_ = 'location-info').contents[0]
        addressTwo = ''.join(line.strip() for line in addressOne.split("\n"))
        address.append(addressTwo)
    for br in numDiv:
        nextBR = br.nextSibling
        newBR = addressTwo = ''.join(line.strip() for line in nextBR.split("\n"))
        num.append(newBR)
    return moreOakland(address, num[0])

def morePorch(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_='contact_info')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('p', class_ = 'address').text
        numOne = food.find('a', class_ = 'phone').text
        addressTwo = ''.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreOakland(address, num)

def moreChipotle(url):  
    food = getWebsite(url)
    foodDiv = food.find_all('div', class_='Core Core--ace')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', class_ = 'Core-address').text
        numOne = food.find('a', class_ = 'Phone-link').text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreOakland(address, num)

def moreZen(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_= 'section general-info')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', class_ = 'address').text
        numOne = food.find('div', class_ = 'phone').text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreOakland(address, num)

def moreTamarind(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_= 'section general-info')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', class_ = 'address').text
        numOne = food.find('div', class_ = 'phone').text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreOakland(address, num)

class moreShadyside: 
    def __init__(self, address, number): 
        self.address = address 
        self.number = number 

def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')

def moreMercurios(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_='col-xs-12 col-sm-4 top-buffer')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', {'id': 'home-section-address'}).text
        numOne = food.find('div', {'id': 'home-section-phone'}).text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreShadyside(address, num)

def moreFujiya(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_= 'section general-info')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', class_ = 'address').text
        numOne = food.find('div', class_ = 'phone').text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreShadyside(address, num)

class moreSquirrelHill: 
    def __init__(self, address, number): 
        self.address = address 
        self.number = number 

def getWebsite(url): 
    request = requests.get(url)
    return BeautifulSoup(request.text, 'html.parser')

def moreWaffallonia(url): 
    food = getWebsite(url) 
    foodDiv = food.find_all('div', class_= 'section general-info')
    address = [] 
    num = []
    for food in foodDiv:
        addressOne = food.find('div', class_ = 'address').text
        numOne = food.find('div', class_ = 'phone').text
        addressTwo = ' '.join(line.strip() for line in addressOne.split("\n"))
        numTwo = ''.join(line.strip() for line in numOne.split("\n"))
        address.append(addressTwo)
        num.append(numTwo)
    return moreSquirrelHill(address, num)
     
##########################
#recommender system K-NN
##########################
#[Type, Occurrence]
#fast food = 0, Italian = 1, Asian = 2, Breakfast/Bakery = 3
X = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[2,1],
     [3,1],[3,2],[0,7],[0,8],[1,2],[0,9],[2,2],[2,3],
     [0,10],[3,3],[3,4],[1,3],[1,4],[1,5],[2,4],[2,5],[2,6],[2,7]]

#[Location, Occurrence]
#Oakland = 0, Shadyside = 1, Squirrel Hill = 2
Z = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],
    [1,1],[1,2],[0,9],[1,3],[1,4],[0,10],[1,5],[1,6],
    [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[0,11],[0,12]]

#[Price, Occurrence]
#$ = 0, $$ = 1, $$$ = 2
V = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,8],[0,9],
     [1,1],[0,10],[0,11],[1,2],[2,3],[1,3],[1,4],[0,12],
     [0,13],[0,14],[0,15],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11]]

Y = ['Five Guys', 'Chikn', 'Subway', 'Chipotle', 'Panera', 'The Porch at Schenley', 'Piada', 'Little Asia', 
     'Cafe Moulin', 'Jitters Cafe', 'McDonalds', 'Honeygrow', 'Mercurios', 'STACKD', 'Fujiya', 'Noodle Head', 
     'Eat n Park', 'Waffallonia', 'Sumi Cakery', 'Milky Way', 'Napoli Pizzeria', 'Mineos pizza House', 
     'Everyday Noodles', 'Taiwanese Bistro Cafe 33', 'Zen Noodle House', 'Tamarind Flavor of India']
    
def restaurants(L):
    restNames = []
    for i in range(len(L)):
        if L[i] not in restNames:
            restNames.append(L[i])
    return restNames

def recommended(choice, values, target, k=3):
    nearest = []
    nearestNames = []
    for i in range(0, k):
        closest = -1
        count = -1
        for i in range(0, len(values)):
            distance = 0
            for j in range(0, len(choice)):
                dist = abs(choice[j] - values[i][j])
                distance += dist
            distance = math.sqrt(distance)
            if (closest == -1) or (closest > distance):
                closest = distance
                count = i
        nearest.append(values[count])
        values.remove(values[count])
        nearestNames.append(target[count])
        target.remove(target[count])
    return nearestNames

# choice = user input 
# values - the values of the dataset
# target - the target values(targetValues) of the dataset
#k = how many nearest I want 
def KNN(choice, values, target, k):
    while True:
        nearestNames = recommended(choice, values, target, k=k)
        targetValue = restaurants(nearestNames)
        if targetValue != None:
            break
    return nearestNames

####################################################################
#resizing images that were webscraped and downloaded 
####################################################################
ogPiadaPic = Image.open('Images/Piada2.jpeg')
newPiadaPic = ogPiadaPic.resize((150,150), Image.ANTIALIAS)

ogPorchPic = Image.open('Images/Porch.jpeg')
newPorchPic = ogPorchPic.resize((210,110), Image.ANTIALIAS)

ogMercuriosPic = Image.open('Images/Mercurios.jpeg')
newMercuriosPic = ogMercuriosPic.resize((210,110), Image.ANTIALIAS)

ogFujiyaPic = Image.open('Images/Fujiya.jpeg')
newFujiyaPic = ogFujiyaPic.resize((230,110), Image.ANTIALIAS)

ogWaffalloniaPic = Image.open('Images/Waffallonia.jpeg')
newWaffalloniaPic = ogWaffalloniaPic.resize((210,90), Image.ANTIALIAS)

ogChipotlePic = Image.open('Images/Chipotle.jpeg')
newChipotlePic = ogChipotlePic.resize((210,130), Image.ANTIALIAS)

ogZenPic = Image.open('Images/Zen.jpeg')
newZenPic = ogZenPic.resize((150,150), Image.ANTIALIAS)

ogTamarindPic = Image.open('Images/Tamarind.jpeg')
newTamarindPic = ogTamarindPic.resize((230,110), Image.ANTIALIAS)

ogSubwayPic = Image.open('Images/Subway.jpeg')
newSubwayPic = ogSubwayPic.resize((230,110), Image.ANTIALIAS)

ogChiknPic = Image.open('Images/Chikn.jpeg')
newChiknPic = ogChiknPic.resize((230,110), Image.ANTIALIAS)

ogFiveGuysPic = Image.open('Images/Five Guys.jpeg')
newFiveGuysPic = ogFiveGuysPic.resize((230,110), Image.ANTIALIAS)

ogMoulinPic = Image.open('Images/Cafe Moulin.jpeg')
newMoulinPic = ogMoulinPic.resize((230,110), Image.ANTIALIAS)

ogHoneygrowPic = Image.open('Images/Honeygrow.jpeg')
newHoneygrowPic = ogHoneygrowPic.resize((230,110), Image.ANTIALIAS)

ogMcDPic = Image.open('Images/McD.jpeg')
newMcDPic = ogMcDPic.resize((230,110), Image.ANTIALIAS)

######################
#appStarted
######################
def appStarted(app):
    app.mainOptions = ['main','Sign In', 'Create Account', 'Help']
    app.curr = app.mainOptions[0]
    app.menuOptions = ['menu', 'Suggested Restaurants', 'More Information', 'View your past menu']
    app.menuCurr = app.menuOptions[0]
    app.moreOptions = ['more', 'Porch', 'Piada', 'Mercurios', 'Fujiya', 
                        'Waffallonia', 'Chipotle', 'Zen', 'Tamarind']
    app.moreCurr = app.moreOptions[0]
    app.user = ''
    app.signin = False 
    app.menu = False
    app.createAccount = False 
    app.choice = '' 
    app.choiceTwo = ''
    app.choiceThree = ''
    app.rest = ''
    app.location = ''
    app.name = ''
    app.prices = ''
    app.suggestions = False 
    app.username = ''
    app.password = ''
    app.creating = False
    app.place = ''
    app.recommend = ''
    app.updateRest = ''
    app.userCount = 0
    app.past = False
    app.piadaImage = ImageTk.PhotoImage(newPiadaPic)
    app.porchImage = ImageTk.PhotoImage(newPorchPic)
    app.mercuriosImage = ImageTk.PhotoImage(newMercuriosPic)
    app.fujiyaImage = ImageTk.PhotoImage(newFujiyaPic)
    app.waffalloniaImage = ImageTk.PhotoImage(newWaffalloniaPic)
    app.chipotleImage = ImageTk.PhotoImage(newChipotlePic)
    app.zenImage = ImageTk.PhotoImage(newZenPic)
    app.tamarindImage = ImageTk.PhotoImage(newTamarindPic)
    app.subwayImage = ImageTk.PhotoImage(newSubwayPic)
    app.moulinImage = ImageTk.PhotoImage(newMoulinPic)
    app.chiknImage = ImageTk.PhotoImage(newChiknPic)
    app.fiveguysImage = ImageTk.PhotoImage(newFiveGuysPic)
    app.subwayImage = ImageTk.PhotoImage(newSubwayPic)
    app.honeygrowImage = ImageTk.PhotoImage(newHoneygrowPic)
    app.mcdImage = ImageTk.PhotoImage(newMcDPic)
    app.more = False
    app.morePiada = False
    app.addressPiada = ''
    app.numberPiada = ''
    app.morePorch = False
    app.addressPorch = ''
    app.numberPorch = ''
    app.moreMercurios = False
    app.addressMercurios = ''
    app.numberMercurios = ''
    app.moreFujiya = False
    app.addressFujiya = ''
    app.numberFujiya = ''
    app.moreChipotle = False
    app.addressChipotle = ''
    app.numberChipotle = ''
    app.moreZen = False
    app.addressZen = ''
    app.numberZen = ''
    app.moreTamarind = False
    app.addressTamarind = ''
    app.numberTamarind = ''
    app.moreWaffallonia = False
    app.addressWaffallonia = ''
    app.numberWaffallonia = ''
    app.music = False 
    app.anotherMenu = False
    app.timerDelay = 50
    app.namePast = ''
    app.pricesPast = ''
    app.organize = [['Low to High', False], ['High to Low', False], ['Alphabetically', False]]
    app.rOne = ''
    app.rTwo = ''
    app.rThree = ''
    app.rFour = ''
    app.rFive = ''

def timerFired(app): 
    if app.signin: 
        signIn(app)
    if app.createAccount: 
        createAccount(app)
    if app.creating: 
        Taste(app)
        app.creating = not app.creating
    if app.suggestions: 
        Recommendations(app)
    if app.past: 
        Past(app)
    if app.morePiada: 
        displayMorePiada(app)
    if app.morePorch: 
        displayMorePorch(app)
    if app.moreMercurios: 
        displayMoreMercurios(app)
    if app.moreChipotle: 
        displayMoreChipotle(app)
    if app.moreFujiya:
        displayMoreFujiya(app) 
    if app.moreZen: 
        displayMoreZen(app)
    if app.moreTamarind: 
        displayMoreTamarind(app)
    if app.moreWaffallonia: 
        displayMoreWaffallonia(app)
    if app.music: 
        playMusic(app)
    if app.anotherMenu: 
        Taste(app)
        app.anotherMenu = not app.anotherMenu
    if app.organize[0][1]:
        lowHigh(app)

###################
#mode controllers 
###################
def keyPressed(app, event):
    if app.curr == 'Sign In': 
        SignInKeyPressed(app,event) 
    if app.curr == 'Create Account':
        CreateAccountKeyPressed(app, event)
    if app.curr == 'Help':
        HelpKeyPressed(app, event)
    if app.menuCurr == 'Suggested Restaurants': 
        SuggestionsKeyPressed(app, event)
    if app.menuCurr == 'More Information': 
        MoreKeyPressed(app, event) 
    if app.menuCurr == 'View your past menu': 
        PastKeyPressed(app, event)
    if app.menu: 
        menuKeyPressed(app, event)
    
def mousePressed(app, event): 
    if app.curr == 'main': 
        mainMousePressed(app, event)
    if app.menuCurr == 'menu': 
        menuMousePressed(app, event)   
    if app.moreCurr == 'more': 
        moreMousePressed(app, event)
             
def redrawAll(app, canvas):
    if app.curr == 'main': 
        mainScreenRedrawAll(app, canvas)
    if app.curr == 'Sign In': 
        SignInRedrawAll(app, canvas)
    if app.curr == 'Create Account': 
        CreateAccountRedrawAll(app, canvas) 
    if app.curr == 'Help': 
        HelpRedrawAll(app, canvas)
    if app.menu: 
        MenuRedrawAll(app, canvas)   
    if app.menuCurr == 'More Information': 
        MoreRedrawAll(app, canvas)
    if app.menuCurr == 'Suggested Restaurants': 
        SuggestedRedrawAll(app, canvas)
    if app.menuCurr == 'View your past menu': 
        PastMenuRedrawAll(app, canvas)
    if app.more: 
        MoreRedrawAll(app, canvas)

######################
#modes 
######################
#main screen mode 
def mainMousePressed(app, event):
        cx, cy = app.width/2, app.height
        if ((cx-100 <= event.x <= cx+100) and
            (cy/4-30 <= event.y <= cy/4+30)):
            app.curr = app.mainOptions[1]
            app.signin = not app.signin
            #app.music = not app.music
        if ((cx-100 <= event.x <= cx+100) and
            (cy/2-30 <= event.y <= cy/2+30)):
            app.curr = app.mainOptions[2]
            app.createAccount = not app.createAccount
        if ((cx-100 <= event.x <= cx+100) and
            (cy/1.3-30 <= event.y <= cy/1.3+30)):
            app.curr = app.mainOptions[3]
        
def mainScreenRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "SteelBlue1")
        canvas.create_text(app.width/2, app.height/8, text = "Make Your Own Personalized Menu!", 
                        font = "Courier 30 bold", fill = "navy") 

        cx, cy = app.width, app.height
        canvas.create_rectangle(cx/2-100, cy/4-30, cx/2+100, cy/4+30, fill='medium orchid')
        canvas.create_text(cx/2, cy/4, text="Sign In", font = "Times 22 bold", fill = 'black')

        canvas.create_rectangle(cx/2-100, cy/2-30, cx/2+100, cy/2+30, fill='medium orchid')
        canvas.create_text(cx/2, cy/2, text='Create Account', font = "Times 22 bold", fill = 'black')

        canvas.create_rectangle(cx/2-100, cy/1.3-30, cx/2+100, cy/1.3+30, fill='medium orchid')
        canvas.create_text(cx/2, cy/1.3, text='How does this work?', font = "Times 20 bold", fill = 'black') 

#sign in mode 
def SignInKeyPressed(app, event): 
    if event.key == 'Left':
        app.curr = app.mainOptions[0]

def SignInRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "firebrick1")
        canvas.create_text(app.width/2, app.height/8, text = "Sign In!", 
                            font = "Courier 39 bold", fill = "white")
        log = 'Log in to see your menu or create a new menu' 
        canvas.create_text(app.width/2, app.height/2, text = log, 
                            font = "Courier 18 bold", fill = "white") 

def signIn(app): #this returns the username 
        logUsername = app.getUserInput('Enter your username: ')
        logPassword = app.getUserInput('Enter your password: ')
        if app.userCount == 1: 
            file = open('Account.txt', 'r')
            for row in file: 
                space = row.split('-') 
                username = space[0]
                password = space[1]
                password = password[0:((len(password) - 1))]
                if logUsername == username and logPassword == password: 
                    app.signin = not app.signin
                    app.menu = not app.menu
                    app.creating = not app.creating 
                    app.username = username
                    app.password = password
                    break 
                else: 
                    continue
        else: 
            file = open('Account.txt', 'r')
            for row in file: 
                space = row.split('-') 
                username = space[0]
                password = space[1]
                if logUsername == username and logPassword == password: 
                    app.signin = not app.signin
                    app.menu = not app.menu
                    app.creating = not app.creating 
                    app.username = username
                    app.password = password
                    break 
                else: 
                    continue

#create account mode 
def CreateAccountKeyPressed(app, event): 
    if event.key == 'Left':
        app.curr = app.mainOptions[0] 

def CreateAccountRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "maroon4")
        canvas.create_text(app.width/2, app.height/8, text = "Create an Account!!", 
                        font = "Courier 39 bold", fill = "white") 
        user = 'Username: ' + str(app.user)
        canvas.create_text(app.width/2, app.height/2,text = user, 
                            font = "Courier 18 bold", fill = 'white')
        canvas.create_text(app.width/2, app.height/1.6,text = 'Password: *************', 
                            font = "Courier 18 bold", fill = 'white') 

def createAccount(app): 
        message = 'Hello! Please create an account to begin'
        title = 'Registration' 
        messagebox.showinfo(title, message)
        while True: 
            username = app.getUserInput('Enter a username: ')
            if username not in open('Account.txt', 'r').read(): 
                app.user = username
                break 
            message = 'Sorry this username already exists, try a different one'
            title = 'Try Again'
            messagebox.showinfo(title, message)
        while True: 
            password = app.getUserInput('Enter a password: ')
            checkPassword = app.getUserInput('Confirm password: ')
            if password == checkPassword: 
                break 
            message = 'Passwords do not match, try again'
            title = 'Try Again'
            messagebox.showinfo(title, message)
        file = open("Account.txt","a")
        file.write (username)
        file.write ("-") 
        file.write (password)
        file.write("\n")
        file.close()
        message = 'You have successfully created an account! Please login now'
        title = 'Registration Successful'
        messagebox.showinfo(title, message) 
        app.createAccount = not app.createAccount
        app.userCount += 1
        app.curr = app.mainOptions[1]
        app.signin = not app.signin 

#help mode 
def HelpKeyPressed(app, event): 
    if event.key == 'Left':
        app.curr = app.mainOptions[0] 

def HelpRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "black")
        canvas.create_text(app.width/2, app.height/8, text = "How does this work?", 
                            font = "Courier 39 bold", fill = "white")
        message = (" Enter what type of food you want to eat and a menu \n of your preferences will be made from local \n" + 
                    ' restaurants near cmu. \n \n Locations: \n \n 1.Oakland \n 2.Shadyside \n 3.Squirrel Hill')
        canvas.create_text(app.width/2, app.height/2, text = message, 
                            font = "Courier 18 bold", fill = "white") 

#menu mode
def menuMousePressed(app, event): 
        cx,cy = app.width/1.2, app.height/1.04
        if((cx-100 <= event.x <= cx+100) and (cy-15 <= event.y <= cy+15)):
            app.menuCurr = app.menuOptions[3]
            app.past = not app.past
        cx1, cy1 = app.width/5.5, app.height/1.04 
        if((cx1-100 <= event.x <= cx1+100) and (cy1-15 <= event.y <= cy1+15)):
            app.menuCurr = app.menuOptions[1]
            app.suggestions = not app.suggestions 
        cx2, cy2 = app.width/2.1, app.height/1.04
        if((cx2-110 <= event.x <= cx2+110) and (cy2-15 <= event.y <= cy2+15)):
            app.menuCurr = app.menuOptions[2]
        cx3, cy3 = app.width/20, app.height/10
        if((cx3-10 <= event.x <= cx3+10) and (cy3-10 <= event.y <= cy3+10)): 
            app.organize[0][1] = not app.organize[0][1]

def MenuRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "cadet blue")
        canvas.create_text(app.width/2, app.height/8, text = 'Your Menu!', 
                            font = 'Courier 39 bold', fill = 'black')

        msg = "You picked: " + str(app.choice) + " --> " + str(app.choiceTwo)
        canvas.create_text(app.width/2, app.height/24, text = msg, 
                            font = 'Courier 18 bold', fill = 'black')
        
        Restaurant = 'Restaurant: ' + app.rest                   
        canvas.create_text(app.width/2, app.height/5, text = Restaurant, 
                            font = 'Courier 14 bold', fill = 'black')

        Location = 'This is Located in: ' + app.location                   
        canvas.create_text(app.width/2, app.height/4.3, text = Location, 
                            font = 'Courier 14 bold', fill = 'black')

        canvas.create_text(app.width/6, app.height/3.4, text = "Food Names:", 
                            font = 'Courier 18 bold', fill = 'black')
        foodNames = app.name
        canvas.create_text(app.width/6, app.height/1.6, text = foodNames, 
                            font = 'Courier 12 bold', fill = 'black')

        canvas.create_text(app.width/1.2, app.height/3.4, text = "Prices($):", 
                            font = 'Courier 18 bold', fill = 'black')
        foodPrices = app.prices
        canvas.create_text(app.width/1.2, app.height/1.6, text = foodPrices, 
                            font = 'Courier 12 bold', fill = 'black')

        canvas.create_rectangle(app.width/1.2-100,app.height/1.04-15,app.width/1.2+100,app.height/1.04+15,
                                fill = 'black')
        canvas.create_text(app.width/1.2, app.height/1.04, text = 'View your past menu', 
                            font = 'Courier 14 bold', fill = 'white')
        
        canvas.create_rectangle(app.width/5.5-100,app.height/1.04-15,app.width/5.5+100,app.height/1.04+15,
                                fill = 'black')
        canvas.create_text(app.width/5.5, app.height/1.04, text = 'Suggested Restuarants', 
                            font = 'Courier 14 bold', fill = 'white')
        
        canvas.create_rectangle(app.width/2.1-110,app.height/1.04-15,app.width/2.1+110,app.height/1.04+15,
                                fill = 'black')
        canvas.create_text(app.width/2.1, app.height/1.04, text = 'More Information', 
                            font = 'Courier 14 bold', fill = 'white')
        canvas.create_text(app.width/8, app.height/15, text = "press 'r' to get another menu", 
                            font = 'Courier 12 bold', fill = 'black')
        if app.rest == 'Piada': 
            canvas.create_image(900, 110, image = app.piadaImage)
        if app.rest == 'The Porch at Schenley': 
            canvas.create_image(850, 110, image = app.porchImage)
        if app.rest == 'Mercurios':
            canvas.create_image(850, 110, image = app.mercuriosImage)
        if app.rest == 'Waffallonia':
            canvas.create_image(850, 110, image = app.waffalloniaImage)
        if app.rest == 'Chipotle':
            canvas.create_image(850, 110, image = app.chipotleImage)
        if app.rest == 'Fujiya':
            canvas.create_image(850, 110, image = app.fujiyaImage)
        if app.rest == 'Zen Noodle House':
            canvas.create_image(850, 110, image = app.zenImage)
        if app.rest == 'Tamarind Flavor of India':
            canvas.create_image(850, 110, image = app.tamarindImage)

        organizeSome = ['The Porch at Schenley', 'Mercurios', 'Chipotle', 'Fujiya', 
                        'Zen Noodle House', 'Tamarind Flavor of India']
        if app.rest in organizeSome: 
            canvas.create_text(app.width/6, app.height/10, text = 'Price: Lowest to Highest', 
                                font = 'Courier 12 bold', fill = 'black')
            if app.organize[0][1] == False: 
                canvas.create_rectangle(app.width/20-10,app.height/10-10,app.width/20+10,app.height/10+10,
                                        width = 2)
            elif app.organize[0][1] == True:
                canvas.create_rectangle(app.width/20-10,app.height/10-10,app.width/20+10,app.height/10+10,
                                        fill = 'black', width = 2)
              
def Taste(app): 
    while True: 
        message = 'What would you like your menu to be based off of?'
        title = 'Options'
        options = ['Taste', 'Location', 'Price']
        response = choose(message, title, options)
        if response in options: 
            app.choiceThree = response 
            break
        message = 'Please choose an option listed'
        title = 'Try Again'
        messagebox.showinfo(title, message)
    if response == 'Taste': 
        while True:
            message = 'What type of food would you like to eat?'
            title = 'Types of Food Options'
            options = ['American Food', 'Italian Food', 'Asian Food']
            response = choose(message, title, options)
            if response in options: 
                app.choice = response 
                break
            message = 'Please choose an option listed'
            title = 'Try Again'
            messagebox.showinfo(title, message)
        if response == 'American Food': 
            message = 'What would you like to eat?'
            title = 'Food Options'
            options = ['Fast Food', 'Breakfast']
            response = choose(message, title, options)
            app.choiceTwo = response
            if response == 'Fast Food': 
                All = ['The Porch at Schenley', 'Chipotle']
                rand = random.choice(All)
                if rand == 'The Porch at Schenley': 
                    app.rest = 'The Porch at Schenley'
                    app.location = 'Oakland'
                    url = 'https://www.dineattheporch.com/schenley/menu'
                    food = Porch(url)
                    app.name = '\n'.join(map(str, food.name)) 
                    app.prices = '\n'.join(map(str, food.price))
                elif rand == 'Chipotle': 
                    app.rest = 'Chipotle'
                    app.location = 'Oakland'
                    url = 'https://www.menuwithprice.com/menu/chipotle-mexican-grill/'
                    food = Chipotle(url)
                    app.name = '\n'.join(map(str, food.name)) 
                    app.prices = '\n'.join(map(str, food.price))
    
            elif response == 'Breakfast': 
                app.rest = 'Waffallonia'
                app.location = 'Squirrel Hill'
                url = 'https://www.waffallonia.com/index.php/menu'
                food = Waffallonia(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
                
        elif response == 'Italian Food': 
            message = 'What would you like to eat?'
            title = 'Food Options'
            options = ['Pasta', 'Pizza']
            response = choose(message, title, options)
            app.choiceTwo = response
            if response == 'Pasta': 
                app.rest = 'Piada'
                app.location = 'Oakland'
                url = 'https://mypiada.com/menu/oakland'
                food = Piada(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
                    
            elif response == 'Pizza':
                app.rest = 'Mercurios'
                app.location = 'Shadyside'
                url = 'https://mercurios.menufy.com/#/'
                food = Mercurios(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
             
        elif response == 'Asian Food': 
            message = 'What would you like to eat?'
            title = 'Food Options'
            options = ['Japanese', 'Chinese', 'Indian']
            response = choose(message, title, options)
            app.choiceTwo = response
            if response == 'Japanese': 
                app.rest = 'Fujiya'
                app.location = 'Shadyside'
                url = 'http://www.fujiyaramenpa.com/menu.htm'
                food = Fujiya(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
            if response == 'Chinese': 
                app.rest = 'Zen Noodle House'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
                food = Zen(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
            if response == 'Indian': 
                app.rest = 'Tamarind Flavor of India'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
                food = Tamarind(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
    if response == 'Location': 
        app.choice = app.choiceThree
        while True:
            message = 'Which location would you prefer?'
            title = 'Location Options'
            options = ['Oakland', 'Shadyside', 'Squirrel Hill']
            response = choose(message, title, options)
            if response in options: 
                app.choiceTwo = response 
                break
            message = 'Please choose an option listed'
            title = 'Try Again'
            messagebox.showinfo(title, message) 
        if response == 'Oakland': 
            All = ['The Porch at Schenley', 'Chipotle', 'Piada', 'Zen Noodle House', 'Tamarind Flavor of India']
            rand = random.choice(All)
            if rand == 'The Porch at Schenley': 
                app.rest = 'The Porch at Schenley'
                app.location = 'Oakland'
                url = 'https://www.dineattheporch.com/schenley/menu'
                food = Porch(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
            elif rand == 'Chipotle': 
                app.rest = 'Chipotle'
                app.location = 'Oakland'
                url = 'https://www.menuwithprice.com/menu/chipotle-mexican-grill/'
                food = Chipotle(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
            elif rand == 'Piada': 
                app.rest = 'Piada'
                app.location = 'Oakland'
                url = 'https://mypiada.com/menu/oakland'
                food = Piada(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
            elif rand == 'Zen Noodle House': 
                app.rest = 'Zen Noodle House'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
                food = Zen(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
            elif rand == 'Tamarind Flavor of India': 
                app.rest = 'Tamarind Flavor of India'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
                food = Tamarind(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
        if response == 'Shadyside': 
            All = ['Mercurios', 'Fujiya'] 
            rand = random.choice(All)
            if rand == 'Mercurios': 
                app.rest = 'Mercurios'
                app.location = 'Shadyside'
                url = 'https://mercurios.menufy.com/#/'
                food = Mercurios(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
            elif rand == 'Fujiya': 
                app.rest = 'Fujiya'
                app.location = 'Shadyside'
                url = 'http://www.fujiyaramenpa.com/menu.htm'
                food = Fujiya(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
        if response == 'Squirrel Hill':
            All = ['Waffallonia'] 
            rand = random.choice(All)
            if rand == 'Waffallonia': 
                app.rest = 'Waffallonia'
                app.location = 'Squirrel Hill'
                url = 'https://www.waffallonia.com/index.php/menu'
                food = Waffallonia(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
    if response == 'Price':
        app.choice = app.choiceThree 
        while True:
            message = 'What is your price range?'
            title = 'Price Options'
            options = ['$', '$$', '$$$']
            response = choose(message, title, options)
            if response in options: 
                app.choiceTwo = response 
                break
            message = 'Please choose an option listed'
            title = 'Try Again'
            messagebox.showinfo(title, message) 
        if response == '$': 
            All = ['Waffallonia', 'Chipotle', 'Piada']
            rand = random.choice(All)
            if rand == 'Waffallonia': 
                app.rest = 'Waffallonia'
                app.location = 'Squirrel Hill'
                url = 'https://www.waffallonia.com/index.php/menu'
                food = Waffallonia(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price)) 
            if rand == 'Chipotle': 
                app.rest = 'Chipotle'
                app.location = 'Oakland'
                url = 'https://www.menuwithprice.com/menu/chipotle-mexican-grill/'
                food = Chipotle(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price)) 
            if rand == 'Piada': 
                app.rest = 'Piada'
                app.location = 'Oakland'
                url = 'https://mypiada.com/menu/oakland'
                food = Piada(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
        if response == '$$': 
            All = ['Fujiya', 'The Porch at Schenley', 'Zen Noodle House', 'Tamarind Flavor of India']
            rand = random.choice(All)
            if rand == 'Fujiya': 
                app.rest = 'Fujiya'
                app.location = 'Shadyside'
                url = 'http://www.fujiyaramenpa.com/menu.htm'
                food = Fujiya(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price)) 
            if rand == 'The Porch at Schenley': 
                app.rest = 'The Porch at Schenley'
                app.location = 'Oakland'
                url = 'https://www.dineattheporch.com/schenley/menu'
                food = Porch(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
            if rand == 'Zen Noodle House': 
                app.rest = 'Zen Noodle House'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
                food = Zen(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
            if rand == 'Tamarind Flavor of India': 
                app.rest = 'Tamarind Flavor of India'
                app.location = 'Oakland'
                url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
                food = Tamarind(url)
                app.name = '\n\n'.join(map(str, food.name)) 
                app.prices = '\n\n'.join(map(str, food.price))
        if response == '$$$': 
            All = ['Mercurios']
            rand = random.choice(All)
            if rand == 'Mercurios': 
                app.rest = 'Mercurios'
                app.location = 'Shadyside'
                url = 'https://mercurios.menufy.com/#/'
                food = Mercurios(url)
                app.name = '\n'.join(map(str, food.name)) 
                app.prices = '\n'.join(map(str, food.price))
    #update file with user's choices
    with open('Account.txt', 'r+') as f:
        text = f.read()
        new = app.username+'-'+app.password+'-'+app.rest
        old = app.username+'-'+app.password
        text = re.sub(old, new, text)
        f.seek(0)
        f.write(text)
        f.truncate()

def menuKeyPressed(app, event): 
    if (event.key == 'r'): 
        app.anotherMenu = not app.anotherMenu

#suggestions mode 
def SuggestionsKeyPressed(app, event): 
    if event.key == 'Left': 
        app.menuCurr = app.menuOptions[0]


def SuggestedRedrawAll(app, canvas): 
        cx, cy = app.width, app.height
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "peach puff")
        canvas.create_text(app.width/2, app.height/12, text = 'Suggested Restaurants', 
                            font = 'Courier 39 bold', fill = 'black')
        canvas.create_text(app.width/2, app.height/6, text = 'Other restaurants you might enjoy based off of what you chose - taste, location, or price', 
                            font = 'Courier 16 bold', fill = 'black') 
        userPlace = 'Similar restaurants to ' + str(app.place) + ' are:'
        canvas.create_text(app.width/2, app.height/4.5, text = userPlace, 
                            font = 'Courier 18 bold', fill = 'black')
        recommend = app.recommend
        canvas.create_text(app.width/2, app.height/2, text = recommend, 
                            font = 'Courier 18 bold', fill = 'black')
        #first recommendation
        if app.rOne == 'Piada': 
            canvas.create_image(120, 550, image = app.piadaImage)
        if app.rOne == 'The Porch at Schenley': 
            canvas.create_image(120, 550, image = app.porchImage)
        if app.rOne == 'Mercurios':
            canvas.create_image(120, 550, image = app.mercuriosImage)
        if app.rOne == 'Waffallonia':
            canvas.create_image(120, 550, image = app.waffalloniaImage)
        if app.rOne == 'Chipotle':
            canvas.create_image(120, 550, image = app.chipotleImage)
        if app.rOne == 'Fujiya':
            canvas.create_image(120, 550, image = app.fujiyaImage)
        if app.rOne == 'Zen Noodle House':
            canvas.create_image(120, 550, image = app.zenImage)
        if app.rOne == 'Tamarind Flavor of India':
            canvas.create_image(120, 550, image = app.tamarindImage)
        if app.rOne == 'Subway':
            canvas.create_image(120, 550, image = app.subwayImage)
        if app.rOne == 'Chikn':
            canvas.create_image(120, 550, image = app.chiknImage)
        if app.rOne == 'Five Guys':
            canvas.create_image(120, 550, image = app.fiveguysImage)
        if app.rOne == 'Cafe Moulim':
            canvas.create_image(120, 550, image = app.moulinImage)
        if app.rOne == 'Honeygrow':
            canvas.create_image(120, 550, image = app.honeygrowImage)
        if app.rOne == 'McDonalds':
            canvas.create_image(120, 550, image = app.mcdImage)
        #second recommendation
        if app.rTwo == 'Piada': 
            canvas.create_image(300, 700, image = app.piadaImage)
        if app.rTwo == 'The Porch at Schenley': 
            canvas.create_image(300, 700, image = app.porchImage)
        if app.rTwo == 'Mercurios':
            canvas.create_image(300, 700, image = app.mercuriosImage)
        if app.rTwo == 'Waffallonia':
            canvas.create_image(300, 700, image = app.waffalloniaImage)
        if app.rTwo == 'Chipotle':
            canvas.create_image(300, 700, image = app.chipotleImage)
        if app.rTwo == 'Fujiya':
            canvas.create_image(300, 700, image = app.fujiyaImage)
        if app.rTwo == 'Zen Noodle House':
            canvas.create_image(300, 700, image = app.zenImage)
        if app.rTwo == 'Tamarind Flavor of India':
            canvas.create_image(300, 700, image = app.tamarindImage)
        if app.rTwo == 'Subway':
            canvas.create_image(300, 700, image = app.subwayImage)
        if app.rTwo == 'Chikn':
            canvas.create_image(300, 700, image = app.chiknImage)
        if app.rTwo == 'Five Guys':
            canvas.create_image(300, 700, image = app.fiveguysImage)
        if app.rTwo == 'Cafe Moulim':
            canvas.create_image(300, 700, image = app.moulinImage)
        if app.rTwo == 'Honeygrow':
            canvas.create_image(300, 700, image = app.honeygrowImage)
        if app.rTwo == 'McDonalds':
            canvas.create_image(300, 700, image = app.mcdImage)
        #third recommendation   
        if app.rThree == 'Piada': 
            canvas.create_image(500, 550, image = app.piadaImage)
        if app.rThree == 'The Porch at Schenley': 
            canvas.create_image(500, 550, image = app.porchImage)
        if app.rThree == 'Mercurios':
            canvas.create_image(500, 550, image = app.mercuriosImage)
        if app.rThree == 'Waffallonia':
            canvas.create_image(500, 550, image = app.waffalloniaImage)
        if app.rThree == 'Chipotle':
            canvas.create_image(500, 550, image = app.chipotleImage)
        if app.rThree == 'Fujiya':
            canvas.create_image(500, 550, image = app.fujiyaImage)
        if app.rThree == 'Zen Noodle House':
            canvas.create_image(500, 550, image = app.zenImage)
        if app.rThree == 'Tamarind Flavor of India':
            canvas.create_image(500, 550, image = app.tamarindImage)
        if app.rThree == 'Subway':
            canvas.create_image(500, 550, image = app.subwayImage)
        if app.rThree == 'Chikn':
            canvas.create_image(500, 550, image = app.chiknImage)
        if app.rThree == 'Five Guys':
            canvas.create_image(500, 550, image = app.fiveguysImage)
        if app.rThree == 'Cafe Moulim':
            canvas.create_image(500, 550, image = app.moulinImage)
        if app.rThree == 'Honeygrow':
            canvas.create_image(500, 550, image = app.honeygrowImage)
        if app.rThree == 'McDonalds':
            canvas.create_image(500, 550, image = app.mcdImage)
        #fourth recommendation
        if app.rFour == 'Piada': 
            canvas.create_image(650, 700, image = app.piadaImage)
        if app.rFour == 'The Porch at Schenley': 
            canvas.create_image(650, 700, image = app.porchImage)
        if app.rFour == 'Mercurios':
            canvas.create_image(650, 700, image = app.mercuriosImage)
        if app.rFour == 'Waffallonia':
            canvas.create_image(650, 700, image = app.waffalloniaImage)
        if app.rFour == 'Chipotle':
            canvas.create_image(650, 700, image = app.chipotleImage)
        if app.rFour == 'Fujiya':
            canvas.create_image(650, 700, image = app.fujiyaImage)
        if app.rFour == 'Zen Noodle House':
            canvas.create_image(650, 700, image = app.zenImage)
        if app.rFour == 'Tamarind Flavor of India':
            canvas.create_image(650, 700, image = app.tamarindImage)
        if app.rFour == 'Subway':
            canvas.create_image(650, 700, image = app.subwayImage)
        if app.rFour == 'Chikn':
            canvas.create_image(650, 700, image = app.chiknImage)
        if app.rFour == 'Five Guys':
            canvas.create_image(650, 700, image = app.fiveguysImage)
        if app.rFour == 'Cafe Moulim':
            canvas.create_image(700, 700, image = app.moulinImage)
        if app.rFour == 'Honeygrow':
            canvas.create_image(750, 700, image = app.honeygrowImage)
        if app.rFour == 'McDonalds':
            canvas.create_image(700, 700, image = app.mcdImage)
        #fifth recommendation
        if app.rFive == 'Piada': 
            canvas.create_image(850, 550, image = app.piadaImage)
        if app.rFive == 'The Porch at Schenley': 
            canvas.create_image(850, 550, image = app.porchImage)
        if app.rFive == 'Mercurios':
            canvas.create_image(850, 550, image = app.mercuriosImage)
        if app.rFive == 'Waffallonia':
            canvas.create_image(850, 550, image = app.waffalloniaImage)
        if app.rFive == 'Chipotle':
            canvas.create_image(850, 550, image = app.chipotleImage)
        if app.rFive == 'Fujiya':
            canvas.create_image(850, 550, image = app.fujiyaImage)
        if app.rFive == 'Zen Noodle House':
            canvas.create_image(850, 550, image = app.zenImage)
        if app.rFive == 'Tamarind Flavor of India':
            canvas.create_image(850, 550, image = app.tamarindImage)
        if app.rFive == 'Subway':
            canvas.create_image(850, 550, image = app.subwayImage)
        if app.rFive == 'Chikn':
            canvas.create_image(850, 550, image = app.chiknImage)
        if app.rFive == 'Five Guys':
            canvas.create_image(850, 550, image = app.fiveguysImage)
        if app.rFive == 'Cafe Moulim':
            canvas.create_image(850, 550, image = app.moulinImage)
        if app.rFive == 'Honeygrow':
            canvas.create_image(850, 550, image = app.honeygrowImage)
        if app.rFive == 'McDonalds':
            canvas.create_image(850, 550, image = app.mcdImage)

def Recommendations(app): 
    if app.choiceThree == 'Taste': 
        if app.rest in Y: 
            index = Y.index(app.rest)
            coordinate = X[index]
            choice = coordinate
            AnswerOne = KNN(choice, X, Y, 1)
            app.place = '\n'.join(map(str, AnswerOne))
            AnswerTwo = KNN(choice, X, Y, 5)
            app.recommend = '\n\n'.join(map(str, AnswerTwo))
            for x in AnswerTwo: 
                if x == AnswerTwo[0]: 
                    app.rOne = AnswerTwo[0]
                if x == AnswerTwo[1]: 
                    app.rTwo = AnswerTwo[1] 
                if x == AnswerTwo[2]: 
                    app.rThree = AnswerTwo[2] 
                if x == AnswerTwo[3]: 
                    app.rFour = AnswerTwo[3]
                if x == AnswerTwo[4]: 
                    app.rFive = AnswerTwo[4]    
    if app.choiceThree == 'Location': 
         if app.rest in Y: 
            index = Y.index(app.rest)
            coordinate = Z[index]
            choice = coordinate
            AnswerOne = KNN(choice, Z, Y, 1)
            app.place = '\n'.join(map(str, AnswerOne))
            AnswerTwo = KNN(choice, Z, Y, 5)
            app.recommend = '\n\n'.join(map(str, AnswerTwo))
    if app.choiceThree == 'Price': 
        if app.rest in Y: 
            index = Y.index(app.rest)
            coordinate = V[index]
            choice = coordinate
            AnswerOne = KNN(choice, V, Y, 1)
            app.place = '\n'.join(map(str, AnswerOne))
            AnswerTwo = KNN(choice, V, Y, 5)
            app.recommend = '\n\n'.join(map(str, AnswerTwo))

#More Info mode 
def MoreKeyPressed(app, event): 
    if event.key == 'Left': 
        app.menuCurr = app.menuOptions[0]  

def MoreRedrawAll(app, canvas): 
        cx, cy = app.width, app.height
        canvas.create_rectangle(0, 0, cx, cy, fill = "peach puff")
        canvas.create_text(app.width/2, app.height/16, text = 'More Information', 
                            font = 'Courier 39 bold', fill = 'black')
        canvas.create_text(app.width/2, app.height/10, text = 'Select a restauarnt to view its address and number', 
                            font = 'Courier 24 bold', fill = 'black') 

        canvas.create_rectangle(cx/10-75, cy/4-70, cx/10+75, cy/4+90, width = 0)
        canvas.create_image(100, 210, image = app.piadaImage)
        if app.morePiada:
            canvas.create_text(cx/3.2, cy/4,text=app.addressPiada,
                                font='Arial 10 bold')
            canvas.create_text(cx/3.5, cy/3.5,text=app.numberPiada,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/9-100, cy/2.5-15, cx/9+115, cy/2.5+100, width = 0)
        canvas.create_image(120, 360, image = app.porchImage)
        if app.morePorch:
            canvas.create_text(cx/2.8, cy/2.5,text=app.addressPorch,
                                font='Arial 10 bold')
            canvas.create_text(cx/3.4, cy/2.3,text=app.numberPorch,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/9-100, cy/1.75-10, cx/9+115, cy/1.75+100, width = 0)
        canvas.create_image(120, 500, image = app.mercuriosImage)
        if app.moreMercurios:
            canvas.create_text(cx/2.8, cy/1.7,text=app.addressMercurios,
                                font='Arial 10 bold')
            canvas.create_text(cx/3.4, cy/1.6,text=app.numberMercurios,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/9-100, cy/1.35-5, cx/9+115, cy/1.35+110, width = 0)
        canvas.create_image(120, 650, image = app.fujiyaImage)
        if app.moreFujiya:
            canvas.create_text(cx/2.8, cy/1.29,text= app.addressFujiya,
                                font='Arial 10 bold')
            canvas.create_text(cx/3.4, cy/1.2,text=app.numberFujiya,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/1.7-100, cy/4.5-10, cx/1.7+115, cy/4.5+80, width = 0)
        canvas.create_image(600, 210, image = app.waffalloniaImage)
        canvas.create_text(cx/1.2, cy/4,text= app.addressWaffallonia,
                                    font='Arial 10 bold')
        canvas.create_text(cx/1.2, cy/3.5,text=app.numberWaffallonia,
                                    font='Arial 10 bold')

        canvas.create_rectangle(cx/1.7-100, cy/2.5-30, cx/1.7+115, cy/2.5+110, width = 0)
        canvas.create_image(600, 360, image = app.chipotleImage)
        if app.moreChipotle:
            canvas.create_text(cx/1.2, cy/2.5,text=app.addressChipotle,
                                font='Arial 10 bold')
            canvas.create_text(cx/1.2, cy/2.3,text=app.numberChipotle,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/1.7-70, cy/1.7-15, cx/1.7+80, cy/1.7+115, width = 0)
        canvas.create_image(600, 520, image = app.zenImage)
        if app.moreZen:
            canvas.create_text(cx/1.2, cy/1.6,text=app.addressZen,
                                font='Arial 10 bold')
            canvas.create_text(cx/1.2, cy/1.5,text=app.numberZen,
                                font='Arial 10 bold')

        canvas.create_rectangle(cx/1.7-100, cy/1.3-15, cx/1.7+120, cy/1.3+110, width = 0)
        canvas.create_image(600, 670, image = app.tamarindImage)
        if app.moreTamarind:
            canvas.create_text(cx/1.2, cy/1.2,text=app.addressTamarind,
                                font='Arial 10 bold')
            canvas.create_text(cx/1.2, cy/1.15,text=app.numberTamarind,
                                font='Arial 10 bold')

def lowHigh(app): 
    if app.rest == 'The Porch at Schenley': #done
        url = 'https://www.dineattheporch.com/schenley/menu'
        food = Porch(url)
        nameList = food.name 
        priceList = food.price
        priceList = [int(i) for i in priceList]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n'.join(map(str, nameSorted)) 
        app.prices = '\n'.join(map(str, sortPriceList))

    if app.rest == 'Mercurios': #done 
        url = 'https://mercurios.menufy.com/#/'
        food = Mercurios(url)
        nameList = food.name 
        priceList = food.price
        removeOne = [x.strip('$') for x in priceList]
        removeTwo = [x.strip('+') for x in removeOne]
        priceList = [float(i) for i in removeTwo]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n'.join(map(str, nameSorted)) 
        app.prices = '\n'.join(map(str, sortPriceList))

    if app.rest == 'Fujiya': #done
        url = 'http://www.fujiyaramenpa.com/menu.htm'
        food = Fujiya(url)
        nameList = food.name 
        priceList = food.price
        remove = [x.strip('$') for x in priceList]
        priceList = [float(i) for i in remove]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n\n'.join(map(str, nameSorted)) 
        app.prices = '\n\n'.join(map(str, sortPriceList))

    if app.rest == 'Zen Noodle House': #done
        url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
        food = Zen(url)
        nameList = food.name 
        priceList = food.price
        remove = [x.strip('$') for x in priceList]
        priceList = [float(i) for i in remove]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n\n'.join(map(str, nameSorted)) 
        app.prices = '\n\n'.join(map(str, sortPriceList)) 

    if app.rest == 'Tamarind Flavor of India': #done
        url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
        food = Tamarind(url)
        nameList = food.name 
        priceList = food.price
        remove = [x.strip('$') for x in priceList]
        priceList = [float(i) for i in remove]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n\n'.join(map(str, nameSorted)) 
        app.prices = '\n\n'.join(map(str, sortPriceList))

    if app.rest == 'Chipotle': #done
        url = 'https://www.menuwithprice.com/menu/chipotle-mexican-grill/'
        food = Chipotle(url)
        nameList = food.name 
        priceList = food.price
        remove = [x.strip('$') for x in priceList]
        priceList = [float(i) for i in remove]
        sortPriceList = sorted(priceList, key = int)
        match = zip(priceList, nameList)
        sorting = sorted(match)
        nameSorted = [names for x, names in sorting]
        app.name = '\n\n'.join(map(str, nameSorted)) 
        app.prices = '\n\n'.join(map(str, sortPriceList))
def moreMousePressed(app, event): 
    cx,cy = app.width, app.height
    if((cx/10-75 <= event.x <= cx/10+75) and (cy/4-70 <= event.y <= cy/4+90)): 
        app.morePiada = not app.morePiada
    if((cx/9-100 <= event.x <= cx/9+115) and (cy/2.5-15 <= event.y <= cy/2.5+100)): 
        app.morePorch = not app.morePorch
    if((cx/9-100 <= event.x <= cx/9+115) and (cy/1.75-10 <= event.y <= cy/1.75+100)): 
        app.moreMercurios = not app.moreMercurios
    if((cx/9-100 <= event.x <= cx/9+115) and (cy/1.35-5 <= event.y <= cy/1.35+110)): 
        app.moreFujiya = not app.moreFujiya
    if((cx/1.7-100 <= event.x <= cx/1.7+115) and (cy/4.5-10 <= event.y <= cy/4.5+80)): 
        app.moreWaffallonia = not app.moreWaffallonia
    if((cx/1.7-100 <= event.x <= cx/1.7+115) and (cy/2.5-30 <= event.y <= cy/2.5+110)): 
        app.moreChipotle = not app.moreChipotle
    if((cx/1.7-70 <= event.x <= cx/1.7+80) and (cy/1.7-15 <= event.y <= cy/1.7+115)): 
        app.moreZen = not app.moreZen
    if((cx/1.7-100 <= event.x <= cx/1.7+120) and (cy/1.3-15 <= event.y <= cy/1.3+110)): 
        app.moreTamarind = not app.moreTamarind
    
def displayMorePiada(app): 
    url = 'https://mypiada.com/menu/oakland'
    food = morePiada(url)
    app.addressPiada = '\n'.join(map(str, food.address)) 
    app.numberPiada = food.number

def displayMorePorch(app): 
    url = 'https://www.dineattheporch.com/schenley/about'
    food = morePorch(url)
    app.addressPorch = '\n'.join(map(str, food.address)) 
    app.numberPorch = '\n'.join(map(str, food.number))

def displayMoreMercurios(app): 
    url = 'https://mercurios.menufy.com/#/'
    food = moreMercurios(url)
    app.addressMercurios = '\n'.join(map(str, food.address)) 
    app.numberMercurios = '\n'.join(map(str, food.number))

def displayMoreWaffallonia(app): 
    url = 'http://places.singleplatform.com/waffallonia/menu?ref=google' 
    food = moreWaffallonia(url)
    app.addressWaffallonia = '\n'.join(map(str, food.address)) 
    app.numberWaffallonia = '\n'.join(map(str, food.number))

def displayMoreFujiya(app): 
    url = 'http://places.singleplatform.com/fujiya-ramen-0/menu?ref=google' 
    food = moreFujiya(url)
    app.addressFujiya = '\n'.join(map(str, food.address)) 
    app.numberFujiya = '\n'.join(map(str, food.number))

def displayMoreZen(app): 
    url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
    food = moreZen(url)
    app.addressZen = '\n'.join(map(str, food.address)) 
    app.numberZen = '\n'.join(map(str, food.number))

def displayMoreChipotle(app): 
    url = 'https://locations.chipotle.com/pa/pittsburgh/4611-forbes-ave'
    food = moreChipotle(url)
    app.addressChipotle = '\n'.join(map(str, food.address)) 
    app.numberChipotle = '\n'.join(map(str, food.number))

def displayMoreTamarind(app): 
    url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
    food = moreTamarind(url)
    app.addressTamarind = '\n'.join(map(str, food.address)) 
    app.numberTamarind= '\n'.join(map(str, food.number))

#past menu mode 
def PastKeyPressed(app, event): 
    if event.key == 'Left': 
        app.menuCurr = app.menuOptions[0]

def PastMenuRedrawAll(app, canvas): 
        canvas.create_rectangle(0, 0, app.width, app.height, fill = "peach puff")
        canvas.create_text(app.width/2, app.height/12, text = 'Your Menu from Last Time', 
                            font = 'Courier 39 bold', fill = 'black')

        msg = "Last time your restaurant was: " + str(app.updateRest)
        canvas.create_text(app.width/2, app.height/6, text = msg, 
                            font = 'Courier 18 bold', fill = 'black')
        Location = 'This is Located in: ' + app.location                   
        canvas.create_text(app.width/2, app.height/4.3, text = Location, 
                            font = 'Courier 16 bold', fill = 'black')

        canvas.create_text(app.width/6, app.height/3.4, text = "Food Names:", 
                            font = 'Courier 18 bold', fill = 'black')
        foodNames = app.namePast
        canvas.create_text(app.width/6, app.height/1.6, text = foodNames, 
                            font = 'Courier 12 bold', fill = 'black')

        canvas.create_text(app.width/1.2, app.height/3.4, text = "Prices($):", 
                            font = 'Courier 18 bold', fill = 'black')
        foodPrices = app.pricesPast
        canvas.create_text(app.width/1.2, app.height/1.6, text = foodPrices, 
                            font = 'Courier 12 bold', fill = 'black')
        if app.updateRest == 'Piada': 
            canvas.create_image(500, 400, image = app.piadaImage)
        if app.updateRest == 'The Porch at Schenley': 
            canvas.create_image(500, 400, image = app.porchImage)
        if app.updateRest == 'Mercurios':
            canvas.create_image(500, 400, image = app.mercuriosImage)
        if app.updateRest == 'Waffallonia':
            canvas.create_image(500, 400, image = app.waffalloniaImage)
        if app.updateRest == 'Chipotle':
            canvas.create_image(500, 400, image = app.chipotleImage)
        if app.updateRest == 'Fujiya':
            canvas.create_image(500, 400, image = app.fujiyaImage)
        if app.updateRest == 'Zen Noodle House':
            canvas.create_image(500, 400, image = app.zenImage)
        if app.updateRest == 'Tamarind Flavor of India':
            canvas.create_image(500, 400, image = app.tamarindImage)
            
def Past(app): 
    if app.userCount == 1: 
        file = open('Account.txt', 'r')
        for row in file: 
            space = row.split('-') 
            app.updateRest = space[2]       
    else: 
        file = open('Account.txt', 'r')
        for row in file: 
            space = row.split('-') 
            if len(space) > 3: 
                if app.username in space:
                    app.updateRest = space[3]
    if app.updateRest == ListOfRestaurants[0]: 
        app.location = 'Oakland'
        url = 'https://www.dineattheporch.com/schenley/menu'
        food = Porch(url)
        app.namePast = '\n'.join(map(str, food.name)) 
        app.pricesPast = '\n'.join(map(str, food.price)) 
    elif app.updateRest == ListOfRestaurants[1]: 
        app.location = 'Oakland'
        url = 'https://www.menuwithprice.com/menu/chipotle-mexican-grill/'
        food = Chipotle(url)
        app.namePast = '\n'.join(map(str, food.name)) 
        app.pricesPast = '\n'.join(map(str, food.price)) 
    elif app.updateRest == ListOfRestaurants[2]: 
        app.location = 'Squirrel Hill'
        url = 'https://www.waffallonia.com/index.php/menu'
        food = Waffallonia(url)
        app.namePast = '\n\n'.join(map(str, food.name)) 
        app.pricesPast = '\n\n'.join(map(str, food.price)) 
    elif app.updateRest == ListOfRestaurants[3]: 
        app.location = 'Oakland'
        url = 'https://mypiada.com/menu/oakland'
        food = Piada(url)
        app.namePast = '\n\n'.join(map(str, food.name)) 
        app.pricesPast = '\n\n'.join(map(str, food.price))
    elif app.updateRest == ListOfRestaurants[4]: 
        app.location = 'Shadyside'
        url = 'https://mercurios.menufy.com/#/'
        food = Mercurios(url)
        app.namePast = '\n'.join(map(str, food.name)) 
        app.pricesPast = '\n'.join(map(str, food.price)) 
    elif app.updateRest == ListOfRestaurants[5]: 
        app.location = 'Shadyside'
        url = 'http://www.fujiyaramenpa.com/menu.htm'
        food = Fujiya(url)
        app.namePast = '\n\n'.join(map(str, food.name)) 
        app.pricesPast = '\n\n'.join(map(str, food.price)) 
    elif app.updateRest == ListOfRestaurants[6]: 
        app.location = 'Oakland'
        url = 'http://places.singleplatform.com/zen-noodle-house/menu?ref=google'
        food = Zen(url)
        app.namePast = '\n\n'.join(map(str, food.name)) 
        app.pricesPast = '\n\n'.join(map(str, food.price))
    elif app.updateRest == ListOfRestaurants[7]:
        app.rest = 'Tamarind Flavor of India'
        app.location = 'Oakland'
        url = 'http://places.singleplatform.com/tamarind-flavor-of-india/menu?ref=google'
        food = Tamarind(url)
        app.namePast = '\n\n'.join(map(str, food.name)) 
        app.pricesPast = '\n\n'.join(map(str, food.price))
                              
######################
#runs everything
######################
runApp(width=1000, height=800)