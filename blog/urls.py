from django.urls import path, include
from .views import BlogPageView, BlogDetailView

"""
Burada amac, siteye giriste herhangi bir adrese gidilmemisse('')
ilk gelen sayfadaki(anasayfa) gorunumu belirlemek. Urls dosyasi ile 
views dosyasindaki HomePageView sinifi referans alinarak
class'in islenmesi saglanir.
"""
"""
'post/<int:pk>/': Bu desen, URL'nin yapisini tanimlar. 
post/ ile başlar ve sonrasinda bir <int:pk> kismi gelir. <int:pk> kismi, birincil anahtarin (primary key) 
bir tamsayi (integer) olduğunu belirtir. Bu, URL'nin bu bolumune bir tamsayi degeri bekledigimizi ifade eder.
"""
urlpatterns = [
    path('',BlogPageView.as_view(), name = 'index'  ),

    path('post/<int:pk>/',BlogDetailView.as_view(), name = 'post'  ), 
]

