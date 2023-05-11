# Generated by Django 3.2.17 on 2023-02-17 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_modify_author', 'Modify author (create,update,delete)'),)},
        ),
    ]