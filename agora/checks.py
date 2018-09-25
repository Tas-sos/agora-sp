from django.db.models import Q
from django.utils.translation import ugettext as _
from apimas.errors import ValidationError
from service.models import ServiceAdminship as sa_m
from component.models import ServiceDetailsComponent as cidl_m
from accounts.models import User as user_m
from agora.utils import safe_html

import logging
logger = logging.getLogger('apimas')



class ServiceAdminship(object):

    @staticmethod
    def check_create_other(backend_input, instance, context):
        admin = user_m.objects.get(id=backend_input['admin_id'])
        if admin.role != 'serviceadmin':
            raise ValidationError(_('Wrong admin role'))
        try:
            sa_m.objects.get(admin=backend_input['admin_id'],
                             service=backend_input['service_id'])
            raise ValidationError(_('Object exists'))
        except sa_m.DoesNotExist:
            backend_input['state'] = 'approved'
            return

    @staticmethod
    def check_create_self(backend_input, instance, context):
        auth_user = context.extract('auth/user')
        try:
            sa_m.objects.get(admin=auth_user.id,
                             service=backend_input['service_id'])
            raise ValidationError(_('Object exists'))
        except sa_m.DoesNotExist:
            backend_input['admin_id'] = auth_user.id
            backend_input['state'] = 'pending'
            return

    @staticmethod
    def is_involved(instance, context):
        auth_user = context.extract('auth/user')
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_services = [x.service for x in user_sa]
        if instance.service in user_services:
            return instance
        if instance.admin == auth_user:
            return instance
        return None

    @staticmethod
    def check_update(backend_input, instance, context):
        TRANSITIONS = set([
            ('pending', 'approved'),
            ('pending', 'rejected'),
            ('rejected', 'pending'),
            ('approved', 'pending'),
        ])

        current_state = instance.state
        input_state = backend_input['state']

        if (current_state, input_state) not in TRANSITIONS:
            raise ValidationError("Transition not allowed")

    @staticmethod
    def manages(context):
        auth_user = context.extract('auth/user')
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_services = [x.service for x in user_sa]

        return Q(service__in=user_services) & ~Q(admin=auth_user)

    @staticmethod
    def manages_or_self_pending(context):
        auth_user = context.extract('auth/user')
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        services = [x.service for x in user_sa]
        self_pending = Q(admin=auth_user, state='pending')

        return (Q(service__in=services) & ~Q(admin=auth_user)) | self_pending

    @staticmethod
    def self_pending(context):
        auth_user = context.extract('auth/user')

        return Q(admin=auth_user, state='pending')


class Service(object):

    @staticmethod
    def owned(backend_input, instance, context):
        auth_user = context.extract('auth/user')
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.service_admins_ids.split(",")
        if auth_user_id in service_admins_ids:
            return
        else:
            raise ValidationError("Unauthorized action")


class User(object):

    @staticmethod
    def me(context):
        auth_user = context.extract('auth/user')
        return Q(id=auth_user.id)


class CIDL(object):

    @staticmethod
    def unique(backend_input, instance, context):
        try:
            cidl_m.objects.get(service_type=backend_input['service_type'])
            raise ValidationError("Service_type should be unique")
        except cidl_m.DoesNotExist:
            return


class Component(object):

    @staticmethod
    def clean_html(backend_input, instance, context):
        description = backend_input['description']
        backend_input['description'] = safe_html(description)
        logger.info(description)
        return
