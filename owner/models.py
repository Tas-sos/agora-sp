from __future__ import unicode_literals

from django.db import models
from accounts.models import User as CustomUser
import uuid
from collections import OrderedDict

class Institution(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    address = models.CharField(max_length=255, default=None, blank=True, null=True)
    country = models.CharField(max_length=255, default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "5. Institutions"


    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("address", self.address),
            ("country", self.country),
            ("department", self.department)
        ])

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = None
        if not self.address or self.address == "":
            self.address = None
        if not self.country or self.country == "":
            self.country = None
        if not self.department or self.department == "":
            self.department = None
        super(Institution, self).save(*args, **kwargs)


class ServiceOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, unique=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(Institution, null=True)

    id_account = models.ForeignKey(CustomUser, null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "1. Service Owners"

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def get_institution(self):
        return Institution.objects.get(id=self.id_service_owner.pk).as_json()


    def save(self, *args, **kwargs):
        if not self.phone or self.phone == "":
            self.phone = None
        if not self.first_name or self.first_name == "":
            self.first_name = None
        if not self.last_name or self.last_name == "":
            self.last_name = None
        if not self.email or self.email == "":
            self.email = None
        super(ServiceOwner, self).save(*args, **kwargs)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("email", self.email),
            ("first_name", self.first_name),
            ("last_name", self.last_name),
            ("phone", self.phone),
            ("institution", self.id_service_owner.as_json() if self.id_service_owner is not None else None),
            ("account_id", self.id_account_id)
        ])


class ContactInformation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, null=True, unique=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    url = models.CharField(max_length=255, default=None, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "2. Contact Informations"

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_internal(self):

        response =  OrderedDict([
            ("uuid", self.id),
            ("url", self.url),
            ("email", self.email),
            ("first_name", self.first_name),
            ("last_name", self.last_name),
            ("phone", self.phone),
        ])

        return { "internal_contact_information": response }


    def get_external(self):

        response = {
            "email": self.email,
            "url": self.url,
        }
        return { "external_contact_information": response }

    def save(self, *args, **kwargs):
        if not self.phone or self.phone == "":
            self.phone = None
        if not self.first_name or self.first_name == "":
            self.first_name = None
        if not self.last_name or self.last_name == "":
            self.last_name = None
        if not self.email or self.email == "":
            self.email = None
        if not self.url or self.url == "":
            self.url = None
        super(ContactInformation, self).save(*args, **kwargs)

    def as_json(self):
        return {
            "internal_contact_information": self.get_internal(),
            "external_contact_information": self.get_external()
        }


class Internal(models.Model):
    id_contact_info = models.ForeignKey(ContactInformation)

    class Meta:
        verbose_name_plural = "2. Internal Contacts"

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)

    def as_json(self):
        return {
            "contact_information": ContactInformation.objects.get(pk=self.id_contact_info.pk)
        }


class External(models.Model):
    id_contact_info = models.ForeignKey(ContactInformation)

    class Meta:
        verbose_name_plural = "3. External Contacts"

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)


class AditionalUsernames(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service_owner = models.ForeignKey(ServiceOwner)
    username = models.CharField(max_length=255, default=None, blank=True)

    def as_json(self):
        return {
            "uuid": self.id,
            "service_owner": self.id_service_owner,
            "username": self.username
        }
