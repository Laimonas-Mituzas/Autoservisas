from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dash/', views.dashboard, name='dash'),
    path('cars/', views.cars, name='cars'),
    # path('cars/<int:car_id>', views.car, name='car'), # medziagoje sitas variantas
    path('car/<int:car_id>', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order'),
    path('search/', views.search, name='search'),
]