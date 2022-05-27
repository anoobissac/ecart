from django.contrib import admin
from product.models import CategoryModel,UnitModel,ProductModel,ReviewModel,CartModel


# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(UnitModel)
admin.site.register(ProductModel)
admin.site.register(ReviewModel)
admin.site.register(CartModel)