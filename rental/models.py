from django.db import models

class Customer(models.Model):
    cust_id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    area = models.CharField(max_length=10)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    price = models.FloatField()

class Invoice(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    issue_date = models.DateField()