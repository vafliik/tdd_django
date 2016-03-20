from django.conf.urls import include, url
import lists.views

urlpatterns = [
    url(r'^$', lists.views.home_page, name='home'),
    url(r'^lists/', include('lists.urls')),
]
