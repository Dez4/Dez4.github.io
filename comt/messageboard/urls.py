from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^http://www.bravolou.com/comment.html/$', views.msgCreate, name='msgCreate')
]
