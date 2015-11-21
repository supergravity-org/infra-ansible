from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from optparse import make_option
import sys

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--user',
            action='store',
            default=None,
            help='Username for new user'),
        make_option('--password',
            action='store',
            default=None,
            help='User Password'),
        make_option('--superuser',
            action='store_true',
            default=False,
            help='Is superuser'),
        make_option('--email',
            action='store',
            default=None,
            help='User Email Address'),
        )

    def handle(self, *args, **kwargs):
        if User.objects.filter(username=kwargs.get('user')).count() > 0:
            print("user %s already exist" % kwargs.get('user'))
            sys.exit(0)
        if kwargs.get('superuser'):
            user = User.objects.create_superuser(
                username=kwargs.get('user'),
                email=kwargs.get('email'),
                password=kwargs.get('password')
            )
        else:
            user = User.objects.create_user(
                username=kwargs.get('user'),
                email=kwargs.get('email')
            )
            user.set_password(kwargs.get('password'))
        user.save()
