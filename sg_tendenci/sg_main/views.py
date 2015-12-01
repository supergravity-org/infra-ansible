from django.shortcuts import render
from oauth2_provider.decorators import protected_resource


@protected_resource()
def user_json(request):
    # An access token is required to get here...
    # ...
    pass
