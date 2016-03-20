from django.conf.urls import url
import lists.views

urlpatterns = [
    url(r'^new$', lists.views.new_list, name='new_list'),
    url(r'^(\d+)/add$', lists.views.add_item, name='add_item'),
    url(r'^(\d+)/$', lists.views.list_view, name='list_view'),
]
