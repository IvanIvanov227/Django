from django.db import models
from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import format_html

from django.contrib.auth import get_user_model

User = get_user_model()


def start_with_vop(value):
    if value.lstrip()[0] == '?':
        raise ValidationError("Заголовок не может начинаться с '?'")


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128, validators=[start_with_vop])
    description = models.TextField('Описание')
    # max_digits - max число цифр во всём числе
    # decimal_places - длина дробной части
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    # Автоматическое заполнение (auto_now_add и auto_now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Если user будет удалён, то все связанные объявления тоже будут удалены
    user = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements')

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Последнее обновление')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: blue; font-weight: bold;">Сегодня в {}</span>', created_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description="Фотография")
    def get_admin_image(self):
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width="100" height="100" class="img-fluid rounded-start" alt="Фото объявления">')
        else:
            return format_html(
                f'<img src="/static/img/adv.png" width="100" height="100" class="img-fluid rounded-start" alt="Фото объявления">')

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    class Meta:
        db_table = 'advertisements'
