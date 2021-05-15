from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import myapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^api/', include(myapp.urls)),
    url(r'^', include(myapp.urls)),
]
