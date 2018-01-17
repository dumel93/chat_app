from django.conf.urls import url

from django.contrib.auth import views as auth_views
from django.template.context_processors import static

from app_sport import settings
from . import views



app_name='accounts'


urlpatterns=[

    url(r'^login/', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/',views.UserLogoutView.as_view(), name='logout'),
    url(r'^signup/', views.UserCreateView.as_view(), name ='signup'),
]