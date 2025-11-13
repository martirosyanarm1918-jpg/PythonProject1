from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('schedule/', views.schedule, name = 'schedule'),
    path('trainers/', views.trainers, name = 'trainers'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('appointment/', views.appointment, name = 'appointment'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('news/', views.news, name = 'news'),
    path('faq/', views.faq, name = 'faq'),

]







