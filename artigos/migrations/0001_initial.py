# Generated by Django 4.0.6 on 2024-06-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorName', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('comentario', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
            ],
        ),
    ]