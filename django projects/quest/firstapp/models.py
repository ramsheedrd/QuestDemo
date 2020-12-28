from django.db import models

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=120, null=False)
    price = models.PositiveIntegerField(null=False)
    seller = models.CharField(max_length=110, null=False)
    category = models.CharField(max_length=60, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products" 
        # ordering = ['name']


    def __str__(self):
        return self.name







