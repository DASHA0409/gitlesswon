from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price',
                    'created_date', 'updated_date', 'auction', 'user', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ('Общее', {'fields': ('title', 'description', 'user', 'image')}),

        ('Финансы', {'fields': ('price', 'auction'),
                     'classes': ['collapse']
                     })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Добавить возможность торга')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='Thumbnail')
    def thumbnail_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50px" />', obj.image.url)
        return "No Image"

    if obj.image:
        return format_html('<img src="{}" height="50px" />', obj.image.url)
    return format_html('<img src="/static/img/adv.png" height="50px" />')

    list_display = ['thumbnail_preview', ]
admin.site.register(Advertisement, AdvertisementAdmin)