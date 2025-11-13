from django.shortcuts import render

def index(request):
    data = {
        'title': "Главная страница",
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'mainweb/index.html', data)

def about(request):
    return render(request, 'mainweb/about.html')

def schedule(request):
    return render(request, 'mainweb/schedule.html')

def trainers(request):
    return render(request, 'mainweb/trainers.html')

def reviews(request):
    return render(request, 'mainweb/reviews.html', {})

def appointment(request):
    return render(request, 'mainweb/appointment.html')

def contacts(request):
    return render(request, 'mainweb/contacts.html')


def faq(request):
    return render(request, 'mainweb/faq.html')


from django.shortcuts import render
from news.models import News

def news(request):
    news = News.objects.all()
    return render(request, 'news/news_home.html', {'news': news})
