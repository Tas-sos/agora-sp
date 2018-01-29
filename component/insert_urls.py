from django.conf.urls import *
from component import views


urlpatterns = [
    url(r'^service_component_implementation/edit/?$', views.edit_service_component_implementation),
    url(r'^service_component_implementation/add/?$', views.insert_service_component_implementation),
    url(r'^service_component_implementation_detail/edit/?$', views.edit_service_component_implementation_details),
    url(r'^service_component_implementation_detail/add/?$', views.insert_service_component_implementation_details),
    url(r'^edit/?$', views.edit_service_component),
    url(r'^add/?$', views.insert_service_component),
    url(r'^service_details_component_implementation_details/edit/?$', views.edit_service_details_component_implementation_details),
    url(r'^service_details_component_implementation_details/add/?$', views.insert_service_details_component_implementation_details),
]