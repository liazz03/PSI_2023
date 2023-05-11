# Generated by Django 3.2.17 on 2023-02-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_rename_date_of_birth_author_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='birth',
        ),
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Birth'),
        ),
    ]