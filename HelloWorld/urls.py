from django.conf.urls import *
from django.contrib import admin
from HelloWorld.view import hello
from HelloWorld.testdb import testdb
from HelloWorld import search
from HelloWorld import search2


admin.autodiscover()

urlpatterns = patterns(
    "",
    (r'^admin/', include(admin.site.urls)),
    ('^hello/$', hello),
    ('^testdb/$', testdb),
    (r'^search-form/$', search.search_form),
    (r'^search/$', search.search),
    (r'^search-post/$', search2.search_post),
)