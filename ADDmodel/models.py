from django.db import models


class monelN (models.Model):
    name=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to="static/",default="")
    subTitle=models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
    
class project (models.Model):
    ProjectName=models.TextField()
    LanguageUse=models.TextField()
    Year=models.TextField()
    UrlLive=models.TextField()

    

    
class skill (models.Model):
    LanguageName=models.TextField()
    WhatSpecial=models.TextField()
    Disc=models.TextField()
    


# Create your models here.
