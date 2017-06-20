"""URL patterns for threads"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # page for all threads
    url(r'^threads/$', views.threads, name='threads'),
    # page for single thread
    url(r'^threads/(?P<topic_id>\d+)/$', views.thread, name='thread'),

    # page for making a new thread
    url(r'^new_thread/$', views.new_thread, name='new_thread'),
    # page for replying to a thread
    url(r'^new_message/(?P<topic_id>\d+)/$', views.new_message,
        name='new_message'),
]