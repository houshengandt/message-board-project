from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'messageboard_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('messageboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
