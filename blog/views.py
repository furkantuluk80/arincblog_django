from django.shortcuts import render
from django.views.generic import TemplateView

"""
Bu  sinif, index.html dosyasinin islenmesini
saglar.
"""
class HomePageView(TemplateView):
    template_name = 'index.html'
    
    
    

