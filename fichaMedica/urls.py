from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.urls import re_path
from django.conf.urls import include

admin.site.site_header = 'Consultorio 6 de Mayo'
admin.site.site_title = 'Consultorio'

urlpatterns = [
#   path('grappelli/', include('grappelli.urls')),
    path('', admin.site.urls),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT})
]
