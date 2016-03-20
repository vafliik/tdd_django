from django.conf.urls import include, url
from django.contrib import admin
import lists.views

urlpatterns = [
    url(r'^$', lists.views.home_page, name='home'),
    url(r'^lists/(\d+)/add$', lists.views.add_item, name='add_item'),
    url(r'^lists/(\d+)/$', lists.views.list_view, name='list_view'),
    url(r'^lists/new$', lists.views.new_list, name='new_list'),

    #url(r'^admin/', include(admin.site.urls)),
]
