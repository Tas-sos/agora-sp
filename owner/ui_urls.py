from django.conf.urls import *
from owner import views


urlpatterns = [
    url(r'^contact_information/?$', views.contact_information_write_ui),
    url(r'^$', views.owner_write_ui),
    url(r'^institution/?$', views.institution_write_ui),
]