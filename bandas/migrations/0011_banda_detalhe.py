# Generated by Django 4.0.6 on 2024-05-27 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0010_remove_banda_detalhe'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='detalhe',
            field=models.CharField(max_length=255, null=True),
        ),
    ]