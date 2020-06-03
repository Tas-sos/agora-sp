from __future__ import unicode_literals
from agora import  settings
from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation
from common import helper
from accounts.models import User, Organisation, Domain, Subdomain
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import SERVICE_ADMINSHIP_STATES, clean_html_fields, \
    publish_message
from agora.emails import send_email_application_created, \
    send_email_resource_admin_assigned, send_email_application_evaluated
from apimas.base import ProcessorFactory
from copy import deepcopy


class ServiceCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    icon = models.ImageField(default=settings.SERVICE_CATEGORY_ICON,
            upload_to=helper.service_area_image_path)
    description = RichTextUploadingField(default=None, blank=True, null=True)

    @property
    def icon_absolute_path(self):
        if self.icon:
            path = self.icon.url
        else:
            path = settings.MEDIA_URL+settings.SERVICE_CATEGORY_ICON
        return helper.current_site_baseurl()+'/'+path

    def __unicode__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceCategory, self).save(*args, **kwargs)


class ServiceTrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    value = models.CharField(max_length=255, default=None, blank=False)
    order = models.IntegerField(default=None, blank=False)

    def __unicode__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceTrl, self).save(*args, **kwargs)


class AccessPolicy(models.Model):
    """
    Policies stating how the service can be accessed
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,
                            default=None,
                            blank=True,
                            unique=True)
    access_mode = RichTextUploadingField(default=None, blank=True, null=True)
    payment_model = RichTextUploadingField(default=None, blank=True, null=True)
    pricing = RichTextUploadingField(default=None, blank=True, null=True)
    conditions = RichTextUploadingField(default=None, blank=True, null=True)
    geo_availability = models.TextField(default=None, blank=True)
    access_policy_url = models.CharField(max_length=255,
                                         default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(AccessPolicy, self).save(*args, **kwargs)


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    url = models.CharField(max_length=255, default=None, blank=True, null=True)
    endpoint = models.CharField(max_length=255, default=None, blank=True, null=True)
    short_description = RichTextUploadingField(default=None, blank=True, null=True)
    tagline = models.TextField(default=None, blank=True, null=True)
    service_categories = models.ManyToManyField(ServiceCategory, blank=False,
                                                related_name="categories")
    service_type = models.CharField(max_length=255, default=None, blank=True, null=True)
    user_value = RichTextUploadingField(default=None, blank=True, null=True)
    target_customers = RichTextUploadingField(default=None, blank=True, null=True)
    target_users = models.TextField(default=None, blank=True, null=True)
    screenshots_videos = RichTextUploadingField(default=None, blank=True, null=True)
    languages = models.TextField(default=None, blank=True, null=True)
    standards = RichTextUploadingField(default=None, blank=True, null=True)
    certifications = RichTextUploadingField(default=None, blank=True, null=True)
    logo = models.ImageField(default=settings.SERVICE_LOGO,
            upload_to=helper.service_image_path)
    customer_facing = models.BooleanField(default=False)
    internal = models.BooleanField(default=False)
    organisations = models.ManyToManyField(Organisation, blank=True)
    tags = models.TextField(default=None, blank=True, null=True)
    scientific_fields = models.TextField(default=None, blank=True, null=True)
    owner_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    owner_contact = models.CharField(max_length=255, default=None, blank=True, null=True)
    support_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    support_contact = models.CharField(max_length=255, default=None, blank=True, null=True)
    security_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    security_contact = models.CharField(max_length=255, default=None, blank=True, null=True)
    helpdesk = models.TextField(default=None, blank=True, null=True)
    order = models.TextField(default=None, blank=True, null=True)
    order_type = RichTextUploadingField(default=None, blank=True, null=True)
    changelog = models.TextField(default=None, blank=True, null=True)
    last_update = models.CharField(max_length=255, default=None, blank=True, null=True)
    required_services = models.ManyToManyField('self', blank=True,
                                               symmetrical=False,
                                               related_name='is_required_by')
    other_required_services = RichTextUploadingField(default=None, blank=True, null=True)
    related_services = models.ManyToManyField('self', blank=True,
                                              symmetrical=False,
                                              related_name='set_as_related_by')
    other_related_services = RichTextUploadingField(default=None, blank=True, null=True)
    related_platform = RichTextUploadingField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Unused fields
    service_category = models.ForeignKey(ServiceCategory, blank=False, null=True)
    description_external = RichTextUploadingField(default=None, blank=True, null=True)
    description_internal = RichTextUploadingField(default=None, blank=True, null=True)
    request_procedures = RichTextUploadingField(default=None, blank=True, null=True)
    funders_for_service = RichTextUploadingField(default=None, blank=True, null=True)
    risks = RichTextUploadingField(default=None, blank=True, null=True)
    competitors = RichTextUploadingField(default=None, blank=True, null=True)
    service_trl = models.ForeignKey(ServiceTrl, null=True)
    id_contact_information = models.ForeignKey(ContactInformation,
                                               null=True,
                                               related_name="external_contact_info")
    id_contact_information_internal = models.ForeignKey(ContactInformation,
                                                        null=True,
                                                        related_name="internal_contact_info")
    id_service_owner = models.ForeignKey(ServiceOwner, null=True)

    def __unicode__(self):
        return str(self.name)

    @property
    def organisations_names(self):
        return ", ".join(o.epp_bai_1_name for o in self.organisations.all())

    @property
    def service_categories_names(self):
        return "; ".join(o.name for o in self.service_categories.all())

    @property
    def related_services_names(self):
        return ", ".join(o.name for o in self.related_services.all())

    @property
    def required_services_names(self):
        return ", ".join(o.name for o in self.required_services.all())

    @property
    def service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="approved")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)

    @property
    def service_admins(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="approved")
        res = []
        for s in service_adminships:
            res.append(s.admin)
        return res

    @property
    def pending_service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="pending")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)

    @property
    def rejected_service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="rejected")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)


    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        clean_html_fields(self)
        super(Service, self).save(*args, **kwargs)


    @property
    def logo_absolute_path(self):
        if self.logo:
            path = self.logo.url
        else:
            path = settings.MEDIA_URL+settings.SERVICE_LOGO
        return helper.current_site_baseurl()+'/'+path


class ServiceStatus(models.Model):
    """
    Phase of the ServiceDetails lifecycle
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    value = models.CharField(max_length=255, default=None, blank=False, unique=True)
    description = models.TextField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceStatus, self).save(*args, **kwargs)


class ServiceDetails(models.Model):

    class Meta:
        unique_together = (("id_service", "version"))
        verbose_name_plural = "02. Service Versions"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    id_service = models.ForeignKey(Service, related_name="service_versions")
    version = models.CharField(max_length=255, default=None, blank=True)
    status = models.ForeignKey(ServiceStatus, default=None, blank=True) # allow empty field
    terms_of_use_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    privacy_policy_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    user_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    operations_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    monitoring_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    is_in_catalogue = models.BooleanField(default=False)
    visible_to_marketplace = models.BooleanField(default=False)
    sla_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    access_policies = models.ManyToManyField(AccessPolicy, blank=True)
    training_information = models.TextField(default=None, blank=True, null=True)
    maintenance_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    service_trl = models.ForeignKey(ServiceTrl, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Unused fields
    features_current = RichTextUploadingField(default=None, blank=True, null=True)
    features_future = RichTextUploadingField(default=None, blank=True, null=True)
    terms_of_use_has = models.NullBooleanField(default=False, blank=True)
    privacy_policy_has = models.NullBooleanField(default=False, blank=True)
    user_documentation_has = models.NullBooleanField(default=False, blank=True)
    operations_documentation_has = models.NullBooleanField(default=False, blank=True)
    monitoring_has = models.NullBooleanField(default=False, blank=True)
    accounting_has = models.NullBooleanField(default=False, blank=True)
    accounting_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    business_continuity_plan_has = models.NullBooleanField(default=False, blank=True)
    business_continuity_plan_url = models.CharField(max_length=255,
                                                    default=None,
                                                    blank=True,
                                                    null=True)
    disaster_recovery_plan_has = models.NullBooleanField(default=False, blank=True)
    disaster_recovery_plan_url = models.CharField(max_length=255,
                                                  default=None,
                                                  blank=True, null=True)
    decommissioning_procedure_has = models.NullBooleanField(default=False, blank=True)
    decommissioning_procedure_url = models.CharField(max_length=255,
                                                     default=None,
                                                     blank=True,
                                                     null=True)
    cost_to_run = models.CharField(max_length=255, default=None, blank=True, null=True)
    cost_to_build = models.CharField(max_length=255, default=None, blank=True, null=True)
    use_cases = RichTextUploadingField(default=None, blank=True, null=True)


    def __unicode__(self):
        primary_key = self.id_service.pk
        srv = Service.objects.get(pk=primary_key)
        return str(srv.name) + " " + str(self.version)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceDetails, self).save(*args, **kwargs)

    @property
    def service_admins_ids(self):
        return self.id_service.service_admins_ids


class ExternalService(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)
    service = models.CharField(max_length=255, default=None, blank=True, null=True)
    details = models.CharField(max_length=255, default=None, blank=True, null=True)


class Service_DependsOn_Service(models.Model):
    """
    Unused model
    """
    class Meta:
        unique_together = (('id_service_one', 'id_service_two'),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service_one = models.ForeignKey(Service, related_name='service_one')
    id_service_two = models.ForeignKey(Service, related_name='service_two')


class Service_ExternalService(models.Model):
    """
    Unused model
    """
    class Meta:
        unique_together = (('id_service', 'id_external_service'),)
        verbose_name_plural = "05. External Dependencies"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service = models.ForeignKey(Service)
    id_external_service = models.ForeignKey(ExternalService)


class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=255, default=None, unique=True)

    def __unicode__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(UserRole, self).save(*args, **kwargs)


class UserCustomer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(UserRole)
    role = RichTextUploadingField(default=None, blank=True, null=True)
    service_id = models.ForeignKey(Service)

    def __unicode__(self):
        return str(self.name) + " as " + str(self.role) + " for " + str(self.service_id)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(UserCustomer, self).save(*args, **kwargs)


class Roles(models.Model):
    """
    Unused model
    """
    id_user = models.ForeignKey(User)
    id_service = models.ForeignKey(Service)
    role = models.CharField(('role'), max_length=90, unique=True, default="spectator")

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Roles, self).save(*args, **kwargs)


class ServiceAdminship(models.Model):
    service = models.ForeignKey(Service, related_name="serviceadminships")
    admin = models.ForeignKey(User)
    state = models.CharField(
            choices=SERVICE_ADMINSHIP_STATES,
            max_length=30,
            default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("service", "admin"),)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceAdminship, self).save(*args, **kwargs)


class PostCreateService(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        service = data['backend/raw_response']
        ServiceAdminship.objects.create(
                service=service,
                admin=user,
                state='approved')
        return {}


class PostCreateMessage(ProcessorFactory):
    def process(self, data):
        content = data['response/content']
        service = {
            'data': content,
            'id': content.get('id'),
            'name': content.get('name'),
        }

        publish_message(service, 'create')
        return {}

class PostUpdateMessage(ProcessorFactory):
    def process(self, data):
        content = data['response/content']
        service = {
            'data': content,
            'id': content.get('id'),
            'name': content.get('name'),
        }

        publish_message(service, 'update')
        return {}

class PostDeleteMessage(ProcessorFactory):
    def process(self, data):
        content = data['backend/instance']
        service = {
            'data': '',
            'id': content.id,
            'name': content.name,
        }

        publish_message(service, 'delete')
        return {}


class PostCreateResourceadminship(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        http_host = data['request/meta/headers'].get('HTTP_HOST', 'Agora')

        sa = data['backend/raw_response']
        if sa.state == 'pending':
            send_email_application_created(sa, http_host)
        if sa.admin != user:
            send_email_resource_admin_assigned(sa, http_host)
        return {}


class PostPartialUpdateResourceadminship(ProcessorFactory):
    def process(self, data):
        http_host = data['request/meta/headers'].get('HTTP_HOST', 'Agora')
        send_email_application_evaluated(data['backend/raw_response'], http_host)
        return {}


class FederationMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, unique=True)
    webpage = models.CharField(max_length=255, default=None, blank=True,
                               null=True)
    logo = models.ImageField(default=settings.FEDERATION_MEMBER_LOGO,
                             upload_to=helper.federation_member_image_path)
    country = models.CharField(max_length=2, default=None)


class TargetUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=255, unique=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(TargetUser, self).save(*args, **kwargs)

class Supercategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Supercategory, self).save(*args, **kwargs)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supercategory = models.ForeignKey('service.Supercategory', blank=True, null=True, related_name='supercategory_category')
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Category, self).save(*args, **kwargs)

class Subcategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('service.Category', blank=True, null=True, related_name='category_subcategory')
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('category', 'name')

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Subcategory, self).save(*args, **kwargs)

class Resource(models.Model):

    # Basic Information fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    erp_bai_0_id = models.CharField(max_length=255, unique=True)
    erp_bai_1_name = models.CharField(max_length=80, default=None, unique=False)
    erp_bai_2_organisation = models.ForeignKey(Organisation,
            blank=False,
            null=True,
            related_name="organisation_services")
    erp_bai_3_providers = models.ManyToManyField(Organisation,
            blank=True,
            related_name="provided_services")
    erp_bai_4_webpage = models.EmailField(default=None, blank=False, null=True)

    # Marketing Information fields
    erp_mri_1_description = RichTextUploadingField(max_length=1000, default=None, blank=True,  null=True)
    erp_mri_2_tagline = models.TextField(max_length=100, default=None, blank=True, null=True)
    erp_mri_3_logo = models.EmailField(default=None, blank=True, null=True)
    erp_mri_4_mulitimedia = models.EmailField(default=None, blank=True, null=True)
    erp_mri_5_target_users = models.ManyToManyField(TargetUser, blank=True)
    erp_mri_6_target_customer_tags = models.TextField(default=None, blank=True, null=True)
    erp_mri_7_use_cases = RichTextUploadingField(max_length=100, default=None, blank=True,  null=True)

    # Classification information
    erp_cli_1_scientific_domain = models.ManyToManyField(
        Domain,
        blank=True,
        related_name='domain_resources')

    erp_cli_2_scientific_subdomain = models.ManyToManyField(
        Subdomain,
        blank=True,
        related_name='subdomain_resources')

    erp_cli_3_category = models.ManyToManyField(
        Category,
        blank=True,
        related_name='categorized_resources')

    erp_cli_4_subcategory = models.ManyToManyField(
        Subcategory,
        blank=True,
        related_name='subcategorized_resources')

    erp_cli_5_tags = models.TextField(max_length=50, default=None, blank=True, null=True)


    # Management Information
    erp_mgi_1_helpdesk_webpage       = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_2_helpdesk_email         = models.EmailField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_3_user_manual            = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_4_terms_of_use           = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_5_privacy_policy         = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_6_sla_specification      = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_7_training_information   = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_8_status_monitoring      = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_9_maintenance            = models.URLField(max_length=255, default=None, blank=True, null=True)

    # Geographical and Language Availability fields
    erp_gla_1_geographical_availability = models.CharField(max_length=255,
        default=None,
        blank=True,
        null=True)
    erp_gla_2_language = models.TextField(default=None, blank=True, null=True)

    # Contact Information
    main_contact = models.ForeignKey(ContactInformation,
        blank=True,
        null=True,
        related_name="main_contact_services")
    public_contact = models.ForeignKey(ContactInformation,
        blank=True,
        null=True,
        related_name="public_contact_services")

    def __unicode__(self):
        return str(self.erp_bai_0_id)

    @property
    def category_names(self):
        return ", ".join(o.name for o in self.erp_cli_3_category.all())

    @property
    def subcategory_names(self):
        return ", ".join(o.name for o in self.erp_cli_4_subcategory.all())

    @property
    def domain_names(self):
        return ", ".join(o.name for o in self.erp_cli_1_scientific_domain.all())

    @property
    def subdomain_names(self):
        return ", ".join(o.name for o in self.erp_cli_2_scientific_subdomain.all())

    @property
    def providers_names(self):
        return ", ".join(o.epp_bai_1_name for o in self.erp_bai_3_providers.all())

    @property
    def erp_mri_5_target_users_verbose(self):
        return ", ".join(o.user for o in self.erp_mri_5_target_users.all())

    def save(self, *args, **kwargs):
        self.erp_bai_0_id = self.erp_bai_0_id.strip()
        self.erp_bai_1_name = self.erp_bai_1_name.strip()
        clean_html_fields(self)
        super(Resource, self).save(*args, **kwargs)

    @property
    def resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="approved")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)

    @property
    def resource_admins(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="approved")
        res = []
        for r in resource_adminships:
            res.append(r.admin)
        return res

    @property
    def pending_resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="pending")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)

    @property
    def rejected_resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="rejected")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)


class ResourceAdminship(models.Model):
    resource = models.ForeignKey(Resource, related_name="resourceadminships")
    admin = models.ForeignKey(User)
    state = models.CharField(
            choices=SERVICE_ADMINSHIP_STATES,
            max_length=30,
            default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("resource", "admin"),)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ResourceAdminship, self).save(*args, **kwargs)

class PostCreateResource(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        resource = data['backend/raw_response']
        ResourceAdminship.objects.create(
                resource=resource,
                admin=user,
                state='approved')
        return {}
