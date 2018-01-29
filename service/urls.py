from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/?$', views.get_service_details),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/service_options/?$', views.get_service_options),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/?$', views.get_all_service_details),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_owner/(?P<service_owner>[0-9a-zA-Z\-\_]+)/institution/?$', views.get_service_owner_institution),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_owner/?$', views.get_service_owners),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/institution/?$', views.get_service_institution),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/contact_information/?$', views.get_service_contact_information),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_dependencies/?$', views.get_service_dependencies),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/service_external_dependencies/?$', views.get_service_external_dependencies),
    url(r'(?P<search_type>[0-9a-zA-Z\-\_]+)/?$', views.get_service),
    url(r'^$', views.list_services),

]