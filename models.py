from django.db import models
from django.contrib import admin
class Advertisement(models.Model):
        title = models.CharField("заголовок", max_length=128)
        description = models.TextField("описание")
        price = models.DecimalField("цена", max_digits=10, decimal_places=2)
        auction = models.BooleanField("торг",  help_text="Отметьте, если торг уместен")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        @admin.display(description='Дата создания')
        def get_updated_at(self, obj):
            from django.utils import timezone
            if obj.updated_at.date() == timezone.now().date():
                return format_html(f'<span style="color: red">Сегодня в {obj.updated_at.strftime("%H:%M")}</span>')
                else:
                return obj.updated_at.strftime("%d.%m.%Y %H:%M")
                get_updated_at.short_description = 'Последнее обновление'

        admin.site.register(Advertisement, AdvertisementAdmin)
        def __str__(self):
            return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

        class Meta:
            db_table = "advertisements"