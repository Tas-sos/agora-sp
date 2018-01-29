from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_dependencies/edit/?$', views.insert_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_dependencies/add/?$', views.insert_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/edit/?$', views.insert_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/add/?$', views.insert_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_external_dependencies/edit/?$', views.insert_external_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_external_dependencies/add/?$', views.insert_external_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/user_customer/edit/?$', views.insert_user_customer),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/user_customer/add/?$', views.insert_user_customer),
    url(r'^edit/?$', views.insert_service),
    url(r'^add/?$', views.insert_service),
    url(r'^external_service/edit/?$', views.insert_external_service),
    url(r'^external_service/add/?$', views.insert_external_service),

]