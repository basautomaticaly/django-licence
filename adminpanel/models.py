from django.db import models


class License(models.Model):
    user_tg = models.CharField(max_length=255, unique=True, verbose_name='Тг юзера')
    user_hwid = models.CharField(max_length=255, unique=True, verbose_name='HWID пользователя')
    expiration_date = models.DateField(verbose_name='Дата окончания лицензии')

    def __str__(self):
        return f'User [ {self.user_tg} ] | HWID [ {self.user_hwid} ] | Expired Date [ {self.expiration_date} ]'

    class Meta:
        verbose_name = 'Лицензия'
        verbose_name_plural = 'Лицензии'

