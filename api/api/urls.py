"""
Definition of urls for api.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from stores.resources import StoreResource
store_resource = StoreResource()

urlpatterns = [
    # Examples:
    # url(r'^$', api.views.home, name='home'),
    # url(r'^api/', include('api.api.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(store_resource.urls)),
]
