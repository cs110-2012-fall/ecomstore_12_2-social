from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #(r'^$','preview.views.home'),
    (r'contact.html','ecomstore.preview.views.contact'),
    (r'about.html'  ,'ecomstore.preview.views.about'),
    (r'services.html','ecomstore.preview.views.services'),
    (r'index.html'    ,'ecomstore.preview.views.home'),
    (r'shop_online.html',include('ecomstore.catalog.urls')),
  
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
     (r'^cart/' , include('ecomstore.cart.urls')),
     (r'^accounts/',include('ecomstore.accounts.urls')),
     (r'^accounts/',include('django.contrib.auth.urls')),
     (r'^checkout/', include('ecomstore.checkout.urls')),
     (r'^search/', include('ecomstore.search.urls')),
     (r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)

