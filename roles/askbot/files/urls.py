""" Main url configuration file for the askbot site. """

from django.conf import settings
try:
    from django.conf.urls import handler404
    from django.conf.urls import include, patterns, url
except ImportError:
    from django.conf.urls.defaults import handler404
    from django.conf.urls.defaults import include, patterns, url

from askbot.views.error import internal_error as handler500
from django.contrib import admin

admin.autodiscover()

if getattr(settings, 'ASKBOT_MULTILINGUAL', False) is True:
    from django.conf.urls.i18n import i18n_patterns
    urlpatterns = i18n_patterns(
        '',
        (r'%s' % settings.ASKBOT_URL, include('askbot.urls'))
    )
else:
    urlpatterns = patterns(
        '',
        (r'%s' % settings.ASKBOT_URL, include('askbot.urls'))
    )

urlpatterns += patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    #(r'^cache/', include('keyedcache.urls')), - broken views disable for now
    #(r'^settings/', include('askbot.deps.livesettings.urls')),
    (r'^followit/', include('followit.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^robots.txt$', include('robots.urls')),
    url(  # TODO: replace with django.conf.urls.static ?
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
    ),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns(
        '',
        url(r'^rosetta/', include('rosetta.urls'))
    )

handler500 = 'askbot.views.error.internal_error'
