from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    # Examples:
    # url(r'^$', 'messageboard_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^', include('messageboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
