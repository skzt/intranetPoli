# Generated by Django 2.2 on 2021-05-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
        migrations.AlterField(
            model_name='links',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]