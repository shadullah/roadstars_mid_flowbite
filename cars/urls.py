from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>', views.DetailsCAr.as_view(), name='details'),
    path('buynow/<int:car_id>/', views.buy_now, name='buynow')
]
