from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

"""
Bu  sinif, index.html dosyasinin islenmesini
saglar.
"""
class BlogPageView(ListView):
    model = Post     #model olarak post kullanilir demek.
    template_name = 'index.html'
    

"""
Bu  sinif, localhost ilk açıldığı anda
gelen linklere tiklandiginda, o linkin
ilgili sayfasina yonledirilmesini saglar.
"""  
class BlogDetailView(DetailView):    
    model = Post     #model olarak post kullanilir demek.
    template_name = 'post.html'
    

