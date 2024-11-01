from django.urls import path

from . import views

# HTTP Request <-> HTTP Response
# MVT (MVC)

urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]