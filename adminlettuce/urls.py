from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
    # Having name='django-admindocs-docroot' makes this link appear
    # automatically in the top-right corner of the Django admin
    # interface, according the template in admin/base.html.
    # In this behavior is not required, comment out the 'name' parameter.
    url('^$', views.feature_index, name='django-admindocs-docroot'),
)
