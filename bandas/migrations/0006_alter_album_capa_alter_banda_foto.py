# Generated by Django 4.0.6 on 2024-04-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0005_banda_ano_de_criacao_banda_nacionalidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bandas'),
        ),
        migrations.AlterField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='bandas/'),
        ),
    ]
