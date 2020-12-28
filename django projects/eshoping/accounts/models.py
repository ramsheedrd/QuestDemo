from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccounts(AbstractUser):
    phone = models.CharField(max_length=15)
    dob = models.DateField()


class ProfilePicture(models.Model):
    user = models.OneToOneField(UserAccounts, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='dp') #pillow
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)



# class Category():
#     name


# class Product():
#     Category
#     Name
#     Price
#     Description
#     Image
#     Stock


# class Review():
#     product
#     review


# class Cart:
#     User
#     Product
#     count

# class Payment:
#     User
#     Product
#     Total
#     Discount









    
