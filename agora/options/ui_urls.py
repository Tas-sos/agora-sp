from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^sla/?$', views.options_sla_write_ui),
    url(r'^parameter/?$', views.options_parameter_write_ui),
    url(r'^service_options/?$', views.service_options_write_ui),
    url(r'^service_details_options/?$', views.service_details_options_write_ui),
    url(r'^service_details_options/(?P<serv_det_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.service_details_options_edit_ui),
    url(r'^service_options/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.service_options_edit_ui),
    url(r'^sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/?$', views.options_sla_edit_ui),
    url(r'^parameter/(?P<param_uuid>[0-9a-zA-Z\-]+)/?$', views.options_parameter_edit_ui),
    url(r'^sla_parameter/?$', views.options_sla_parameter_write_ui),
    url(r'^sla_parameter/(?P<sla_param_uuid>[0-9a-zA-Z\-]+)/?$', views.options_sla_parameter_edit_ui),
]