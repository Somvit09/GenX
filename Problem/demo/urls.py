from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("authentication.urls")), # Auth routes - login / register
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)