# views.py

from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

class InvoiceListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailListView(generics.ListCreateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer

class InvoiceDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InvoiceDetailSerializer 

    def get_queryset(self):
        # Filter the queryset to retrieve only the detail related to the specified invoice
        invoice_id = self.kwargs['invoice_id']
        return InvoiceDetail.objects.filter(invoice_id=invoice_id)
