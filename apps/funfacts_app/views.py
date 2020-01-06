from django.shortcuts import render
from datetime import datetime

from .import web_scrapping
# Create your views here.
#  url(r'^$', views.index),
#     url(r'^funfacts$', views.funfacts),
def index(request):
    return render(request,"funfacts_app/index.html")
    # img_src = web_scrapping.get_src(dob)
    #     context ={
    #         "img_src" : img_src
    #     }
    #     #return redirect("/books",)
    #     return render(request,"funfacts_app/funfacts.html",context)

def funfacts(request):
    print(request.POST)
    date_chk = request.POST['dob']
    date_chk  = datetime.strptime(date_chk, "%Y-%m-%d")
    print (f"Month  = {date_chk.month}")
    print (f"Day  = {date_chk.day}")
    print (f"Year  = {date_chk.year}")
    new_str = date_chk.strftime("%B %d")
    category = request.POST['category']
    todays_horoscope = web_scrapping.getHoroscope(date_chk.year,new_str)
    #name_img = web_scrapping.get_src(new_str,category)
    events = web_scrapping.get_historical_data(new_str,date_chk.year)
    historic_events = web_scrapping.events_past(new_str)
    context ={
        "img_src" : events['image'],
        "celeb_name" : events['name'],
        "todays_horoscope" : todays_horoscope,
        "events": historic_events
    }

    return render(request,"funfacts_app/funfacts.html",context)