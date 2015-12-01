from django.conf.urls import include, patterns, url

# Add additional url patterns for additional apps
# here and they will be included in the main urls.py
extrapatterns = patterns('',
     (r'^explorer/', include('explorer.urls')),
     (r'^explorer/', include('tendenci.apps.explorer_extensions.urls')),
     #(r'^helpdesk/', include('helpdesk.urls')),
     ('^', include('tendenci.apps.committees.urls')),
     ('^', include('tendenci.apps.case_studies.urls')),
     ('^', include('tendenci.apps.donations.urls')),
     ('^', include('tendenci.apps.speakers.urls')),
     ('^', include('tendenci.apps.staff.urls')),
     ('^', include('tendenci.apps.studygroups.urls')),
     ('^', include('tendenci.apps.videos.urls')),
     ('^', include('tendenci.apps.testimonials.urls')),
     (r'^', include('tendenci.apps.social_services.urls')),
)

extrapatterns += patterns('',
    url(r'^auth/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^auth/o/', include('provider.oauth2.urls', namespace = 'oauth2')),
    url(r'^auth/cas/',  include('mama_cas.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include('sg_main.api')),
)
