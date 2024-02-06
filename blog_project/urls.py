from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

# localhost:8000/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about/', TemplateView.as_view(template_name = 'about.html')),
]

urlpatterns += static(settings.STATIC_URL, documant_root = settings.STATICFILES_DIRS)