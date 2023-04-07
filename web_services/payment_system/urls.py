from django.urls import path

from . import views

urlpatterns = [
    path('purchase_tickets/', views.PurchaseTicketsView.as_view(), name='purchase_tickets'),
]
