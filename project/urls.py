from django.contrib import admin
from django.urls import path,include
# importing django settings file
from django.conf import settings
# importing static files urls
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mcv_app.urls',namespace='mcv')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)