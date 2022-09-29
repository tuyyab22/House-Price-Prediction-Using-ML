
from distutils.log import error
import imp
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

import pandas as pd
import pickle 
from django.contrib import messages
import openpyxl
import pickle 
import locale

from .models import Liked
data=pd.pandas.read_csv('C:/Users/TUYYAB/OneDrive/Desktop/house prediction/House-price-prediction-ML/home/static/img/excel/Cleaned_data.csv')
pipe=pickle.load(open("C:/Users/TUYYAB/OneDrive/Desktop/house prediction/House-price-prediction-ML/home/RidgeModel2.pkl","rb"))
username=""
pickle.dump(username, open("username.dat", "wb"))
# Create your views here.

def signup(request):
    if request.method=='POST':
        uname=request.POST['uname']
        emailid=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['password1']
        if password1!=password2:
            print("not matching")
            messages.info(request,'PASSWORD NOT MATCHING')
        else:
            x=User.objects.create_user(username=uname,email=emailid,password=password1)
            x.save()
            return render(request,'login.html')
    return render(request,"register.html")

def login(request):
    locations=sorted(data['location'].unique())
    if request.method=='POST':
        uname=request.POST.get('lname')
        lpassword=request.POST.get('loginpass')
        user = authenticate(username=uname, password=lpassword)
        if user is not None:
            pickle.dump(uname, open("username.dat", "wb"))
            messages.info(request,'sproduct')
            return render(request,'dashboard.html',{'name':uname,'password':lpassword,'locations':locations})
        else:
            messages.error(request,"INVALID USERNAME OR PASSWORD")
            print(" no sucesss")
    return render(request,'login.html')


# def adddata(request):
#     locations=sorted(data['location'].unique())
#     if request.method=='POST':
#         aname=request.POST.get('location',False)
#         bh=request.POST.get('bhk',False)
#         size=request.POST.get('size',False)
#         bt=request.POST.get('bt',False)
#         parking=request.POST.get('parking',False)
#         duplex=request.POST.get('duplex',False)
#         balcony=request.POST.get('balcany',False)
#         amount=request.POST.get('amount',False)
#         filename='/home/shreyank/miniproject/mini/home/static/img/excel/final_version.xlsx'
#         print(aname,bh,size,bt,parking,duplex,balcony,amount)
#         wb=openpyxl.load_workbook(filename=filename)
#         sheet = wb['Sheet1']
#         new_row = [aname,size,bt,bh,duplex,parking,balcony,amount]
#         sheet.append(new_row)
#         wb.save(filename)
#     return render(request,'adddata.html',{'location':locations})

def sproduct(request):
    locations=sorted(data['location'].unique())
    username = pickle.load(open("username.dat", "rb"))
    print(username)
    dic={'name':username,'password':'GUEST','locations':locations}
    if request.method=='POST':
        aname=request.POST.get('location',False)
        areaname=aname
        bh=request.POST.get('bhk',0)
        gbhk=bh
        size=request.POST.get('size',0)
        bt=request.POST.get('bt',0)
        bathroom=bt
        parking=request.POST.get('parking',0)
        duplex=request.POST.get('duplex',0)
        balcony=request.POST.get('balcany',0)
        print(aname,bh,size,bt,parking,duplex,balcony)
        input=pd.DataFrame([[aname,size,bt,bh,duplex,parking,balcony]],columns=['location','total_sqft','bath','bhk','Duplex','Parking','Balcony'])
        answer=(round((pipe.predict(input)[0]*100000),3))
        locale.setlocale(locale.LC_MONETARY, 'en_IN')
        answer=locale.currency(answer, grouping=True)
        ganswer=answer
        if(parking=='0'):
            parking='No'
        else:
            parking='Yes'
        
        if(duplex=='0'):
            duplex='No'
        else:
            duplex='Yes'
        
        if(balcony=='0'):
            balcony='No'
        else:
            balcony='Yes'
        dict={'area':aname,'size':size,'bt':bt,'bhk':bh,'answer':answer,'locations':locations,'duplex':duplex,'parking':parking,'balcony':balcony,'like':'like'}
        messages.info(request,'like')
        return render(request,'answer.html',{'dict':dict})
    return render(request,"product.html",dic)

def productsearch(request):
    locations=sorted(data['location'].unique())
    username = pickle.load(open("username.dat", "rb"))
    dic={'name':username,'password':'GUEST','locations':locations,'like':'like'}
    if request.method=='POST':
        messages.info(request,'sproduct')
        return render(request,'dashboard.html',{'dict':dic})
    return render(request,'product.html')


def liked(request):
    
    if request.method=='POST':
        username = pickle.load(open("username.dat", "rb"))
        Size=request.POST.get('size')
        Bhk=request.POST.get('bhk')
        areaname=request.POST.get('area')
        Bathroom=request.POST.get('bath')
        Duplex=request.POST.get('duplex')
        Parking=request.POST.get('parking')
        Balcony=request.POST.get('balcony')
        Totalcost=request.POST.get('answer')
        
        
        data=Liked(username=username,areaname=areaname,bhk=Bhk,size=Size,bathroom=Bathroom,duplex=Duplex,parking=Parking,balcony=Balcony,totalcost=Totalcost)
        data.save()
        data1=Liked.objects.filter(username=username)
        return render(request,'likedpages.html',{'data':data1})
    


        



def likedpages(request):
    username = pickle.load(open("username.dat", "rb"))
    data=Liked.objects.filter(username=username)
    if request.method=='POST':
        messages.info(request,'likedpages')
        return render(request,'dashboard.html',{'data':data})
    return render(request,'likedpages.html',{'data':data})

def cpass(request):
    if request.method=='POST':
        username = pickle.load(open("username.dat", "rb"))
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            u = User.objects.get(username=username)
            u.set_password(password1)
            u.save()
            return render(request,'login.html')
    return render(request,'changepass.html')

def logoutuser(request):
    
    logout(request)
    return redirect('login')
        
    











    
