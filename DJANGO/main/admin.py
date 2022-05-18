from django.contrib import admin

from .models import Users, Product, Category, Cart

admin.site.register(Users)
admin.site.register(Cart)


class PostImageAdmin(admin.StackedInline):
    model = Category

    prepopulated_fields = {"slug": ("name",)}

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]


    class Meta:
        model = Product


@admin.register(Category)
class PostImageAdmin(admin.ModelAdmin):
    pass

