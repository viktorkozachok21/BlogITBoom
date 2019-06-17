# coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from .models import *

import json
import random
import operator


# Create your views here.
def home(request):

    rating = ComputerLanguage.objects.all()
    sorted_rating = sorted(rating, key=operator.attrgetter('index'))
    languages_title, languages_index = [], []
    for item in sorted_rating:
        languages_title.append(item.title)
        languages_index.append(item.index)

    languages_title.reverse()
    languages_index.reverse()

    articles = Article.objects.all()
    news = News.objects.order_by("-pk")
    top_news = []
    for top in news:
        if top.top == 1:
            top_news.append(top)
    random.shuffle(top_news)
    latest = top_news[0].id

    top_lines = RunabledNews.objects.order_by("-pk")
    lines_list = []
    for top in top_lines:
        if top.top == 1:
            lines_list.append(top.title)
    random.shuffle(lines_list)
    run_line = ''
    run_line = ".\t".join(topic for topic in lines_list)

    article = random.choice(articles)

    song_list = Song.objects.all()
    song_names, song_artists, song_records = [], [], []

    for song in song_list:
        song_names.append(song.song_name)
        song_artists.append(song.song_artist)
        song_records.append(song.song_record.url)

    context = {
        'Article': article,
        'run_line':run_line,
        'news':top_news,
        'Articles':articles,
        "latest":latest,
        "languages_title":languages_title,
        "languages_index":languages_index,
        'Song_names':json.dumps(song_names),
        'Song_artists':json.dumps(song_artists),
        'Song_records':json.dumps(song_records)
    }

    return render(request, 'ItBoom/home.html', context)

def sendoffer(request):

    if request.method == "POST" and request.is_ajax:
        offer = request.POST['offer']
        new_offer = OfferMessage.objects.create(message=offer)
        return HttpResponseRedirect(request.path_info, status=200)
    return HttpResponseRedirect(request.path_info, status=400)

def sendmessage(request):

    if request.method == "POST" and request.is_ajax:
        author = request.POST['author']
        email = request.POST['email']
        message = request.POST['message']
        new_message = ContactMessage.objects.create(author=author, email=email, message=message)

    return HttpResponseRedirect(request.path_info)

def showarticle(request):

    if request.method == "GET" and request.is_ajax:
        article_key = request.GET['key']
        article = get_object_or_404(Article, title=article_key)
        choise_article = {
            'title':article.title,
            'content':article.description
        }

        return JsonResponse({"article":choise_article}, status=200)
    return JsonResponse({"success":False}, status=400)

def shownews(request):

    if request.method == "GET" and request.is_ajax:
        news_key = request.GET['key']
        news = get_object_or_404(News, title=news_key)
        choise_news = {
            'title':news.title,
            'content':news.description
        }

        return JsonResponse({"news":choise_news}, status=200)
    return JsonResponse({"success":False}, status=400)
