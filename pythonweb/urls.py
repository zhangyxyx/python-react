
from django.conf.urls import url
from pythonweb import views

urlpatterns = [
    # url('execl/', views.execl),
    # url('essay/', views.essay),
    url('home/', views.react),
    url('question/', views.question),
    # url(r'^ajax_list/$', views.ajax_list),
]
