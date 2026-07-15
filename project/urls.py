from django.contrib import admin
from django.urls import path
from rental import views

urlpatterns = [
    path('admin/', admin.site.urls),   # 👈 ADD THIS LINE
    path('', views.movie_list),
    path('customers/', views.customer_list),
    path('invoices/', views.invoice_list),
]
