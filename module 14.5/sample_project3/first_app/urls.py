from django.urls import path
# from . import views
from first_app.views import home,index
urlpatterns = [
    # path('', views.home, name='homepage'),
    path('', home, name='homepage'),
    path('first_app/', index, name='modelformpage'),
]
