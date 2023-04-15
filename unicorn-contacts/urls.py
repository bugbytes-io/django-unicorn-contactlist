from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('allauth.urls')),
    path("unicorn/", include("django_unicorn.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
