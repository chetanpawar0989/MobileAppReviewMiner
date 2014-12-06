from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MobileAppReviews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls)),

    url(r'^reviewminer/', include('ReviewMiner.urls', namespace='ReviewMiner')),
)
