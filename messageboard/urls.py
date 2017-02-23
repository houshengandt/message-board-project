from django.conf.urls import url

from messageboard import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='messageboardindex'),
    url(r'^leave-message/$', views.leave_message, name='leave_message'),
]
