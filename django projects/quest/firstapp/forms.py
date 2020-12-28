from django import forms
from .models import ProductModel

class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name")
    price = forms.IntegerField(widget=forms.TextInput)
    seller = forms.CharField(widget=forms.TextInput)
    category = forms.CharField()
    
    def clean_price(self):
        p = self.cleaned_data["price"]
        if p < 0:
            raise forms.ValidationError("Positive Integer Required")
        return p


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = ['name', 'price', 'seller', 'category']
        widgets = {'price':forms.TextInput}
        labels = {'name': 'Product Name'}
        # exclude = ['seller']