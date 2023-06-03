from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membership_card_balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.customer.name} at {self.shop.name}"


class MembershipCard(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Membership Card: {self.card_number}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    times_deducted = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=8, decimal_places=2)
    sales_commission_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
