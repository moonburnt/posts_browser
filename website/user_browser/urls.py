from django.conf.urls import url, include
from user_browser import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.home_page_view),
]
