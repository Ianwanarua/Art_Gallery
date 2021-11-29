from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.showpage,name='art'),
    url(r'^search/', views.search_category, name='search_category'),
    url('^image/(?P<image_id>\d+)/$',views.image_properties, name='image'),
    url(r'^location/(?P<location_name>\w+)',views.image_location,name = 'location'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)