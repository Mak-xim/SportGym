from django.db import models

class Abonement(models.Model):
    number = models.CharField(max_length=200,  verbose_name="Количество занятий")
    price = models.IntegerField( verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Дополнительное описание")


    def __str__(self):
        return self.number
