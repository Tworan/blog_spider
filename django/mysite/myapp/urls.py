from django.conf.urls import url, include
from myapp import views

urlpatterns = [
    url(r'show_BlogUser$', views.show_BlogUser, ),
    url(r'add_user$', views.add_user, ),
    url(r'show_hotboard$', views.show_hotboard, ),
    url(r'add_bloguserall$', views.add_bloguserall, ),
]
