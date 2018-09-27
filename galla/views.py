from django.shortcuts import render
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def image_today(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})

def convert_dates(dates):
    '''
    function that gets the weekely number of the date.
    '''
    day_number = dt.date.weekday(dates)
    days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    '''
    returning the actual day of the week 
    '''
    day = days[day_number]
    return day
def past_days_images(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False