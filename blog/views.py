from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

"""
Bu  sinif, index.html dosyasinin islenmesini
saglar.
"""
class BlogPageView(ListView):
    model = Post     #model olarak post kullanilir demek.
    template_name = 'index.html'
    
    
    

