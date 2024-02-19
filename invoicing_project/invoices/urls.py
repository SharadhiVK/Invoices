from django.urls import path
from . import views

urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),
    path('invoices/details/', views.InvoiceDetailListView.as_view(), name='invoice-detail-list'),
    path('invoices/<int:invoice_id>/details/<int:pk>/', views.InvoiceDetailDetailView.as_view(), name='invoice-detail-detail'),
]
