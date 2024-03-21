from django.db import models

# Create your models here.

class Post(models.Model): 
    titulo= models.CharField(blank=False, max_length=100, null=False )
    autor= models.CharField(blank=False, max_length=70, null=False ) 
    date= models.DateTimeField(auto_now_add=True)
    preview= models.TextChoices(blank=False, max_length=200, null=False)
    content= models.TextChoices(blank=False, null=False)
    slug= models.SlugField()

    class Meta:
        ordering= ['-date']

class Comentario(models.Model):
    usuario = models.CharField(max_length=50, blank=True)
    comentario = models.TextField(blank=False, max_length=200)
    data2= models.DateField(auto_now_add=True)
