from django.urls import path,include
from news.views import scrape, news_list , home , contact
from django.contrib import admin
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('feed/', news_list, name="feed"),
  path('home/', home, name="home"),
  path('contact/',contact,name="contact"),
  path('home/',home,name="home"),
  path('',home,name="home"),
  path('admin/', admin.site.urls),
 # path('',include("news.urls")),
]


