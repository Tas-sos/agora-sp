from django.db.models import Q
from django.utils.translation import ugettext as _
from apimas.errors import ValidationError
from service.models import ServiceAdminship as sa_m
from component.models import ServiceDetailsComponent as cidl_m
from accounts.models import User as user_m


class ServiceAdminship(object):

    @staticmethod
    def check_create_other(backend_input, instance, context):
        """Admins/superadmins can create ServiceAdminships.

        Admins/superadmins can create a new ServiceAdminship instance
        for a given service and a given user, only if the user has role
        'serviceadmin' and she/he does not already admin the service.
        The ServiceAdminship created by admins/superadmins has state
        'approved'.

        """
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
        """Serviceadmins can request ServiceAdminships.

        A user can create a ServiceAdminship instance only if she/he does not
        already admin the service.
        The ServiceAdminship created is not yet approved/rejected, so it is
        created with state 'pending'.

        """
        auth_user = context['auth/user']
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
        """Serviceadmins retrieve ServiceAdminships they are involved in.

        Serviceadmins can retrieve ServiceAdminships of Services they admin, so
        that they can reject/approve these ServiceAdminships.
        Serviceadmins can also retrieve the ServiceAdminship for which they are
        admins regardlress of the state, so that they can view a
        ServiceAdminship request or revoke one.

        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_services = [x.service for x in user_sa]
        if instance.service in user_services:
            return instance
        if instance.admin == auth_user:
            return instance
        return None

    @staticmethod
    def check_update(backend_input, instance, context):
        """Check allowed transitions between ServiceAdminship instances.

        The transition between 'approved' and 'rejected' must go via 'pending'.

        """
        TRANSITIONS = set([
            ('pending', 'approved'),
            ('pending', 'rejected'),
            ('rejected', 'pending'),
            ('approved', 'pending'),
        ])

        current_state = instance.state
        input_state = backend_input['state']

        if (current_state, input_state) not in TRANSITIONS:
            raise ValidationError(_('Transition not allowed'))

    @staticmethod
    def manages(context):
        """Serviceadmins can partially update some ServiceAdminships.

        A serviceadmin can partially update ServiceAdminships of services
        he/she admins.
        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_services = [x.service for x in user_sa]

        return Q(service__in=user_services) & ~Q(admin=auth_user)

    @staticmethod
    def manages_or_self_pending(context):
        """Serviceadmins list a subset of ServiceAdminships.

        A serviceadmin can list ServiceAdminships if he/she has applied for
        a ServiceAdminship and is still in state 'pending' so that he/she can
        revoke it, if he/she has an approved ServiceAdminship, or if he/she
        admins the service of the ServiceAdminship.
        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        services = [x.service for x in user_sa]
        self_pending = Q(admin=auth_user, state='pending')

        return (Q(service__in=services) & ~Q(admin=auth_user)) | self_pending

    @staticmethod
    def self_pending(context):
        """A serviceadmin can delete a ServiceAdminship.

        A serviceadmin can delete a ServiceAdminship so that she/he can
        revoke the ServiceAdminship application.
        The ServiceAdminship should still be in state 'pending' and the admin
        should be the user.
        """
        auth_user = context['auth/user']

        return Q(admin=auth_user, state='pending')


class Service(object):

    @staticmethod
    def owned(backend_input, instance, context):
        """Servicadmins can update Services they own.

        A serviceadmin owns a Service if service's service_admins_ids
        computed property contains the id of the user.

        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.service_admins_ids.split(",")
        if auth_user_id in service_admins_ids:
            return
        else:
            raise ValidationError(_('Unauthorized action'))

    @staticmethod
    def filter_owned(context):
        """List only the Services a serviceadmins owns.

        List all the Services that belong to a ServiceAdminship where the admin
        is the user and are in state 'approved'.
        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)
        user_sa = sa_m.objects.filter(admin__id=auth_user_id, state='approved')
        services = [x.service.id for x in user_sa]
        return Q(id__in=services)


class User(object):

    @staticmethod
    def me(context):
        """
        A serviceadmin can only retrieve herself.
        """
        auth_user = context['auth/user']
        return Q(id=auth_user.id)


class CIDL(object):

    @staticmethod
    def unique(backend_input, instance, context):
        """Admins/superadmins create CIDL with unique service_type.
        """
        try:
            cidl_m.objects.get(service_type=backend_input['service_type'])
            raise ValidationError(_('Service_type should be unique'))
        except cidl_m.DoesNotExist:
            return

    @staticmethod
    def create_owns_service_unique(backend_input, instance, context):
        """Serviceadmins can conditionally create CIDLs.

        A serviceadmin can create a CIDL only if he/she admins the Service of
        the CIDL.
        The CIDL is created only if the service_type is unique.
        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)

        try:
            sa_m.objects.get(admin=auth_user_id,
                             service=backend_input['service_id_id'])
        except sa_m.DoesNotExist:
            raise ValidationError(_('User should admin the service'))
        try:
            cidl_m.objects.get(service_type=backend_input['service_type'])
            raise ValidationError(_('Service_type should be unique'))
        except cidl_m.DoesNotExist:
            return

    @staticmethod
    def update_owns_service_unique(backend_input, instance, context):
        """CIDL update rules for serviceadmins.

        A serviceadmin can update a CIDL only if she/he admins the Service of
        the CIDL. She/he should also admin the updated Service.
        If there is an update in the value of the service_type, it should be
        unique.
        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.service_admins_ids.split(",")

        if auth_user_id not in service_admins_ids:
            raise ValidationError(_('Unauthorized action'))

        try:
            sa_m.objects.get(admin=auth_user_id,
                             service=backend_input['service_id_id'])
        except sa_m.DoesNotExist:
            raise ValidationError(_('User should admin the service'))

        if (backend_input['service_type'] == instance.service_type):
            return

        try:
            cidl_m.objects.get(service_type=backend_input['service_type'])
            raise ValidationError(_('Service_type should be unique'))
        except cidl_m.DoesNotExist:
            return

    @staticmethod
    def update_unique(backend_input, instance, context):
        """CIDL update rules for admins/superadmins.

        If a admin/superadmin updates a CIDL, the new service_type value should
        be unique.
        """

        if (backend_input['service_type'] == instance.service_type):
            return

        try:
            cidl_m.objects.get(service_type=backend_input['service_type'])
            raise ValidationError(_('Service_type should be unique'))
        except cidl_m.DoesNotExist:
            return


class ServiceVersion(object):

    @staticmethod
    def update_owns_service(backend_input, instance, context):
        """ ServiceVersions update rules for serviceadmins.

        Serviceadmins can update a ServiceVersion if they  own the Service of 
        the ServiceVersion. If they choose to update the Service, they should
        also own the new Service.
        """

        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.service_admins_ids.split(",")

        try:
            sa_m.objects.get(admin=auth_user_id,
                             state='approved',
                             service=backend_input['id_service_id'])
        except sa_m.DoesNotExist:
            raise ValidationError(_('User should admin the service'))

        if auth_user_id in service_admins_ids:
            return
        else:
            raise ValidationError(_('Unauthorized action'))

    @staticmethod
    def create_owns_service(backend_input, instance, context):
        """
        Serviceadmins can create ServiceVersion of Services the admin.

        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)

        try:
            sa_m.objects.get(admin=auth_user_id,
                             service=backend_input['id_service_id'])
        except sa_m.DoesNotExist:
            raise ValidationError(_('User should admin the service'))
