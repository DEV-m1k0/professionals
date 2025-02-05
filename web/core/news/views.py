from datetime import date
import datetime
import requests
from models.models import *
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from xml.etree import ElementTree
from core.settings import BASE_DIR


# Create your views here.


class HomePageView(TemplateView, ContextMixin):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context["employees"] = Employee.objects.all()[:10]
        context["news"] = News.objects.all()
        context["events"] = Event.objects.all()
        context["feed_news"] = self.get_news_feed()
        return context
    
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