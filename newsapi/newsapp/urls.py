from django.urls import path
from . import views
urlpatterns = [
    path('', views.headlines)
    
#    path('', views.blockchain)
#    path('', views.business)
#    path('', views.Apple)
#    path('', views.Techcrunch)
#    path('', views.Wallstreet)


]
