from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    url('^$', views.feature_index),
)
