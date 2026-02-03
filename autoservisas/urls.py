from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:order_id>', views.OrderDetailView.as_view(), name='order'),
]