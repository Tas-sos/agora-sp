"""agora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from service import views
from component import views as component_views
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^api/admin/?', admin.site.urls),
    url(r'^api/docs/?', include('rest_framework_swagger.urls')),
    url(r'^api/v1/(portfolio|catalogue)/services/(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9a-zA-Z\.]+)/service_components/?', include('component.urls')),
    url(r'^api/v1/(portfolio|catalogue)/services/(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9a-zA-Z\.]+)/service_options/?', include('options.urls')),
    url(r'^api/v1/(portfolio|catalogue)/services/(?P<search_type>[0-9a-zA-Z\-\_]+)/service_components/?', component_views.get_service_components_complete),
    url(r'^api/v1/(portfolio|catalogue)/services/(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_owner/?', include('owner.urls')),
    url(r'^api/v1/(portfolio|catalogue)/services/?', include('service.urls')),
    url(r'^api/v1/(portfolio|catalogue)/service_picker/?', views.get_services_by_area),
    url(r'^api/v1/catalogue/view/?', views.get_catalogue_main_page),
    url(r'^api/v1/services/?', include('service.insert_urls')),
    url(r'^api/v1/owner/?', include('owner.insert_urls')),
    url(r'^api/v1/options/?', include('options.insert_urls')),
    url(r'^api/v1/component/?', include('component.insert_urls')),
    # url(r'^api/v1/accounts/?', include('accounts.urls')),
    # url(r'^api/v1/auth/', include("social.apps.django_app.urls", namespace="social")),
    # url(r'^api/v1/accounts/?', include('django.contrib.auth.urls')),
    url(r'^ui/?', include('service.view_urls')),
    url(r'^ui/component/?', include('component.ui_urls')),
    url(r'^ui/owner/?', include('owner.ui_urls')),
    url(r'^ui/service/?', include('service.ui_urls')),
    url(r'^ui/options/?', include('options.ui_urls')),
    url(r'^saml2/', include('djangosaml2.urls')),
    url(r'^test/', 'djangosaml2.views.echo_attributes'),
    url(r'^/?$', RedirectView.as_view(url='/ui/catalogue/services'))
]

handler404 = "agora.views.error404"
handler400 = "agora.views.error400"
handler500 = "agora.views.error500"
