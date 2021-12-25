from django.conf.urls.static import static
from django.urls import include, path
from django.contrib import admin
from djangorestfilesupload import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fileupload.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

