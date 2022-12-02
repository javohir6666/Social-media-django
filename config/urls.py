from django.contrib import admin
from django.urls import path, include
from landing.views import Index
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('landing.urls')),
    path("social/", include('social.urls')),
    path('accounts/', include('allauth.urls')),
]
