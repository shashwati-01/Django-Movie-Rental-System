from django.shortcuts import render
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'rental/home.html', {'movies': movies})

from .models import Movie, Customer, Invoice
from django.shortcuts import render

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'rental/home.html', {'movies': movies})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'rental/customer.html', {'customers': customers})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'rental/invoice.html', {'invoices': invoices})
