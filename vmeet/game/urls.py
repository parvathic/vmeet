from django.urls import path
from . import views
from .views import home, gallery, chess, quiz
urlpatterns = [
    path('',views.home, name='home'),
    path('index.html', home, name = "index"), 
    path('gallery.html', gallery, name = "gallery"), 
    path('home.html', chess, name = "chess"), 
    path('trivia.html', quiz, name = "quiz"),
]
