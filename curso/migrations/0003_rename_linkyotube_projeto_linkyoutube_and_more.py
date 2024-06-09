# Generated by Django 4.0.6 on 2024-04-22 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_disciplina_cursos_alter_disciplina_semestre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='linkYotube',
            new_name='linkYoutube',
        ),
        migrations.AddField(
            model_name='linguagem',
            name='disciplina',
            field=models.ManyToManyField(to='curso.disciplina'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='disciplina',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='projeto', to='curso.disciplina'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='curso'),
        ),
    ]