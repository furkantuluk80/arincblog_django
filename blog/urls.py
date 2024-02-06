from django.urls import path, include
from .views import HomePageView

"""
Burada amac, siteye giriste herhangi bir adrese gidilmemisse('')
ilk gelen sayfadaki(anasayfa) gorunumu belirlemek. Urls dosyasi ile 
views dosyasindaki HomePageView sinifi referans alinarak
class'in islenmesi saglanir.
"""
urlpatterns = [
    path('',HomePageView.as_view(), name = 'index'  ),
]

