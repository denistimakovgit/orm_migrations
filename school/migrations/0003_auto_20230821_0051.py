# Generated by Django 3.1.2 on 2023-08-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20230820_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher', verbose_name='Учителя'),
        ),
    ]
