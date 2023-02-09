from django.urls import path

from wall import views


urlpatterns = [
    path('wall/', views.WallView.as_view({'get': 'list'})),
    # path('wall/<int:pk>', views.UserWallView.as_view({'get': 'retrieve'})),
    # path('wall/', views.WallView.as_view({'get': 'retrieve'})),
    # path('wall/<int:pk>', )
]