from __future__ import unicode_literals

from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation, Institution
from common import helper
from collections import OrderedDict


class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=255, default=None, blank=True)
    description_external = models.TextField(default=None, blank=True, null=True)
    description_internal = models.TextField(default=None, blank=True, null=True)
    service_area = models.CharField(max_length=255, default=None, blank=True, null=True)
    service_type = models.CharField(max_length=255, default=None, blank=True, null=True)
    request_procedures = models.TextField( default=None, blank=True, null=True)
    funders_for_service = models.TextField(default=None, blank=True, null=True)
    value_to_customer = models.TextField(default=None, blank=True, null=True)
    risks = models.TextField(default=None, blank=True, null=True)
    competitors = models.TextField(default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(ServiceOwner, null=True)
    id_contact_information = models.ForeignKey(ContactInformation, null=True)

    def __unicode__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.description_internal:
            self.description_internal = None
        if not self.description_external:
            self.description_external = None
        if not self.service_area:
            self.service_area = None
        if not self.service_type:
            self.service_type = None
        if not self.request_procedures:
            self.request_procedures = None
        if not self.funders_for_service:
            self.funders_for_service = None
        if not self.value_to_customer:
            self.value_to_customer = None
        if not self.request_procedures:
            self.request_procedures = None
        if not self.risks:
            self.risks = None
        if not self.competitors:
            self.competitors = None
        super(Service, self).save(*args, **kwargs)

    def get_service_details(self, complete=False, url=False, catalogue=False):

        services = []
        if not catalogue:
            servs = ServiceDetails.objects.filter(id_service=self.pk)
        else:
            servs = ServiceDetails.objects.filter(id_service=self.pk, is_in_catalogue=True)
        for s in servs:
            if complete:
                services.append(s.as_complete(url=url))
            else:
                services.append(s.as_short())

        return services

    def get_service_details_by_version(self, version):
        return ServiceDetails.objects.get(id_service=self.pk, version=version)

    def get_user_customers(self):
        return [c.as_json() for c in UserCustomer.objects.filter(service_id=self.pk)]

    def get_service_owners(self):
        return ServiceOwner.objects.get(id=self.id_service_owner.pk).as_json()

    def get_service_owner_object(self):
        return ServiceOwner.objects.get(id=self.id_service_owner.pk) if self.id_service_owner is not None else None

    def get_service_institution(self):
        return Institution.objects.get(pk=ServiceOwner.objects.
                                       get(id=self.id_service_owner.pk).id_service_owner.pk).as_json()

    def get_service_external_dependencies(self):
        return [ExternalService.objects.get(id=dependency.id_external_service.pk).as_json()
                for dependency in Service_ExternalService.objects.filter(id_service=self.id)]

    def get_service_contact_information(self):
        return ContactInformation.objects.get(id=self.id_contact_information.pk).as_json()

    def get_service_contact_information_object(self):
        return ContactInformation.objects.get(id=self.id_contact_information.pk) if self.id_contact_information is \
                                                                                    not None else None

    def get_service_dependencies(self):
        dependencies = Service_DependsOn_Service.objects.filter(id_service_one=self.pk)
        service_dependencies = []

        for d in dependencies:
            service = Service.objects.get(id=d.id_service_two.pk)
            service_dependencies.append({
                "service": {
                    "uuid": service.id,
                    "name": service.name,
                    "links": {
                        "self":helper.current_site_url() + "/v1/portfolio/services/" + str(
                            Service.objects.get(pk=d.id_service_two.pk).name)
                    },
                }
            })

        return service_dependencies

    def as_complete_portfolio(self):
        service_dependencies = self.get_service_dependencies()

        external = Service_ExternalService.objects.filter(id_service=self.pk)
        external_services = []

        for e in external:
            external_services.append({
                "uuid": e.id_external_service.pk,
                "name": e.id_external_service.name

            })

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True)

        contact_information = self.get_service_contact_information_object()
        if contact_information is not None:
            contact_information = {
                "email": self.get_service_contact_information_object().email,
                "url": self.get_service_contact_information_object().url,
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_") + "/contact_information",
                }
            }

        service_owner = self.get_service_owner_object()
        if service_owner is not None:
            service_owner = {
                "uuid": self.get_service_owner_object().id,
                "email": self.get_service_owner_object().email,
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_"),
                }
            }

        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("description_external", self.description_external),
            ("description_internal", self.description_internal),
            ("service_owner", service_owner),
            ("contact_information", contact_information),
            ("service_area", self.service_area),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("dependencies", {
                "count": len(service_dependencies),
                "service_dependencies_link": {
                    "related": {
                        "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_")
                                + "/service_dependencies",
                        "meta": {
                            "desc": "A list of links to the service dependencies"
                        }
                    }

                },
                "services": service_dependencies
            }),
            ("external", {
                "count": len(external_services),
               "external_services_link": {
                    "related": {
                        "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_") + "/service_external_dependencies",
                        "meta": {
                            "desc": "Links to external services that this service uses."
                        }}
                },

                "external_services": external_services
            }),
            ("funders_for_service", self.funders_for_service),
            ("value_to_customer", self.value_to_customer),
            ("risks", self.risks),
            ("competitors", self.competitors),
            ("service_type", self.service_type),
            ("request_procedures", self.request_procedures),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("service_complete_link", {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }}),
        ])


    def as_portfolio(self):

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True)

        contact_information = self.get_service_contact_information_object()
        if contact_information is not None:
            contact_information = {
                "email": self.get_service_contact_information_object().email,
                "url": self.get_service_contact_information_object().url,
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_") + "/contact_information",
                }
            }

        service_owner = self.get_service_owner_object()
        if service_owner is not None:
            service_owner = {
                "uuid": self.get_service_owner_object().id,
                "email": self.get_service_owner_object().email,
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_"),
                }
            }

        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("description_external", self.description_external),
            ("description_internal", self.description_internal),
            ("service_owner", service_owner),
            ("contact_information", contact_information),
            ("service_area", self.service_area),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("funders_for_service", self.funders_for_service),
            ("value_to_customer", self.value_to_customer),
            ("risks", self.risks),
            ("competitors", self.competitors),
            ("service_type", self.service_type),
            ("request_procedures", self.request_procedures),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("service_complete_link", {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }})
        ])

    def as_catalogue(self):

        service_details = self.get_service_details(complete=True, url=True, catalogue=True)

        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("description_external", self.description_external),
            ("service_area", self.service_area),
            ("value_to_customer", self.value_to_customer),
            ("service_type", self.service_type),
            ("service", {
                "name": self.name,
                "links": {
                "self": helper.current_site_url() + "/v1/catalogue/services/" + str(self.name).replace(" ", "_"),
                }}),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            })
        ])


class ServiceDetails(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    id_service = models.ForeignKey(Service)
    version = models.CharField(max_length=255, default=None, blank=True)
    status = models.CharField(max_length=255, default="Inactive", blank=True, null=True)
    features_current = models.TextField(default=None, blank=True, null=True)
    features_future = models.TextField( default=None, blank=True, null=True)
    usage_policy_has = models.BooleanField(default=False, blank=True)
    usage_policy_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    user_documentation_has = models.BooleanField(default=False, blank=True)
    user_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    operations_documentation_has = models.BooleanField(default=False, blank=True)
    operations_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    monitoring_has = models.BooleanField(default=False, blank=True)
    monitoring_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    accounting_has = models.BooleanField(default=False, blank=True)
    accounting_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    business_continuity_plan_has = models.BooleanField(default=False, blank=True)
    business_continuity_plan_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    disaster_recovery_plan_has = models.BooleanField(default=False, blank=True)
    disaster_recovery_plan_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    decommissioning_procedure_has = models.BooleanField(default=False, blank=True)
    decommissioning_procedure_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    cost_to_run = models.CharField(max_length=255, default=None, blank=True, null=True)
    cost_to_build = models.CharField(max_length=255, default=None, blank=True, null=True)
    use_cases = models.TextField(default=None, blank=True, null=True)
    is_in_catalogue = models.BooleanField(default=False)

    def __unicode__(self):
        primary_key = self.id_service.pk
        srv = Service.objects.get(pk=primary_key)
        return str(srv.name) + " " + str(self.version)

    def save(self, *args, **kwargs):
        if not self.status:
            self.status = "Inactive"
        if not self.features_current:
            self.features_current = None
        if not self.features_future:
            self.features_future = None
        if not self.cost_to_run:
            self.cost_to_run = None
        if not self.cost_to_build:
            self.cost_to_build = None
        if not self.use_cases:
            self.use_cases = None
        super(ServiceDetails, self).save(*args, **kwargs)

    def as_short(self):
        return OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status),
            ("features_current", self.features_current),
            ("features_future", self.features_future),
            ("service_details", {
                "version": self.version,
                "status": self.status,
                "in_catalogue": self.is_in_catalogue,
                "links": {
                "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name).
                        replace(" ", "_") + "/service_details/" + self.version,
                }
            })
        ])

    def as_complete(self, url=False):

        service_dependencies = self.id_service.get_service_dependencies()

        details = OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status),
            ("use_cases", self.use_cases),
            ("features_current", self.features_current),
            ("features_future", self.features_future),
            ("dependencies", {
                "count": len(service_dependencies),
                "service_dependencies_link": {
                    "related": {
                        "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name).replace(" ", "_")
                                + "/service_dependencies",
                        "meta": {
                            "desc": "A list of links to the service dependencies"
                        }
                    }

                },
                "services": service_dependencies
            }),
            ("usage_policy_has", self.usage_policy_has),
            ("usage_policy_link", {
                "related": {
                    "href": self.usage_policy_url,
                    "meta": {
                        "desc": "A link to the usage policy for this service."
                    }
                }}),
            ("user_documentation_has", self.user_documentation_has),
            ("user_documentation_link",  {
                "related": {
                    "href": self.user_documentation_url,
                    "meta": {
                        "desc": "A link to the user documentation for this service."
                    }
                }}),
            ("operations_documentation_has", self.operations_documentation_has),
            ("operations_documentation_link", {
                "related": {
                    "href": self.operations_documentation_url,
                    "meta": {
                        "desc": "A link to the operations documentation for this service."
                    }
                }}),
            ("monitoring_has", self.monitoring_has),
            ("monitoring_link", {
                "related": {
                    "href": self.monitoring_url,
                    "meta": {
                        "desc": "A link to the monitoring system for this service."
                    }
                }}),
            ("accounting_has", self.accounting_has),
            ("accounting_link",  {
                "related": {
                    "href": self.accounting_url,
                    "meta": {
                        "desc": "A link to the accounting system for this service."
                    }
                }}),
            ("business_continuity_plan_has", self.business_continuity_plan_has),
            ("business_continuity_plan_link", {
                "related": {
                    "href": self.business_continuity_plan_url,
                    "meta": {
                        "desc": "A link to the business continuity plan for this service."
                    }
                }}),
            ("disaster_recovery_plan_has", self.disaster_recovery_plan_has),
            ("disaster_recovery_plan_url", {
                "related": {
                    "href": self.disaster_recovery_plan_url,
                    "meta": {
                        "desc": "A link to the disaster recovery plan for this service."
                    }
                }}),
            ("decommissioning_procedure_has", self.decommissioning_procedure_has),
            ("decommissioning_procedure_url",  {
                "related": {
                    "href": self.decommissioning_procedure_url,
                    "meta": {
                        "desc": "A link to the decommissioning procedure for this service."
                    }
                }}),
            ("cost_to_run", self.cost_to_run),
            ("cost_to_build", self.cost_to_build),
            ("service_details_type", "Catalogue" if self.is_in_catalogue else "Portfolio")
        ])


        if url:
            details.update({"service_details": {
                "version": self.version,
                "status": self.status,
                "in_catalogue": self.is_in_catalogue,
                "links": {
                "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name).
                        replace(" ", "_") + "/service_details/" + self.version,
                }
            }})

        return details

    def as_json(self):
        return {
            "uuid": self.id,
            "version": self.version,
            "service_status": self.status,
            "features_current": self.features_current,
            "features_future": self.features_future
        }


class ExternalService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    service = models.CharField(max_length=255, default=None, blank=True, null=True)
    details = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "service": self.service,
            "details": self.details
        }

    def save(self, *args, **kwargs):
        if not self.description:
            self.description = None
        super(ExternalService, self).save(*args, **kwargs)


class Service_DependsOn_Service(models.Model):
    class Meta:
        unique_together = (('id_service_one', 'id_service_two'),)

    id_service_one = models.ForeignKey(Service, related_name='service_one')
    id_service_two = models.ForeignKey(Service, related_name='service_two')

    def __unicode__(self):
        primary_key_one = self.id_service_one.pk
        primary_key_two = self.id_service_two.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = Service.objects.get(pk=primary_key_two)

        return str(srv1.name) + " " + str(srv2.name)

    def as_json(self):
        return {
            "service": self.id_service_one.name,
            "dependency": self.id_service_two.name
        }


class Service_ExternalService(models.Model):
    class Meta:
        unique_together = (('id_service', 'id_external_service'),)

    id_service = models.ForeignKey(Service)
    id_external_service = models.ForeignKey(ExternalService)

    def __unicode__(self):
        primary_key_one = self.id_service.pk

        external_primary_key_one = self.id_external_service.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = ExternalService.objects.get(pk=external_primary_key_one)

        return str(srv1.name) + " " + str(srv2.name)

    def as_json(self):
        return {
            "service": self.id_service.pk,
            "external_service": self.id_external_service.pk
        }


class UserCustomer(models.Model):
    USER_TYPES = (
        ("Individual Researchers", "Individual Researchers"),
        ("Community manager", "Community manager"),
        ("Service provider", "Service provider"),
        ("Data Project Principle Investigator (PI)", "Data Project Principle Investigator (PI)")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, choices=USER_TYPES, blank=True)
    role = models.CharField(max_length=255, default=None, blank=True)
    service_id = models.ForeignKey(Service)

    def __unicode__(self):
        return str(self.name) + " as " + str(self.role) + " for " + str(self.service_id)

    def as_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "role": self.role
        }
