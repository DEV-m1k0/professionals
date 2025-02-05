from django.contrib.syndication.views import Feed
from models.models import News
from datetime import date

class NewsFeed(Feed):
    title = "Новости на сайте"
    link = "" 

    def items(self):
        return News.objects.all()
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description, item.date

    
    def item_link(self, item):
        return f"/news/{item.id}"