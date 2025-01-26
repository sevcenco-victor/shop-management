from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def validate_stock(self, value):
        if value <= 0:
            raise ValidationError("Stock must be greater than zero.")
        return value


    def __str__(self):
        return self.name


class Order(models.Model):
    class OrdersStatus(models.TextChoices):
        PENDING = "Pending"
        COMPLETED = "Completed"
        SHIPPED = "Shipped"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    status = models.CharField(
        max_length=10,
        choices=OrdersStatus.choices,
        default=OrdersStatus.PENDING,
    )

    def __str__(self):
        return f"{self.user} - {self.date}"


class Payment(models.Model):
    class PaymentTypes(models.TextChoices):
        CREDIT_CARD = "Credit Card"
        PAYPAL = "Paypal"
        ON_DELIVERY = "On Delivery"

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentTypes.choices
    )

    def __str__(self):
        return f"{self.user.username} {self.date} {self.total_sum}"
