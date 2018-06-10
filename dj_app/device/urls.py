from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^devices/$', views.DeviceView.as_view(), name='device'),
    re_path(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetailView.as_view(), name='device-detail'),
    re_path(r'^data/$', views.DeviceDataView.as_view()),
    re_path(r'^data/(?P<pk>[0-9]+)/$', views.DeviceDataDetailView.as_view()),
]