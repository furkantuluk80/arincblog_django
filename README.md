# arincblog_django
Django ile ornek website yapimi icin olusturulan projedir.

## 1) PYTHON - DJANGO - SANAL ORTAM KURULUMU

* `https://www.python.org/downloads/` sitesinden ilgili işletim sistemi için python kurulur ve kurulum aşamasında **add  python to path** seçeneğine tıklanır.
* CMD açılır.
* `mkdir projeismi` komutu ile proje için istenilen yerde  "projeismi" yerine yazılacak isimde klasör oluşturulur
* `pip install virtualenv` komutu ile virtualenv kurulumu yapılır.
* ``python -m pip install --upgrade pip`` komutu ile pip güncellenir.
* `virtualenv env` komutu ile "env" adında sanal ortam oluşturulur.
* `env\Scripts\activate` komutu ile sanal ortam aktifleştirilir ve  komutun başına (env) şeklinde yazı geldiği görülür.
* `pip install django` komutu ile django oluşturulan sanal ortam için yüklenir.
* `django-admin startproject proje_ismi .` komutu ile proje "projeismi" klasörünün içinde **proje_ismi** ile oluşturularak gerekli dosyaların oluşturulması sağlanır. 

> Sanal ortamdan çıkmak için `deactivate` komutu kullanılır.

## 1.1) UYGULAMANIN KURULUMU 
* Proje yolu açılır.
* Path kısmına cmd yazılarak direkt cmd'nin açılması sağlanır.
* `env\Scripts\activate` komutu ile sanal ortam aktif edilir. 
* ``py manage.py startapp uygulama_ismi``  komutu ile uygulama oluşturulur.
## 1.2) VERİTABANI OLUŞTURMA VE SERVER ÇALIŞTIRMA

* ``py manage.py migrate`` komutu ile veri tabanı oluşturulur.
* ``py manage.py runserver``komutu ile server çalıştırılır.
* ``py manage.py createsuperuser`` komutu ile admin kendi veritabanını oluşturur.
* Sonrasında 'username' 'email' ve 'password' alanları doldurulur. 

>Veri tabanında değişiklik yapılacağı zaman `py manage.py makemigrations` komutu ile veri tabanındaki değişiklikler algılanır ve yeniden migration dosyası oluşturularak veri tabanı güncellenir.

# 2) NEDİR NE İŞE YARAR?

## 2.1) Admin.py

Bu dosya tabloların sitede görünmesi için, models.py'de veri tabanına eklenen modelin kaydedilmesini sağlar.
Örnek kod:

`admin.site.register(Model_Adi)`
## 2.2) Urls.py

Sitenin adreslemelerine yönlendirilmesini sağlayan dosyadır.
Burada ilgili adreslemeler için html dosyaları referans olarak verilir.  Örnek kod aşağıdaki gibidir.

```
from django.contrib import admin

from django.urls import path, include

from django.views.generic import TemplateView

from django.conf.urls.static import static

from django.conf import settings

loalhost:8000/

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('blog.urls')),

    path('about/', TemplateView.as_view(template_name = 'about.html')),

    path('home/', TemplateView.as_view(template_name = 'home.html')),

    path('contact/', TemplateView.as_view(template_name = 'contact.html')),

]
urlpatterns += static(settings.STATIC_URL, documant_root = settings.STATICFILES_DIRS)
```
## 2.3) Views.py

Bu dosya, kullanılacak olan modeli tanımlayarak, o model için referans olacak html dosyasının düzenlemelerinin yapıldığı yerdir. Oluşturulan class **urls.py'e** eklenir.  Örnek kod aşağıdaki gibidir.
```
class BlogPageView(ListView):

    model = Post     #model olarak post kullanilir demek.

    template_name = 'index.html'
```

## 2.4) Settings.py

Bu dosyada projenin yapılandırma dosyasıdır.
```
#blog buraya eklenerek, projedeki sayfalarin gosterilmesini saglar.

INSTALLED_APPS = [

    'blog.apps.BlogConfig',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

]
```

```
# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join('static'),)
```
## 2.5) Models.py
Burada olusturulan classlar veritabanindaki tabloları ifade etmektedir. Burada, class içinde oluşturulması istenen modelin(tablonun) özellikleri girilerek kullanıcının veritabanını 
yönetmesi sağlanır. Örnek kod  aşağıdaki gibidir.
```
class Post(models.Model):

    title    = models.CharField(max_length = 100)

    subtitle = models.CharField(max_length = 100)

    content  = models.TextField()

    author   = models.ForeignKey('auth.User',

                                 on_delete = models.CASCADE )

    date     = models.DateTimeField(auto_now_add = True)
```
Görüldüğü gibi **title**, **subtitle**, **content**, **author**, **date** gibi field'lar **Post** adında bir modelin altında toplanarak kullanıcı tarafından özelleştirilmişlerdir.

Aşağıdaki görselde veri tabanında oluşturulan Post modelinin başlığının, sitede görünmesini sağlayan  örneği verilmiştir.  
```
    def __str__(self):
        return self.title
```
> Bu kod yazılmadığı halde, postreSQL tarafından otomatik olarak oluşturulan başlık sitede görünecektir.



