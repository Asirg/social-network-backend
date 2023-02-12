from django.urls import path

from . import views


urlpatterns = [
    # path('user/', views.UserViewSet.as_view({'get': 'list'})),
    # path('user/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
    path('user/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'})),
]
