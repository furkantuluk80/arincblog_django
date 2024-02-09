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
    path('home/', TemplateView.as_view(template_name = 'home.html')),
    path('contact/', TemplateView.as_view(template_name = 'contact.html')),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)