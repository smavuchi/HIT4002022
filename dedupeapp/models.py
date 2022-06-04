from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Deduped(models.Model):
    title= models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    deduped_file = models.FileField(upload_to="files")

    def __str__(self):
        return f'{self.user} Deduped'

    class Meta:
        verbose_name_plural = 'Deduped'
