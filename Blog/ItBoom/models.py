# coding: utf-8
from django.db import models
from django.utils import timezone
from tinymce import HTMLField

class Article(models.Model):

    title = models.CharField(max_length=255,blank=False,null=False)
    description = HTMLField('Description')
    content = HTMLField('Content')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.title

class News(models.Model):

    title = models.CharField(max_length=255,blank=False,null=False)
    top = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='article_images')
    description = HTMLField('Description')
    content = HTMLField('Content')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.title

class RunabledNews(models.Model):

    title = models.TextField()
    top = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.title

class ContactMessage(models.Model):

    status = models.CharField(max_length=255,default='new')
    author = models.CharField(max_length=255,blank=False,null=False)
    email = models.CharField(max_length=255,blank=False,null=False)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.status

class OfferMessage(models.Model):

    status = models.CharField(max_length=255,default='new')
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % self.status

class ComputerLanguage(models.Model):

    title = models.CharField(max_length=255,blank=False,null=False)
    index = models.FloatField(default=0)

    def __str__(self):
        return '%s' % self.title

class Song(models.Model):

    song_name = models.CharField(max_length=255,blank=False,null=False)
    song_artist = models.CharField(max_length=255,blank=False,null=False)
    song_record = models.FileField(upload_to='music')

    def __str__(self):
        return '%s' % self.song_name
