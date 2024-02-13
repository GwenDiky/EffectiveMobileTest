from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Catalog(models.Model):
    surname = models.CharField("Фамилия", max_length = 100)
    name = models.CharField("Имя", max_length = 100)
    patronymic = models.CharField("Отчество", max_length = 100)
    organisation = models.CharField("Организация", max_length = 200)

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    work_phone = models.CharField("Рабочий телефон", validators = [phoneNumberRegex],
                                 max_length = 16, unique = True, help_text="+7(XXX)XXX-XX-XX")
    personal_phone = models.CharField("Личный телефон", validators = [phoneNumberRegex],
                                 max_length = 16, unique = True)

    def get_absolute_url(self):
        return f'/{self.pk}/'

    class Meta:
        verbose_name = "Справочная информация"
        verbose_name_plural = "Справочник"




