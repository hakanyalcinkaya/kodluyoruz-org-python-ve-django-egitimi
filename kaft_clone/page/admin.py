from django.contrib import admin
from .models import Page, Carousel


class PageModify(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status', 
        'updated_at',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'status', 
    )


admin.site.register(Page, PageModify)
admin.site.register(Carousel)