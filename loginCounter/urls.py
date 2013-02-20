from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^users/login$', 'loginCounter.views.login'),
    url(r'^users/add$', 'loginCounter.views.add'),
    url(r'^TESTAPI/resetFixture$', 'loginCounter.views.resetFixture'),
    url(r'^TESTAPI/unitTests$', 'loginCounter.views.unitTests'),
    # url(r'^loginCounter/', include('loginCounter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
