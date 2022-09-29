
# Create your views here.

from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import pandas as pd
import pickle 
import locale

data=pd.pandas.read_csv('C:/Users/TUYYAB/OneDrive/Desktop/house prediction/House-price-prediction-ML/home/static/img/excel/Cleaned_data.csv')
pipe=pickle.load(open("C:/Users/TUYYAB/OneDrive/Desktop/house prediction/House-price-prediction-ML/home/RidgeModel2.pkl","rb"))
username=""

areaname=""
bathroom=""
gbhk=""
ganswer=""

def homepage(request):
    return render(request, "index.html")

# def answer(request):
#     return render(request,'answer.html',{'arae':areaname},{'bt':bathroom},{'bhk':gbhk},{'answer':ganswer})






def gproduct(request):
    locations=sorted(data['location'].unique())
    dic={'name':'GUEST1','password':'GUEST','locations':locations}
    if request.method=='POST':
        aname=request.POST.get('location',False)
        areaname=aname
        bh=request.POST.get('bhk',False)
        gbhk=bh
        size=request.POST.get('size',False)
        bt=request.POST.get('bt',False)
        bathroom=bt
        parking=request.POST.get('parking',False)
        duplex=request.POST.get('duplex',False)
        balcony=request.POST.get('balcany',False)
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
        dict={'area':aname,'size':size,'bt':bt,'bhk':bh,'answer':answer,'locations':locations,'duplex':duplex,'parking':parking,'balcony':balcony}
        return render(request,'answer.html',{'dict':dict})
        
    return render(request,"gproduct.html",dic)







