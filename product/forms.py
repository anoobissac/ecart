from django import forms
from product.models import CategoryModel, ProductModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        # fields = ['name','price','image','category','description','unit']
        exclude = ('status', 'created_on', 'updated_on')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['name']
        # exclude = ('status', 'created_on', 'updated_on')