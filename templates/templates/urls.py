
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('basic/', include('basic.urls')),
    path('admin/', admin.site.urls),
]
