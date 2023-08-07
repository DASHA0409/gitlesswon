from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'advertisements'

    def ready(self):
        super().ready()
        self.verbose_name = 'Объявления'
