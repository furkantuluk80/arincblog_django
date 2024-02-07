from django.contrib import admin
from .models import Post

"""
admin alaninda eklenen models.py dosyasina eklenenen
tablonun gorunmesi icin, model buraya kaydedilir.
.models dosyasindan Post import edilir.(satir 2 )
"""

admin.site.register(Post)