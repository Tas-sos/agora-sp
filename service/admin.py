from django.contrib import admin
from reversion.admin import VersionAdmin
from service.models import *
# Register your models here.


class ServiceAdmin(VersionAdmin):
    list_display = ['id', 'name', ]


class ServiceDetailsAdmin(VersionAdmin):
    list_display = ['id', 'id_service', 'version']


class ExternalServiceAdmin(VersionAdmin):
    pass


class Service_DependsOn_ServiceAdmin(VersionAdmin):
    pass


class Service_ExternalServiceAdmin(VersionAdmin):
    pass


class UserCustomerAdmin(VersionAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceDetails, ServiceDetailsAdmin)
admin.site.register(ExternalService, ExternalServiceAdmin)
admin.site.register(Service_DependsOn_Service, Service_DependsOn_ServiceAdmin)
admin.site.register(Service_ExternalService, Service_ExternalServiceAdmin)
admin.site.register(UserCustomer, UserCustomerAdmin)
