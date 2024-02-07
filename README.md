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

## 2) UYGULAMANIN KURULUMU 
* Proje yolu açılır.
* Path kısmına cmd yazılarak direkt cmd'nin açılması sağlanır.
* `env\Scripts\activate` komutu ile sanal ortam aktif edilir. 
* ``py manage.py startapp uygulama_ismi``  komutu ile uygulama oluşturulur.
## 3) VERİTABANI OLUŞTURMA VE SERVER ÇALIŞTIRMA

* ``py manage.py migrate`` komutu ile veri tabanı oluşturulur.
* ``py manage.py runserver``komutu ile server çalıştırılır.
* ``py manage.py createsuperuser`` komutu ile admin kendi veritabanını oluşturur.
* Sonrasında 'username' 'email' ve 'password' alanları doldurulur. 

>Veri tabanında değişiklik yapılacağı zaman `py manage.py makemigrations` komutu ile veri tabanındaki değişiklikler algılanır ve yeniden migration dosyası oluşturularak veri tabanı güncellenir.





