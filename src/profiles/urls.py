from django.urls import path

from . import views


urlpatterns = [
    path('user/', views.UserViewSet.as_view({'get': 'list'})),
    path('follower/', views.FollowerViewSet.as_view({'get': 'list', 'post': 'create',})),
    path('follower/<int:pk>/', views.FollowerViewSet.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
    path('technology/', views.TechnologyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('technology/<str:url>/', views.TechnologyViewSet.as_view({'get': 'retrieve'})),
    path('user/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'})),
]