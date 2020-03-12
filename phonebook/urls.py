from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^abonent/$', views.contact, name='contact'),#
    url(r'^contact/$', views.contact, name='contact'),
]
