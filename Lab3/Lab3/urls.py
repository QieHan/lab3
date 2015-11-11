from django.conf.urls import *
from my_library.views import book_all,book_add,first_page,book_find,return_find,delete_book,author_add,\
show_book,change_book
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    ('^first_page/$',first_page),
    ('^book_all/$',book_all),
    ('^book_add/$',book_add),
    ('^return_find/$',return_find),
    ('^book_find/$',book_find),
    ('^delete_book/$',delete_book),
    ('^author_add/$',author_add),
    ('^show_book/$',show_book),
    ('^change_book/$',change_book),
    (r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': 'G:\Library\Lab3\static'}),
    # Examples:
    # url(r'^$', 'Lab3.views.home', name='home'),
    # url(r'^Lab3/', include('Lab3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls))
)
