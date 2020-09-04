from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from public.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('influencer/', include('influencer.urls')),
    path('business/', include('business.urls')),
    path('accounts/', include('user.urls')),
    path('memer/', include('memer.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)