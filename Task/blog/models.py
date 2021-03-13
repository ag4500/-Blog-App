from django.db import models

# Create your models here.
class Post(models.Model):
    mode=(('private','Private'),('public','Public'))
    title=models.CharField(max_length=150)
    desc=models.TextField(max_length=500)
    status = models.CharField(max_length=10, choices=mode,      
    default="draft")
    user=models.CharField(max_length=12,default="ram")
    image=models.ImageField(upload_to='media',verbose_name='Upload Image')
    def __str__(self):
        return self.title

