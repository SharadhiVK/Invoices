# Import necessary modules
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

# Import models
from invoices.models import Invoice, InvoiceDetail

def create_invoice_detail():
    try:
        # Retrieve an existing invoice (you need to replace 'your_invoice_id' with the actual invoice ID)
        invoice = Invoice.objects.get(id=your_invoice_id)

        # Create a new invoice detail
        invoice_detail = InvoiceDetail.objects.create(
            invoice=invoice,
            description="Your description here",
            quantity=3,
            unit_price=10.50,
            price=31.50  # Make sure to calculate the price based on quantity and unit_price
        )

        # Print success message
        print("Invoice Detail created successfully:", invoice_detail)

    except Invoice.DoesNotExist:
        print("Invoice does not exist.")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    create_invoice_detail()
