from django.contrib import admin
from .models import * 

# For multiple images for a product
############ START ######################## 
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    search_fields = ('prod_id', 'title' )

    class Meta:
       model = Product
 
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
############## END ########################

# For search field 
class SubCategoryAdmin(admin.ModelAdmin):
    model = SubCategory
    search_fields = ('id', 'sub_category', 'category__category')

class CarouselImageAdmin(admin.ModelAdmin):
    model = CarouselImage
    search_fields = ('id',)
    ordering = ('-id',)  # Must be a list or tuple

admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brand)
admin.site.register(FeatureItem)