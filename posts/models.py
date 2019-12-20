from django.db import models

# Create your models here.

from django.conf import settings

User = settings.AUTH_USER_MODEL#modelo de los usuaarios que registramos#

class Post(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    authors = models.ForeignKey('Author',on_delete=models.CASCADE)#realacion de uno a uno con la tabla o clase authors#
    image = models.ImageField()
    slug = models.SlugField()#utilizada para la url ejemplo : post/1 ----> posts/slug lo que contenga este campo

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/posts/detail/{}/".format(self.slug)
    
    #cada vez que veamos este model nos va devolver el titulo#

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone = models.IntegerField()#"809 se le "


    def __str__(self):
        return self.user.username