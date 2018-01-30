from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from agora.settings import AVATAR_LOCATION
from agora.settings import USER_CREATION_EMAIL_LIST
from rest_framework.authtoken.models import Token
import datetime
import pytz

class UserManager(BaseUserManager):

    def _create_user(self,username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):

        return self._create_user( username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):

        return self._create_user( username, email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions

    """
    username = models.CharField(('username'), max_length=30, unique=True, default=None)
    email = models.EmailField(('email address'), max_length=254, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(('staff status'), default=False,
        help_text=('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(('active'), default=True,
        help_text=('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    avatar = models.ImageField(upload_to= AVATAR_LOCATION, blank=True)
    shibboleth_id = models.CharField(
                    max_length=255, unique=True, null=True, default=None)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

#    def retrieve_complete_social_info(self):
#        social_user = UserSocialAuth.objects.get({"Uid": self.email})
#
#        return social_user

    def __unicode__(self):
        return  str(self.email)


@receiver(post_save,sender=User)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):

    utc=pytz.UTC

    date_joined = instance.date_joined.replace(tzinfo=utc).replace(microsecond=0)
    now = datetime.datetime.now().replace(tzinfo=utc).replace(microsecond=0)

    if date_joined < now:
        pass
    else:
        token = Token.objects.get_or_create(user=instance)
