from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    icon = models.ImageField(upload_to='images/')
    image = models.ImageField(upload_to='images/')
    votes = models.IntegerField(default=0)
    body = models.TextField()
    product_url = models.CharField(max_length=100)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')

    def __str__(self):
        return self.title


class Voter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
