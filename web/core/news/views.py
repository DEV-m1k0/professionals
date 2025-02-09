from django.shortcuts import render
from datetime import date
import datetime
import requests
from models.models import *
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from django.shortcuts import redirect
from xml.etree import ElementTree
from core.settings import BASE_DIR
from .forms import SearchForm
from django.db.models import Q


# Create your views here.


class HomePageView(TemplateView, ContextMixin):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context["employees"] = Employee.objects.all()
        context["news"] = News.objects.all()
        context["events"] = Event.objects.all()
        context["feed_news"] = self.get_news_feed()
        context["search_form"] = SearchForm()
        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get("search") == "":
            return redirect("home")
        try:
            job_title = Position.objects.get(title__contains=request.POST.get('search'))
        except:
            job_title = 0
        try:
            author_news = Position.objects.get(username__contains=request.POST.get('search'))
        except:
            author_news = 0
        form = SearchForm(request.POST)
        employees = Employee.objects.filter(Q(username__contains=request.POST.get("search")) | Q(position_id=job_title) | Q(work_phone__contains=request.POST.get("search")) | Q(email__contains=request.POST.get("search")))
        events = Event.objects.filter(Q(title__contains=request.POST.get("search")) | Q(description__contains=request.POST.get("search")) | Q(responsible_worker=author_news))
        news = News.objects.filter(Q(title__contains=request.POST.get("search")) | Q(description__contains=request.POST.get("search")))
        context = self.get_context_data()
        context["employees"] = employees
        context["search_form"] = form
        context['events'] = events
        context['feed_news'] = news
        return render(request, self.template_name, context)

    
    def get_news_feed(self):
        url = "http://127.0.0.1:8000/news/feed"
        response = requests.get(url)
        if response.status_code == 200:
            with open("news.xml", "w") as xml_news_feed:
                xml_news_feed.write(response.text)

            tree = ElementTree.parse(BASE_DIR / "news.xml")
            root = tree.getroot()

            feed_news = []

            for elem in root.iter("item"):
                title = list(elem)[0].text
                
                feed_news.append(News.objects.get(title=title))

            return feed_news