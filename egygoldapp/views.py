from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.http import HttpResponse
from django.contrib import messages
import datetime
from .models import Post,Comment,Contact
from .forms import NowComment
# start import library to web scraping
import requests
import pandas as pd
import pandas
from bs4 import BeautifulSoup

# end import library to web scraping

# coding: utf-8
def maksoup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def Scrpe_EgyptGold():
    link="https://egypt.gold-price-today.com/"
    soup = maksoup(link)
    get_divs = soup.find_all('div')
    title = get_divs[0]
    title = title.find_all('p')
    title = title[1].text
    tables = soup.find_all('table')
    list = []
    list1 =[]
    list2 =[]
    list3 =[]
    list4 =[]
    def get_tableData():
        i = 1
        for table in tables:
            if i == 1:
                for team in table.find_all('tbody'):
                    rows = team.find_all('tr')
                    c = 1
                    for row in rows:
                        d = {}
                        if c<=3:
                            d['td1'] = row.find('th').text
                            d['td2'] = row.find('td').text
                            list.append(d)
                            c =c+1
                        else:
                            if c<=6:
                                d['td1'] = row.find('th').text
                                d['td2'] = row.find('td').text
                                list1.append(d)
                                c = c+1
                            else:
                                d['td1'] = row.find('th').text
                                d['td2'] = row.find('td').text
                                list2.append(d)
                                
            if i == 2:
                tfoot_text = table.find('tfoot').text
                for team in table.find_all('tbody'):
                    rows = team.find_all('tr')
                    for row in rows:
                        d = {}
                        d['th'] = row.find('th').text
                        tds = row.find_all('td')
                        d['td1'] = tds[0].text
                        d['td2'] = tds[1].text
                        list3.append(d)

            if i == 3:
                for team in table.find_all('tbody'):
                    rows = team.find_all('tr')
                    for row in rows:
                        d = {}
                        d['th'] = row.find('th').text
                        tds = row.find_all('td')
                        d['td1'] = tds[0].text
                        d['td2'] = tds[1].text
                        d['td3'] = tds[2].text
                        d['td4'] = tds[3].text
                        d['td5'] = tds[4].text
                        list4.append(d)

            i = i+1
        return list,list1,list2,list3,tfoot_text,list4 
    list,list1,list2,list3,tfoot_text,list4  = get_tableData() 
    return list,list1,list2,list3,tfoot_text,list4,title
        
def ScrpeData_allCountries(url):
    soup = maksoup(url)
    get_divs = soup.find_all('div')
    title = get_divs[0]
    title = title.find_all('p')
    title = title[1].text
    box = soup.find('img').get('src')
    tables = soup.find_all('table')
    list = []
    list1 = []
    i = 1
    for table in tables:
        if i == 1:
            rows = table.find('tbody').find_all('tr')
            tfoot_text = table.find('tfoot').text 
            for row in rows:
                d ={}
                d['th'] = row.find('th').text
                tds = row.find_all('td')
                d['td'] = tds[0].text
                d['td1'] = tds[1].text
                list.append(d)
        
        if i == 2:
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                d ={}
                d['th'] = row.find('th').text
                tds = row.find_all('td')
                d['td'] = tds[0].text
                d['td1'] = tds[1].text
                d['td2'] = tds[2].text
                d['td3'] = tds[3].text
                d['td4'] = tds[4].text
                list1.append(d)
        i = i+1
    return list,list1,tfoot_text,title,box

def ScrpeData_goldpricestoday(url):
    soup = maksoup(url)
    get_divs = soup.find_all('div')
    title = get_divs[0]
    title = title.find_all('p')
    title = title[1].text
    tables = soup.find_all('table')
    list = []
    list1 = []
    i = 1
    for table in tables:
        if i == 1:
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                d ={}
                tds = row.find_all('td')
                d['td'] = tds[0].text
                list.append(d)
        if i == 2:
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                d ={}
                d['th'] = row.find('th').text
                tds = row.find_all('td')
                d['td'] = tds[0].text
                d['td1'] = tds[1].text
                d['td2'] = tds[2].text
                d['td3'] = tds[3].text
                d['td4'] = tds[4].text
                list1.append(d)
        i = i+1
    return list,list1,title

def ScrpeData_goldpricestoday_egy(url):
    soup = maksoup(url)
    get_divs = soup.find_all('div')
    title = get_divs[0]
    title = title.find_all('p')
    title = title[1].text
    tables = soup.find_all('table')
    list = []
    list1 = []
    i = 1
    for table in tables:
        if i == 2:
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                d ={}
                tds = row.find_all('td')
                d['td'] = tds[0].text
                list.append(d)
        if i == 3:
            rows = table.find('tbody').find_all('tr')
            for row in rows:
                d ={}
                d['th'] = row.find('th').text
                tds = row.find_all('td')
                d['td'] = tds[0].text
                d['td1'] = tds[1].text
                d['td2'] = tds[2].text
                d['td3'] = tds[3].text
                d['td4'] = tds[4].text
                list1.append(d)
        i = i+1
    return list,list1,title

def ScrapGoldPriceForecast(url):
    list = []
    soup = maksoup(url)
    tables = soup.find_all('table')
    table = tables[2]
    rows = table.find_all('tr')
    i = 1
    for row in rows:
        if i !=1:
            d = {}
            datas = row.find_all('td')
            d['td'] = datas[0].text
            d['td1'] = datas[1].text
            d['td2'] = datas[2].text
            d['td3'] = datas[3].text
            d['td4'] = datas[4].text
            list.append(d)
        i = 2
    return list

def ScrapDollarPricetoday(url):
    list = []
    list1 = []
    soup = maksoup(url)
    table = soup.find('table')
    theads = table.find_all('thead')
    for thead in theads[1]:
        d = {}
        rows = thead.find_all('td')
        try:
            d["td"] = rows[0].find('img').get('src')
        except:
            d["td"] = ""
        d["td1"] = rows[1].text
        d["td2"] = rows[2].text
        d["td3"] = rows[3].text
        d["td4"] = rows[4].text
        list1.append(d)
        
    tbody = table.find('tbody')
    rows = tbody.find_all('tr')

    for row in rows:
        d = {}
        tds = row.find_all('td')
        d["td"] = tds[0].find('img').get('src')
        d["td1"] = tds[1].text
        d["td2"] = tds[2].text
        d["td3"] = tds[3].text
        d["td4"] = tds[4].text
        list.append(d)

    text = soup.find('div',{'class':'jumbotron'})
    date = text.find('p').text
    span = text.find('span')
    span = span.find_all('h4')
    span1 = span[0].text
    span2 = span[1].text

    return list,list1,date,span,span1,span2
    

def get_title(url):
    soup = maksoup(url)
    get_divs = soup.find_all('div')
    title = get_divs[0]
    title = title.find_all('p')
    title = title[1].text
    return title

def home(request):
    x = datetime.datetime.now()
    now = x.strftime("%d-%m-%Y")
    try:
        posts,posts1,posts2,posts3,posts4,posts5,posts6 = Scrpe_EgyptGold()
        context = {
        'title': 'الصفحة الرئيسية',
        'posts':  posts,
        'posts1': posts1,
        'posts2': posts2,
        'posts3': posts3,
        'posts4': posts4,
        'posts5': posts5,
        'posts6': posts6,
        'date': now,
    }
    except:
        posts7 = 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py'
        context = {
            'title': 'الصفحة الرئيسية',
            'posts7':posts7,
            'date': now,
        }
    '''now =datetime.datetime.now()
    now = now.strftime("%y-%m-%d %H:%S")'''
    
    return render(request, 'egygoldapp/index.html',context)

def saudi(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://saudi-arabia.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في السعودية',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في السعودية',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/saudi.html',context)

def kuwait(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://kuwait.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في الكويت',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في الكويت',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/kuwait.html',context)

def UAE(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://united-arab-emirates.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في الإمارات',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في الإمارات',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/UAE.html',context)

def qatar(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://qatar.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في قطر',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في قطر',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/qatar.html',context)

def Jordan(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://jordan.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في الأردن',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في الأردن',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/Jordan.html',context)

def bahrain(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://bahrain.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في البحرين',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في البحرين',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/bahrain.html',context)

def Oman(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://oman.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في عمان',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في عمان',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/Oman.html',context)

def Palestine(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://palestine.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في فلسطين',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في فلسطين',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/Palestine.html',context)

def Iraq(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://iraq.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في العراق',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في العراق',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/Iraq.html',context)

def Lebanon(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://lebanon.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في لبنان',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في لبنان',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/Lebanon.html',context)

def algeria(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://algeria.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في الجزائر',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في الجزائر',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/algeria.html',context)

def morocco(request):
    try:
        posts,posts1,tfoot_text,title,box = ScrpeData_allCountries('https://morocco.gold-price-today.com/')
        context = {
            'title':'اسعار الذهب اليوم في المغرب',
            'posts': posts,
            'posts1': posts1,
            'posts2' : tfoot_text,
            'posts3' : title,
            'posts4': box
        }
    except:
        context = {
            'title':'اسعار الذهب اليوم في المغرب',
            'posts5': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }

    return render(request,'egygoldapp/morocco.html',context)

def goldpricestoday(request):
    x = datetime.datetime.now()
    now = x.strftime("%d-%m-%Y")
    now1 = now
    #hour = x.strftime("%p %H:%M")
    try:
        title = get_title("https://egypt.gold-price-today.com/")
        context= {
            'title':"أسعار الذهب اليوم",
            'titles': title,
            'date' : now,
            'date1': now1,
        }
    except:
         context= {
            'title':"أسعار الذهب اليوم",
            'error' : 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
        }

    return render(request,'egygoldapp/goldpricestoday.html', context)

def article(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%p %H:%M")
    link = "/static/images/egyp.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday_egy("https://egypt.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            elif i ==8:
                posts8 =lis['td']
            else:
                posts9 =lis['td']
            i = i+1
        context = {
            'title':'أسعار الذهب اليوم في مصر',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts8' : posts8,
            'posts9' : posts9,
            'posts10': list1,
            'titles' : title,
            'name' : 'مصر',
            'currency': 'جنيه مصرى',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في مصر',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_saudi(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/السعودية-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://saudi-arabia.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في السعودية',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'السعودية',
            'currency': ' الريال السعودي',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في  بالريال السعودي',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_kuwait(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/الكويت-1.png"    
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://kuwait.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في الكويت',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'الكويت',
            'currency': 'الدينار الكويتي',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في الكويت',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_uae(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/الامارات-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://united-arab-emirates.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في الإمارات',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'الإمارات',
            'currency': 'الدرهم الاماراتي',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في الإمارات',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_qatar(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/قطر-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://united-arab-emirates.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في قطر',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'قطر',
            'currency': 'الريال القطري',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في قطر',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_jordan(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/الأردن-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://united-arab-emirates.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في الأردن',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'الأردن',
            'currency': 'الدينار الاردني',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في الأردن',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_bahrain(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/البحرين-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://bahrain.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في البحرين',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'البحرين',
            'currency': 'الدينار البحريني',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في البحرين',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_oman(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link="/static/images/عمان-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://oman.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في عمان',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'عمان',
            'currency': 'الريال العماني',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في عمان',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_palestine(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/فلسطين-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://palestine.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في فلسطين',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'فلسطين',
            'currency': 'الشيكل',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في فلسطين',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_iraq(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/العراق-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://iraq.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في العراق',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'العراق',
            'currency': 'الدينار العراقي',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في العراق',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_lebanaon(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/لبنان-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://lebanon.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في لبنان',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'لبنان',
            'currency': 'الليرة اللبنانية',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في لبنان',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_algeria(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/الجزائر-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://algeria.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في الجزائر',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'الجزائر',
            'currency': 'الدينار الجزائري',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في الجزائر',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def article_marocco(request):
    x = datetime.datetime.now()
    now = x.strftime("%Y-%m-%d")
    now1 = x.strftime("%d-%m-%Y")
    hour = x.strftime("%H:%M%p")
    link = "/static/images/المغرب-1.png"
    try:
        list,list1,title = ScrpeData_goldpricestoday("https://morocco.gold-price-today.com/")
        i = 0
        for lis in list:
            if i ==0:
                posts = lis['td']
            elif i==1:
                posts1 = lis['td']
            elif i ==2:
                posts2 =lis['td']
            elif i ==3:
                posts3 =lis['td']
            elif i ==4:
                posts4 =lis['td']
            elif i ==5:
                posts5 =lis['td']
            elif i ==6:
                posts6 =lis['td']
            elif i ==7:
                posts7 =lis['td']
            else :
                posts8 =lis['td']
            i = i+1   
        context = {
            'title':'أسعار الذهب اليوم في المغرب',
            'posts' : posts,
            'posts2' : posts2,
            'posts3' : posts3,
            'posts4' : posts4,
            'posts5' : posts5,
            'posts7' : posts7,
            'posts8' : posts8,
            'posts10': list1,
            'titles' : title,
            'name' : 'المغرب',
            'currency': 'الدرهم المغربي',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    except:
        context ={
            'title':'أسعار الذهب اليوم في المغرب',
            'post': 'حدث خطأفي عملية سحب البيانات راجع ملف ال views.py',
            'date' : now,
            'date1': now1,
            'hour':hour,
            'hour':hour,
            'link': link,
        }
    return render(request, 'egygoldapp/article.html', context)

def about(request):
    context = {
        'title': 'من نحن',
    }
    return render(request,'egygoldapp/about.html',context)

def privacy(request):
    context = {
        'title': 'سياسة الخصوصية',
    }
    return render(request,'egygoldapp/privacy.html',context)

def GoldPriceForecast(request):
    try:
        list = ScrapGoldPriceForecast("https://thedollartoday.com/gold-price-forecast")
        context = {
            'title':'توقعات اسعار الذهب',
            'posts': list,

        }
    except:
        context = {
            'title':'توقعات اسعار الذهب',
            'error': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }
    return render(request,'egygoldapp/gold-price-forecast.html',context)

def BitcoinPriceForecast(request):
    try:
        list = ScrapGoldPriceForecast("https://thedollartoday.com/bitcoin-price-forecast")
        context = {
            'title':'توقعات سعر البيتكوين',
            'posts': list,

        }
    except:
        context = {
            'title':'توقعات سعر البيتكوين',
            'error': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }
    return render(request,'egygoldapp/bitcoin-price-forecast.html',context)

def DollarPricetoday(request):
    try:
        list,list1,date,span,span1,span2 = ScrapDollarPricetoday("https://eldolar.live/USD")
        context = {
            'title': 'سعر الدولار اليوم',
            'posts':list,
            'posts1':list1,
            'posts2': date,
            'posts3': span1,
            'posts4': span2,
            
        }
    except:
        context = {
            'title': 'سعر الدولار اليوم',
            'error': 'حدث خطأ في عملية سحب البيانات راجع ملف ال views.py',
        }
    return render(request,'egygoldapp/dollar-price-today.html',context)

def news(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)

    context = {
        'title': 'الاخبار',
        'posts': posts,
        'page': page,
    }
    return render(request,'egygoldapp/news.html',context)

def Post_detail(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form = NowComment()
    next_comment = None
    context = {
        'title': post,
        'post':post,
        'comments':comments,
        'comment_form': comment_form,
    }
    if request.method == 'POST':
        comment_form = NowComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NowComment()
            return render(request,'egygoldapp/comment_render.html')
        else:
            comment_form = NowComment()

    return render(request, 'egygoldapp/detail.html',context)

def contact_us(request):
    context = {
        'title': 'اتصل بنا',
    }
    contact = Contact()
    if request.method =="POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return  render(request,'egygoldapp/message.html')
   
    return render(request, 'egygoldapp/contact_us.html',context)