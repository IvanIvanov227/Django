from django.db import models


class Advertisement(models.Model):
    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'

    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    # max_digits - max число цифр во всём числе
    # decimal_places - длина дробной части
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    # Автоматическое заполнение (auto_now_add и auto_now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
