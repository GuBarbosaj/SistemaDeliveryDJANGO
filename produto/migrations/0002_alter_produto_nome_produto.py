# Generated by Django 3.2.5 on 2021-07-10 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome_produto',
            field=models.CharField(max_length=100),
        ),
    ]