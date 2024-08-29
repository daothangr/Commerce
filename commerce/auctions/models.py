from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AuctionList(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1000)
    price = models.IntegerField()
    closed = models.BooleanField(default = False)
   


class Link(models.Model):
    product = models.ForeignKey(AuctionList, on_delete=models.CASCADE, blank=True, null=True, related_name="product_link")
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="person_link")
    bid = models.IntegerField(null = True)
    isActive = models.BooleanField(default=False)
    watchList = models.BooleanField(default=False)
    
    
class Comment(models.Model):
    product = models.ForeignKey(AuctionList, on_delete=models.CASCADE, blank=True, null=True, related_name="product_comment")
    person = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="person_comment")
    comment = models.CharField(max_length=1000, null = True)


    


