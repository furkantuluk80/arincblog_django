from django.db import models

#olusturulan classlar veritabanindaki tablolar. Bu classlara ait ozellikler
#veritabanindaki tablolara ait olacak.


class Post(models.Model):
    title    = models.CharField(max_length = 100)
    subtitle = models.CharField(max_length = 100)
    content  = models.TextField()
    author   = models.ForeignKey('auth.User',
                                 on_delete = models.CASCADE )
    date     = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to='images/', null = True, blank = True)
    path = 'media/images/'



        
