from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome')

def image_today(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

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
