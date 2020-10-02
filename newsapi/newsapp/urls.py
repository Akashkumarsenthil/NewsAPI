from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.headlines),
    path('blockchain/', views.blockchain),
    path('business/', views.business),
    path('apple/', views.apple),
    path('techcrunch/', views.techcrunch),
    path('wallstreet', views.wallstreet),


]
