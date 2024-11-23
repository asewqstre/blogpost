# Generated by Django 5.1.3 on 2024-11-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('pub_datetime', models.DateTimeField(verbose_name='Дата и время опубликования')),
                ('content', models.TextField(verbose_name='Содержание')),
            ],
        ),
    ]
