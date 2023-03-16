from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date


class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
         return reverse("home")

class profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True,upload_to="images/profile/")
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
         return reverse("home")



class post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag=models.CharField(max_length=255,default="post")
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    timeCreation=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blogposts')
    category=models.CharField(max_length=255,default='Horror')

    def __str__(self):
        return self.title+" | "+str(self.auther)
    def get_absolute_url(self):
         #return reverse("articleDetail",args=(str(self.id)))
         return reverse("home")

class Comment(models.Model):
    post=models.ForeignKey(post,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_time=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return '%s - %s' % (self.post.title , self.name)

    
