from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails
from common import helper


class ServiceComponent(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        component_implementations = [sci.as_json() for sci in ServiceComponentImplementation.objects
            .filter(component_id=self.pk)]

        return {
            "uuid": str(self.id),
            "name": self.name,
            "description": self.description,
            "component_implementations_list": {
                "count": len(component_implementations),
                "component_implementations": component_implementations
            }
        }

    def as_short(self, service_id, service_details_version):

        service = Service.objects.get(id=service_id)

        return {
            "component_implementation": {
            "uuid": str(self.id),
            "name": self.name,
            "description": self.description,
                "links": {
                        "self":helper.current_site_url() + "/v1/portfolio/services/" + str(service.name).replace(" ", "_")
                            + "/service_details/" + str(service_details_version) + "/service_components/" + str(self.pk)
                            + "/service_component_implementations",
                }}
        }

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = None
        super(ServiceComponent, self).save(*args, **kwargs)


class ServiceComponentImplementation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        component_implementation_details = [scid.as_json() for scid in ServiceComponentImplementationDetail.objects.
                                filter(component_id=self.component_id.pk, component_implementation_id=self.pk)]

        return {
            "uuid": str(self.id),
            "name": self.name,
            "description": self.description,
            "component_implementation_details_list": {
                "count": len(component_implementation_details),
                "component_implementation_details": component_implementation_details
            }
        }

    def as_short(self, service_id, service_details_version):

        service = Service.objects.get(id=service_id)

        return {
            "uuid": str(self.id),
            "name": self.name,
            "description": self.description,
            "component_implementation_details_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(service.name).replace(" ", "_")
                           + "/service_details/" + str(service_details_version) + "/service_components/"
                           + str(self.component_id.pk) + "/service_component_implementations/" + str(self.pk)
                                                    + "/service_component_implementation_detail",
                    "meta": {
                        "desc": "Link to the concrete service component implementation details."
                    }}}
        }


    def save(self, *args, **kwargs):
        if not self.description:
            self.description = None
        super(ServiceComponentImplementation, self).save(*args, **kwargs)

class ServiceComponentImplementationDetail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    component_implementation_id = models.ForeignKey(ServiceComponentImplementation, on_delete=models.CASCADE)
    version = models.CharField(max_length=255, default=None, blank=True)
    configuration_parameters = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.component_implementation_id.name) + " " +  str(self.version)

    def as_json(self):
        return {
            "uuid": str(self.id),
            "version": self.version,
            "configuration_parameters": self.configuration_parameters
        }


    def save(self, *args, **kwargs):
        if not self.configuration_parameters:
            self.configuration_parameters = None
        super(ServiceComponentImplementationDetail, self).save(*args, **kwargs)


class ServiceDetailsComponent(models.Model):

    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_component_implementation_detail_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_component_implementation_detail_id = models.ForeignKey(ServiceComponentImplementationDetail)

    def __unicode__(self):
        return str(self.service_id.name) + " "  + str(self.service_details_id.version) + " " + \
               str(self.service_component_implementation_detail_id.version)

    def as_json(self):
        return {
            "service_uuid": self.service_id.name,
            "service_details_version": self.service_details_id.version,
            "service_component_implementation_detail_uuid": self.service_component_implementation_detail_id.pk
        }
