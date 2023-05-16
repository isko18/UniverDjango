from django.db import models

# Create your models here.
class Courses(models.Model):
    name_course = models.CharField(
        max_length=255,
        verbose_name="Название курса"
    )
    foto_course = models.ImageField(
        upload_to="product/",
        verbose_name="Фотография продукта"
    )
    price = models.BigIntegerField(
        verbose_name="Цена курса"
    )
    desc_course = models.TextField(
        max_length=255,
        verbose_name="Описание продукта"       
    )
    less = models.BigIntegerField(
        verbose_name="Количество занятий"
    )
    students = models.BigIntegerField(
        verbose_name="Количество студентов"
    )

    def __str__(self):
        return self.name_course
    
    class Meta:
        verbose_name = "Наши курсы"
        verbose_name_plural = "Наши курсы"