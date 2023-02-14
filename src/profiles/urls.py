from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserRetrieveView.as_view()),

    path('users/subscribers/<int:pk>/', views.SubscribersListView.as_view()),
    path('users/subscriptions/<int:pk>/', views.SubscriptionsListView.as_view()),

    path('users/technology/', views.TechnologyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('users/technology/<str:url>/', views.TechnologyViewSet.as_view({'get': 'retrieve'})),

    path('follower/<int:pk>/', views.FollowerViewSet.as_view({'put': 'update', 'delete': 'destroy', 'get': 'retrieve'})),
]