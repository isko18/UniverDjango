# Generated by Django 4.2 on 2023-05-11 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_site', models.CharField(max_length=150, verbose_name='Название колледжа')),
                ('logo_site', models.ImageField(upload_to='logo/', verbose_name='Логотип колледжа')),
                ('info_site', models.CharField(max_length=255, verbose_name='Дополнительная информация о колледже')),
            ],
            options={
                'verbose_name': 'Настройки колледжа',
                'verbose_name_plural': 'Настройки колледжа',
            },
        ),
    ]
