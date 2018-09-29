from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Categorys,Image,Location
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

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

    '''
    view function to present images from past days
    '''
def past_days_images(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(image_today)

    galla = Image.past_days_images(date)
    return render(request, 'all-images/past-images.html',{"date": date,"galla":galla})

def image_today(request):
    date = dt.date.today()
    galla = Image.todays_images()
    return render(request,'all-images/gallery-images.html',{"date": date,"galla":galla})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_image = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_image})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})

def category_image(request,category_id):
    category=Category.query.get(id=category_id)
    return render(request,'category.html',locals())

def image(request,image_id):

    image = Image.objects.filter(id = image_id)
    return render(request,"all-images/image.html", {"image":image})

    